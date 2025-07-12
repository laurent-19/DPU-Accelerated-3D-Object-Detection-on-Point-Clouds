
# DPU-Accelerated 3D Object Detection on Point Clouds

> **Credits:**  
> This project is based on the original at [Hackster.io: Point Clouds Based 3D Object Detection on PYNQ DPU](https://www.hackster.io/447969/point-clouds-based-3d-object-detection-on-pynq-dpu-c26930).
>
> **Contributors:**  
> - **Xinyu Chen**  
>   [GitHub](https://github.com/SoldierChen)  
>   PhD student at National University of Singapore  
> - **Vera Lee**
>
> The source code and further updates are available on [GitHub](https://github.com/SoldierChen/DPU-Accelerated-3D-Object-Detection-on-Point-Clouds/tree/main).


## Get Started!

Below are detailed instructions to implement the efficient 3D object detection system on the KV260 board, including model training, quantization, compilation, and deployment.

### Setup Environment

1. Install the Ubuntu 20.04 image to KV260 according to the [official guide](https://ubuntu.com/download/amd).
2. Install PYNQ in the Ubuntu operating system (see [PYNQ GitHub](https://github.com/Xilinx/Kria-PYNQ) for details).
3. Clone this repository:

```bash
git clone https://github.com/laurent-19/DPU-Accelerated-3D-Object-Detection-on-Point-Clouds.git
cd DPU-Accelerated-3D-Object-Detection-on-Point-Clouds
```

> **Note:** PyTorch 1.4 is required as the VART of PYNQ DPU is v1.4.

### Data Preparation

The KITTI 3D detection dataset is required for training, validation, and testing. The demo scripts will automatically download a small demo dataset for inference, but for full training and evaluation, download the official KITTI dataset from [here](https://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d) and organize it as follows:

```
dataset/kitti/
├── ImageSets/
│   ├── train.txt
│   ├── val.txt
│   └── test.txt
├── training/
│   ├── calib/
│   ├── image_2/
│   ├── label_2/
│   └── velodyne/
└── testing/
    ├── calib/
    ├── image_2/
    └── velodyne/
```

- `velodyne/`: 3D point clouds (bin files)
- `label_2/`: Object detection labels (for training/validation)
- `calib/`: Camera and lidar calibration files
- `image_2/`: Left color images (optional, for visualization)
- `ImageSets/`: Text files listing train/val/test splits

To visualize 3D point clouds with 3D boxes, run:

```bash
cd model_quant_compile/data_process/
python kitti_dataset.py
```

> **Note:** The script automatically selects the `training` or `testing` subfolder based on the mode. For example, if `self.mode = 'test'`, it uses the `testing` folder; otherwise, it uses `training`.

### Model Training

```bash
python train.py --gpu_idx 0
```

You can select either the FPN ResNet or the ResNet as the target model. The trained model will be stored in the checkpoint folder. Depending on your hardware, the number of epochs can be from 10 to 300 (higher is better for accuracy).

### Model Quantization and Compilation

As the VART of PYNQ is v1.4, use VITIS AI v1.4 (not v2.0) for model quantization.

```bash
# Install the docker if not already installed
docker pull xilinx/vitis-ai-cpu:1.4.1.978  
```

```bash
# Run the docker
./docker_run.sh xilinx/vitis-ai-cpu:1.4.1.978
```

You are now inside the Vitis AI Docker container. The prompt should look like:

```
Vitis-AI /workspace > 
```

From here, you can proceed with model quantization and compilation steps as described below.

#### Quantize the model

```bash
# Activate the PyTorch environment
conda activate vitis-ai-pytorch 
```

```bash
# Install required packages
pip install -r requirements.txt
```

To quantize the model, first navigate to the `sfa` directory:

```bash
cd sfa
```

```bash
# Quantization (calibration mode)
python quantize.py --quant_mode calib
```

This will run quantization in calibration mode. Main options:
- `--build_dir`: Output directory for quantized/compiled models (default: `build`)
- `--quant_mode`: Quantization mode (`calib` for calibration, `test` for test/output)
- `--batchsize`: Batch size for quantization (default: 100)

You should see log output similar to:

```
[VAIQ_NOTE]: Loading NNDCT kernels...

-----------------------------------------
PyTorch version :  1.4.0
3.6.13 | packaged by conda-forge
[GCC 9.4.0]
-----------------------------------------
 Command line options:
--build_dir    :  build
--quant_mode   :  calib
--batchsize    :  100
```

```bash
# Quantization (test/output mode)
```bash
python quantize.py --quant_mode test
```

This will run quantization in test/output mode. During this process, the script will evaluate the quantized model on the test set. You should see output similar to the following:

```
[VAIQ_NOTE]: Loading NNDCT kernels...

-----------------------------------------
PyTorch version :  1.4.0
3.6.13 | packaged by conda-forge
[GCC 9.4.0]
-----------------------------------------
 Command line options:
--build_dir    :  build
--quant_mode   :  test
--batchsize    :  100
-----------------------------------------
ResNet architecture with feature pyramid
loaded pretrained model at ./fpn_resnet_18_epoch_300.pth

[VAIQ_NOTE]: Quantization test process start up...
[VAIQ_NOTE]: =>Quant Module is in 'cpu'.
[VAIQ_NOTE]: =>Parsing PoseResNet...
[VAIQ_NOTE]: =>Doing weights equalization...
[VAIQ_NOTE]: =>Quantizable module is generated.(build/quant_model/PoseResNet.py)
[VAIQ_NOTE]: =>Get module with quantization.
num_samples7518
    Done testing the 0th sample, time: xx.xx ms, speed y.yy FPS
    Done testing the 1th sample, time: xx.x ms, speed y.yy FPS
    ...
[VAIQ_NOTE]: =>Converting to xmodel ...
[VAIQ_NOTE]: =>Successfully convert 'PoseResNet' to xmodel.(build/quant_model/PoseResNet_int.xmodel)
```

During testing, output images and results are saved to the `results/fpn_resnet_18/` directory for each sample processed.

### Compile the model

To compile the quantized model for the KV260 (using the zcu102 DPU architecture), run:

```bash
sudo ./compile.sh zcu102 build/
```

> **Note:** The zcu102 shares the same DPU architecture as the KV260.

During compilation, you may see a message like:

```
-----------------------------------------
COMPILING MODEL FOR ZCU102..
-----------------------------------------
MODEL COMPILED
-----------------------------------------
```

After successful compilation, a compiled `.xmodel` file will be generated in the `build/` directory. This file can be deployed and executed on the DPU overlay on the KV260 board.

## Deployment and Inference on KV260

This section provides a step-by-step guide to deploy the compiled `.xmodel` to the KV260 board and run DPU-accelerated inference, including setup, environment configuration, and demo execution.

### 1. Copy the Compiled Model from Docker

After compiling the `.xmodel` inside the Vitis AI Docker container:

- List running containers to find the Vitis AI container ID:
    ```bash
    docker ps -a
    ```
- Copy the compiled `.xmodel` from the container to your host (replace `<container_id>` as needed):
    ```bash
    docker cp <container_id>:/workspace/sfa/build/compiled_model/CNN_zcu102.xmodel ./
    ```

### 2. Transfer the Model to KV260

- Transfer the `.xmodel` to the target board (the default username is usually `ubuntu` for the official AMD Ubuntu image; replace `<kv260_ip>` with your board's IP address):
    ```bash
    scp CNN_zcu102.xmodel ubuntu@<kv260_ip>:/home/ubuntu/DPU-Accelerated-3D-Object-Detection-on-Point-Clouds/sfa/
    ```

### 3. Prepare the KV260 Environment

- SSH into the KV260 and navigate to the project directory:
    ```bash
    ssh <user>@<kv260_ip>
    cd /home/ubuntu/DPU-Accelerated-3D-Object-Detection-on-Point-Clouds/sfa
    ```
- (Optional) Switch to root for setup:
    ```bash
    sudo -i
    cd /home/ubuntu/DPU-Accelerated-3D-Object-Detection-on-Point-Clouds/sfa
    ```
- Configure the PyTorch environment to avoid static TLS block errors:
    ```bash
    export LD_PRELOAD=/usr/lib/python3.8/site-packages/torch.libs/libgomp-*.so.*
    ```
    **Note:** This step is crucial to prevent `ImportError: ...libgomp*.so.* cannot allocate memory in static TLS block`.

### 4. Run Demo Scripts

Change to the `sfa` directory and execute the desired demo script:

```bash
cd sfa
```

Available demo scripts:

- `demo_front-dpu.py`: DPU-accelerated inference (front view).
- `demo_2_sides-dpu.py`: DPU-accelerated inference (front and back views).
- `demo_2_sides-dpu-live.py`: Live video rendering (front and back views).
- `demo_front-dpu-stats.py`: Inference (front view) with system/inference statistics logged to CSV.
- `demo_2_sides-dpu-stats.py`: Inference (front and back) with statistics logged to CSV.

Example commands:

#### Front view detection

```bash
python3 demo_front-dpu.py
```

#### Two-sided detection

```bash
python3 demo_2_sides-dpu.py
```

#### Front view detection with stats logging

```bash
python3 demo_front-dpu-stats.py
```

#### Two-sided detection with stats logging

```bash
python3 demo_2_sides-dpu-stats.py
```

#### Live video rendering (front and back)

```bash
python3 demo_2_sides-dpu-live.py
```

### 5. System and Inference Statistics

The statistics-enabled scripts log per-frame metrics to CSV, including:

- DPU inference FPS (front/back)
- SOM total power (mW)
- Programmable Logic (PL) temperature (°C)
- System memory (total/free, kB)
- Per-core CPU utilization (%)

All statistics are measured using `xlnx-config -x platformstats -a` and saved for benchmarking.

**Example CSV Output:**

```csv
Frame,Front_DL_FPS,Back_DL_FPS,Power_mW,PL_temp_C,MemTotal_kB,MemFree_kB,CPU0_usage_%,CPU1_usage_%,CPU2_usage_%,CPU3_usage_%
0,7.95,8.05,4900,31,4025304,593708,33.77,11.1,40.92,43.1
1,7.98,8.05,4760,31,4025304,596940,78.1,49.60,28.97,48.58
```

---

By following these steps, you can deploy your quantized and compiled model to the KV260 and run DPU-accelerated 3D object detection with performance and system monitoring.
