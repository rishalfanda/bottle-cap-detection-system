# BSORT: Bottle Cap Color Detection System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![YOLOv8](https://img.shields.io/badge/YOLO-v8n-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

**BSORT** is a lightweight Computer Vision pipeline designed to detect and classify bottle caps (Light Blue, Dark Blue, Others) in real-time. Designed for edge deployment (Raspberry Pi 5).

## 📌 Project Overview
The system processes video frames/images to segregate bottle caps based on color using a custom-trained YOLOv8 Nano model. It includes a CLI tool for easy inference and is containerized using Docker.

## 🚀 Features
- **Auto-Relabeling Pipeline:** Converts raw YOLO labels to color-specific classes using HSV filtering.
- **Edge Optimized:** Uses YOLOv8 Nano and supports NCNN export for ARM devices.
- **Robust CLI:** Simple command-line interface for inference.
- **Dockerized:** Ready for deployment in any environment.

## 🛠️ Installation

### Option 1: Local Python (Recommended for Dev)

# 1. Clone repository
git clone [https://github.com/rishalfanda/bsort.git](https://github.com/rishalfanda/bsort.git)
cd bsort

# 2. Install package
pip install .

### Option 2: Docker (Production)

docker build -t bsort:latest .
docker run --rm -v $(pwd):/app/data bsort:latest infer --image /app/data/test.jpg

## Usage
Run inference on an image:
### Using the installed CLI
bsort infer --image tests/test.jpg --config config/settings.yaml
## Configuration (config/settings.yaml):
model:
  path: "./best.pt"
  conf_threshold: 0.25  # Lowered for higher recall on challenging datasets
  img_size: 640         # Adjustable: 320 for speed, 640 for accuracy

## Performance & Analysis
Hardware Constraints
1. Target Device: Raspberry Pi 5 (Edge)
2. Constraint: Inference time < 10ms

### Optimization Strategy
Since a physical Raspberry Pi was unavailable, performance was benchmarked on a local CPU using Resolution Scaling to simulate edge constraints.
MetricValue (Local CPU)Estimated RasPi 5 (NCNN)Input Size320x320320x320FormatPyTorch (.pt)NCNN (.ncnn)Inference Time~12.5 ms~5-8 msFPS~80 FPS>100 FPS
Note: Reducing input resolution to 320x320 reduces computational load by ~75%, allowing the model to meet the <10ms target on ARM CPUs.

### Detection Results
(Sample output showing dark_blue class detection with confidence scores)

### Limitations:
1. Due to the limited size of the training dataset, the model currently operates best with a lower confidence threshold (0.25).
2. Future improvements will involve collecting more diverse data to improve High-Confidence Precision.

## Project Structure

bsort/
├── bsort/           # Core Source Code
│   ├── main.py      # CLI Entry Point
│   ├── infer.py     # Inference Engine
│   └── ...
├── config/          # Configuration Files
├── tests/           # Unit Tests
├── Dockerfile       # Container Setup
└── pyproject.toml   # Project Metadata

Created by Risha Alfanda
