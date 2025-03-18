# DPU-Accelerated 3D Object Detection on Point Clouds

## Overview
This project implements DPU-accelerated 3D object detection on point clouds. For comprehensive details and instructions, visit our [Hackster.io project page](https://www.hackster.io/projects/c26930/).

## System Requirements
- Root access for PYNQ environment scripts
- Python 3.8
- PyTorch

## Setup Instructions

1. Switch to root user:
```bash
sudo -i
```

2. Go to project directory:
```bash
cd /home/ubuntu/DPU-Accelerated-3D-Object-Detection-on-Point-Clouds
cd sfa
```

3. Configure PyTorch environment:
```bash
export LD_PRELOAD=/usr/lib/python3.8/site-packages/torch.libs/libgomp-*.so.*
```

**Important**: The environment variable export is crucial to avoid the error:
`ImportError: /usr/lib/[path to torch]/libgomp*.so.* cannot allocate memory in static TLS block`

## Demo Execution

Choose one of the following detection modes:

```bash
# Front view detection
python3 demo_front-dpu.py

# Two-sided detection
python3 demo_2_sides-dpu.py
```

For complete project documentation, refer to the Hackster.io link above.
