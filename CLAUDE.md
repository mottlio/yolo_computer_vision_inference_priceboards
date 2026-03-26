# CLAUDE.md

## Project Overview

Gas station priceboard detection using YOLO computer vision. Detects fuel price boards from dashcam footage, crops detections, and extracts prices via OCR.

## Tech Stack

- Python 3.11+ (use `uv` for dependency management)
- Ultralytics YOLO11 for object detection
- NumPy <2 (required for ultralytics compatibility)

## Key Files

- `test_yolo.py` - Main inference script: loads trained YOLO model and runs predictions on dashcam frames
- `best.pt` - Trained YOLO model weights (~400 CVAT-labeled images)
- `main.py` - Entry point (placeholder)

## Setup

```bash
uv venv .venv-yolo --python 3.11
source .venv-yolo/bin/activate
uv pip install "numpy<2" ultralytics
```

## Running Inference

```bash
python test_yolo.py
```

Inference reads frames from an external drive (`/Volumes/T7/Paliwowo/processed/frames_for_inference`). Results are saved by YOLO to `runs/` directory.

## Notes

- `runs/` directory is git-ignored (YOLO output)
- Training was done on Google Colab with T4 GPU
- Data is not tracked in git
