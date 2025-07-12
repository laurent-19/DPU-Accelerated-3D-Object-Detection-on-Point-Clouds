# -----------------------------------------------------------------------------------
# Description: 
# DPU-accelerated 3D object detection on point clouds (front view only).
# Runs inference on KITTI data, collects system stats, and logs results.
#
# This script is designed for Xilinx Kria KV260 (uses same dpu compile as ZCU102)
# using the Xilinx DPU (Deep-learning Processing Unit) overlay for hardware-accelerated
# inference. It uses the pynq_dpu Python API to interact with the DPU.
#
# During inference, the script measures and logs the following system statistics:
#   - DPU inference FPS (frames per second)
#   - SOM (System-on-Module) total power consumption (mW)
#   - Programmable Logic (PL) temperature (°C)
#   - Total and free system memory (kB)
#   - Per-core CPU utilization (% for CPU0-CPU3)
#
# System statistics are collected using the 'xlnx-config -x platformstats -a' command,
# which is specific to Xilinx platforms and provides detailed hardware monitoring data.
# All results are saved to a CSV file for further analysis.
# -----------------------------------------------------------------------------------
# Author: laurent-19 (Popa Ioan Laurentiu)
# -----------------------------------------------------------------------------------

import sys
import os
import warnings
import csv
import subprocess
import re
from datetime import datetime

warnings.filterwarnings("ignore", category=UserWarning)

import cv2
import torch
import numpy as np

src_dir = os.path.dirname(os.path.realpath(__file__))
if src_dir not in sys.path:
    sys.path.append(src_dir)

from data_process.demo_dataset import Demo_KittiDataset
from models.model_utils import create_model
from utils.evaluation_utils import draw_predictions, convert_det_to_real_values
import config.kitti_config as cnf
from data_process.transformation import lidar_to_camera_box
from utils.visualization_utils import merge_rgb_to_bev, show_rgb_image_with_boxes
from data_process.kitti_data_utils import Calibration
from utils.demo_utils import parse_demo_configs, download_and_unzip, write_credit
from utils.misc import make_folder, time_synchronized
from utils.evaluation_utils import decode, post_processing
from utils.torch_utils import _sigmoid


from pynq_dpu import DpuOverlay


def get_system_stats():
    """Get system statistics and return as dictionary (quiet version)"""
    try:
        # Try without sudo first
        result = subprocess.run('xlnx-config -x platformstats -a', 
                               shell=True, capture_output=True, text=True, timeout=15)
        
        # Check if we got valid output even with non-zero return code
        output = result.stdout
        if not output or "CPU Utilization" not in output:
            # Try with sudo
            result = subprocess.run('sudo -n xlnx-config -x platformstats -a', 
                                   shell=True, capture_output=True, text=True, timeout=15)
            output = result.stdout
            
            if not output or "CPU Utilization" not in output:
                return None
            
        # Parse the output
        stats = {}
        
        # Parse CPU utilization
        cpu_pattern = r'CPU(\d+)\s*:\s*([\d.]+)%'
        cpu_matches = re.findall(cpu_pattern, output)
        for cpu_id, usage in cpu_matches:
            stats[f'CPU{cpu_id}_usage_%'] = float(usage)
        
        # Parse power
        power_pattern = r'SOM total power\s*:\s*(\d+)\s*mW'
        power_match = re.search(power_pattern, output)
        if power_match:
            power = int(power_match.group(1))
            stats['SOM_total_power_mW'] = power
        
        # Parse temperature
        temp_pattern = r'PL temperature\s*:\s*(\d+)\s*C'
        temp_match = re.search(temp_pattern, output)
        if temp_match:
            temp = int(temp_match.group(1))
            stats['PL_temp_C'] = temp
        
        # Parse memory info
        mem_total_pattern = r'MemTotal\s*:\s*(\d+)\s*kB'
        mem_total_match = re.search(mem_total_pattern, output)
        if mem_total_match:
            mem_total = int(mem_total_match.group(1))
            stats['MemTotal_kB'] = mem_total
        
        mem_free_pattern = r'MemFree\s*:\s*(\d+)\s*kB'
        mem_free_match = re.search(mem_free_pattern, output)
        if mem_free_match:
            mem_free = int(mem_free_match.group(1))
            stats['MemFree_kB'] = mem_free
        
        return stats
        
    except subprocess.TimeoutExpired:
        return None
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

def init_csv_file(csv_filename):
    """Initialize CSV file with headers"""
    headers = [
        'Frame', 'Front_DL_FPS', 'Power_mW',
        'PL_temp_C', 'MemTotal_kB', 'MemFree_kB',
        'CPU0_usage_%', 'CPU1_usage_%', 'CPU2_usage_%', 'CPU3_usage_%'
    ]
    
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
    
    return headers


