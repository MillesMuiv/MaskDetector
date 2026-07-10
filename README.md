# Face Mask Detector

Real-time face mask detection using deep learning, with both **TensorFlow/Keras** and **PyTorch** implementations.

## Overview

This project detects whether a person is wearing a face mask in real-time via webcam. It uses a **MobileNetV2** backbone (pre-trained on ImageNet) with a custom classifier head, trained on a dataset of masked and unmasked faces.

Two independent training pipelines:
- **TensorFlow/Keras** – in [`train.ipynb`](train.ipynb)
- **PyTorch** – in [`torchmask.ipynb`](torchmask.ipynb)

The PyTorch model handles data properly (lazy dataloader, no data leakage) and is the **recommended** version.

## Features

- Real-time inference from webcam
- Face detection via OpenCV DNN (Caffe-based SSD)
- Mask classification with MobileNetV2
- Two trained models (Keras `.keras` / PyTorch `.pth`)
- Data augmentation & duplicate removal during training

## Project Structure

```
MaskDetector/
├── README.md
├── requirements.txt
├── setup.py
├── video.py                   # Real-time webcam inference script
├── train.ipynb                # TensorFlow/Keras training notebook
├── torchmask.ipynb            # PyTorch training notebook
├── test.py                    # Simple quick test
├── mask_detector_model.keras  # Trained TensorFlow model
├── mask_detector_torch.pth    # Trained PyTorch weights
├── face_detector/             # Caffe face detection model
│   ├── deploy.prototxt
│   └── res10_300x300_ssd_iter_140000.caffemodel
├── dataset/                   # Training images
│   ├── with_mask/
│   └── without_mask/
└── mask_detector.egg-info/    # Package metadata
```

## Requirements

- Python ≥ 3.8, < 3.13
- See [`requirements.txt`](requirements.txt) for full list

Key dependencies:
- PyTorch (CUDA 13.2) / TensorFlow ≥ 2.12
- OpenCV ≥ 4.5
- NumPy, scikit-learn, matplotlib, imutils

!!3.10 python version is highly recommended!!

Pull from github:

```bash
git clone https://github.com/MillesMuiv/MaskDetector
cd maskdetector
python3.10 venv .venv
```
For Windows:

```bash
source .venv/scripts/activate
```
For Linux:

```bash
source .venv/bin/activate
```
Install with pip:

```bash
pip install -r requirements.txt
```

## Usage

### Real-time detection (webcam)

Run the video inference script:

```bash
python video.py
```

- The script captures video from your default webcam (`src=0`)
- Faces are detected with the Caffe SSD model
- Each face is classified as **Mask** (green) or **No Mask** (red) with confidence %
- Press **q** to quit

### Training from scratch

#### TensorFlow / Keras
Open and run [`train.ipynb`](train.ipynb) – uses `ImageDataGenerator` for augmentation.

#### PyTorch
Open and run [`torchmask.ipynb`](torchmask.ipynb) – uses custom `MaskDataset` with `torchvision` transforms.

Both notebooks expect a `dataset/` directory containing:
```
dataset/
├── with_mask/
│   ├── image1.jpg
│   └── ...
└── without_mask/
    ├── image1.jpg
    └── ...
```

## Models

| Model | File | Framework |
|-------|------|-----------|
| Mask Detector (TF) | `mask_detector_model.keras` | TensorFlow/Keras |
| Mask Detector (PyTorch) | `mask_detector_torch.pth` | PyTorch |

Both use **MobileNetV2** as the feature extractor with a custom head:
- Global average pooling
- Fully-connected layer (128 units, ReLU)
- Dropout (0.5)
- Output layer (2 classes – with_mask / without_mask)

## Data Notes

- The dataset is **included** in this repository
- The training notebooks include duplicate detection (MD5 hashing) and stratified train/test splitting
- A `LabelEncoder` maps class names to integer labels
- The TensorFlow version uses one-hot encoding; the PyTorch version uses integer labels with `CrossEntropyLoss`
