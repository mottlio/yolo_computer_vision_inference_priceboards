# Gas Station Priceboard Detection

This project aims to automatically detect fuel price boards from dashcam footage and extract price information for large-scale fuel price monitoring.

---

## Objective

The goal is to build a pipeline that:

1. Captures short video clips while driving past gas stations  
2. Detects priceboards using a YOLO object detection model  
3. Crops the detected region  
4. Extracts fuel prices using OCR  
5. Stores results for analysis  

---

## Approach

- **Object Detection:** YOLO (Ultralytics YOLO11)
- **Data Source:** Dashcam-style video clips of Polish gas stations + still images
- **Annotation Tool:** CVAT
- **Training Environment:** Google Colab (GPU)
- **Inference:** Local (VSCode)

---

## 📂 Project Structure

├── data/ # datasets (not tracked in git)
├── models/ # trained weights ('best.pt' file - output of training YOLO on frames labelled using CVAT)
├── scripts/
│ ├── extract_frames.py
│ ├── test_yolo.py
│ └── utils.py
├── notebooks/ # optional Colab notebooks
├── runs/ # YOLO outputs (ignored in git)
└── README.md



## Setup

### 1. Create virtual environment

```zsh
python3.11 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

pip install --upgrade pip
pip install "numpy<2" ultralytics  #For some reason ultralytics doesn't play well with numpy>2


## Training

I used Google Colab with a T4 GPU as runtime. ~ 400 images labelled in CVAT and exprted in YOLO Ultralytics Detection format (I want to know where the priceboards are). 

Link to my [Google Colab notebook](https://colab.research.google.com/drive/1cnkozosInB-HwFON6FeqY9JM7MK-LK3L?usp=sharing) 

## Running inference locally

- we need a trained model - output of training a YOLO model (best.pt). 
- folder with test frames from new videos (not used for training)

### Create a new virtual environment (I use uv)

```bash
uv venv .venv-yolo --python 3.11
source .venv-yolo/bin/activate
```
### Install dependencies

```bash
uv init #creates pyproject.toml
uv pip install "numpy<2" ultralytics
```
### Test it

```bash
python -c "from ultralytics import YOLO; print('YOLO ready')"
```