def write_stats_to_csv(csv_filename, frame_id, front_fps, system_stats, headers):
    """Write frame statistics to CSV file"""
    row = {
        'Frame': frame_id,
        'Front_DL_FPS': front_fps
    }
    
    # Add system stats if available
    if system_stats:
        # Map system stats to CSV headers
        if 'SOM_total_power_mW' in system_stats:
            row['Power_mW'] = system_stats['SOM_total_power_mW']
        if 'PL_temp_C' in system_stats:
            row['PL_temp_C'] = system_stats['PL_temp_C']
        if 'MemTotal_kB' in system_stats:
            row['MemTotal_kB'] = system_stats['MemTotal_kB']
        if 'MemFree_kB' in system_stats:
            row['MemFree_kB'] = system_stats['MemFree_kB']
        
        # Map CPU usage stats
        for i in range(4):
            cpu_key = f'CPU{i}_usage_%'
            if cpu_key in system_stats:
                row[cpu_key] = system_stats[cpu_key]
    
    # Fill missing values with None
    for header in headers:
        if header not in row:
            row[header] = None
    
    with open(csv_filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writerow(row)

def do_detect(dpu, shapeIn, image, input_data, output_data, configs, bevmap, is_front):
    
    if not is_front:
        bevmap = torch.flip(bevmap, [1, 2])
    input_bev_maps = bevmap.unsqueeze(0).to("cpu", non_blocking=True).float()
    input_bev_maps = input_bev_maps.permute(0, 2, 3, 1)
    
    image[0,...] = input_bev_maps[0,...] #.reshape(shapeIn[1:])

    t1 = time_synchronized() 
    
    job_id = dpu.execute_async(input_data, output_data)
    
    dpu.wait(job_id)

    t2 = time_synchronized() 

    inference_time = (t2 - t1) * 1000  # Convert to milliseconds
    fps = 1 / (t2 - t1)
        
    outputs0 = torch.tensor(output_data[0])
    outputs1 = torch.tensor(output_data[1])
    outputs2 = torch.tensor(output_data[2])
    outputs3 = torch.tensor(output_data[3])
    outputs4 = torch.tensor(output_data[4])
    
    outputs0 = outputs0.permute(0, 3, 1, 2)
    outputs1 = outputs1.permute(0, 3, 1, 2)
    outputs2 = outputs2.permute(0, 3, 1, 2)
    outputs3 = outputs3.permute(0, 3, 1, 2)
    outputs4 = outputs4.permute(0, 3, 1, 2)

    outputs0 = _sigmoid(outputs0)
    outputs1 = _sigmoid(outputs1)
    
    detections = decode(
                        outputs0,
                        outputs1,
                        outputs2,
                        outputs3,
                        outputs4, K=configs.K)
        
    detections = detections.cpu().numpy().astype(np.float32)
    detections = post_processing(detections, configs.num_classes, configs.down_ratio, configs.peak_thresh)

    return detections[0], bevmap, fps, inference_time





if __name__ == '__main__':
    configs = parse_demo_configs()

    # Try to download the dataset for demonstration
    server_url = 'https://s3.eu-central-1.amazonaws.com/avg-kitti/raw_data'
    download_url = '{}/{}/{}.zip'.format(server_url, configs.foldername[:-5], configs.foldername)
    download_and_unzip(configs.dataset_dir, download_url)

    demo_dataset = Demo_KittiDataset(configs)
    
    csv_filename = os.path.join(configs.results_dir, '{}_stats.csv'.format(configs.foldername))
    headers = init_csv_file(csv_filename)
    print(f'Stats will be saved to: {csv_filename}')
    
    overlay = DpuOverlay("dpu.bit")
    overlay.load_model("./10ep_resnet_CNN_zcu102.xmodel")
    dpu = overlay.runner
    
    inputTensors = dpu.get_input_tensors()
    outputTensors = dpu.get_output_tensors()

    shapeIn = tuple(inputTensors[0].dims)
    
    #print("shapein", shapeIn)
    
    outputSize = int(outputTensors[0].get_data_size() / shapeIn[0])

    shapeOut = tuple(outputTensors[0].dims)
    shapeOut1 = tuple(outputTensors[1].dims)
    shapeOut2 = tuple(outputTensors[2].dims)
    shapeOut3 = tuple(outputTensors[3].dims)
    shapeOut4 = tuple(outputTensors[4].dims)

    #print(shapeOut,shapeOut1,shapeOut2,shapeOut3,shapeOut4)
    
    output_data = [np.empty(shapeOut, dtype=np.float32, order="C"),
                  np.empty(shapeOut1, dtype=np.float32, order="C"),
                  np.empty(shapeOut2, dtype=np.float32, order="C"),
                  np.empty(shapeOut3, dtype=np.float32, order="C"),
                  np.empty(shapeOut4, dtype=np.float32, order="C")]
    
    input_data = [np.empty(shapeIn, dtype=np.float32, order="C")]
    image = input_data[0]
    
    for sample_idx in range(len(demo_dataset)):
        metadatas, bev_map, img_rgb = demo_dataset.load_bevmap_front(sample_idx)
        detections, bev_map, fps, inference_time = do_detect(dpu, shapeIn, image, input_data, output_data, configs, bev_map, is_front=True)

        system_stats = get_system_stats()
        write_stats_to_csv(csv_filename, sample_idx, fps, system_stats, headers)

    print(f'Benchmarking complete. Results saved to {csv_filename}')
