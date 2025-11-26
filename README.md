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

<table border="1" cellspacing="0" cellpadding="6">
    <tr>
        <th>Metric</th>
        <th>Value (Local CPU)</th>
        <th>Estimated RasPi 5 (NCNN)</th>
    </tr>
    <tr>
        <td><b>Input Size</b></td>
        <td>320x320</td>
        <td>320x320</td>
    </tr>
    <tr>
        <td><b>Format</b></td>
        <td>PyTorch (.pt)</td>
        <td>NCNN (.ncnn)</td>
    </tr>
    <tr>
        <td><b>Inference Time</b></td>
        <td>~12.5 ms</td>
        <td>~5–8 ms</td>
    </tr>
    <tr>
        <td><b>FPS</b></td>
        <td>~80 FPS</td>
        <td>>100 FPS</td>
    </tr>
</table>





### Detection Results
(Sample output showing dark_blue class detection with confidence scores)

### Limitations:
1. Due to the limited size of the training dataset, the model currently operates best with a lower confidence threshold (0.25).
2. Future improvements will involve collecting more diverse data to improve High-Confidence Precision.

## 📂 Project Structure

The project follows a modular Python package structure, designed for scalability and ease of deployment.

```text
bsort_project/
├── .github/
│   └── workflows/
│       └── ci_cd.yaml       # GitHub Actions pipeline (Lint, Test, Build)
├── bsort/                   # Core Source Code Package
│   ├── __init__.py          # Package initialization
│   ├── main.py              # CLI Entry Point (handles 'train' and 'infer' commands)
│   ├── infer.py             # Inference Engine (YOLOv8 wrapper & logic)
│   └── utils.py             # Helper functions (HSV logic, preprocessing)
├── config/
│   └── settings.yaml        # Centralized configuration (thresholds, model paths)
├── tests/                   # Unit Tests
│   └── test_basic.py        # Pytest cases for config and imports
├── .dockerignore            # Specifies files to exclude from Docker builds
├── .gitignore               # Specifies files to ignore in Git (datasets, models)
├── Dockerfile               # Docker configuration for containerized deployment
├── pyproject.toml           # Project metadata, dependencies, and CLI script definitions
├── README.md                # Project documentation and usage guide
└── requirements.txt         # List of Python dependencies

Created by Risha Alfanda
