#!/usr/bin/env python3
"""
Simple system statistics module for extracting xlnx-config data
"""

import subprocess
import re
import os


def check_root_privileges():
    """Check if script is running with root privileges"""
    return os.geteuid() == 0


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
