# YOLOv8 Object Detection for Autonomous Driving

This project implements YOLOv8 for vehicle detection in autonomous driving scenarios, achieving ~90% mAP50 accuracy.

## Project Structure
```
YOLOV8-S0E7/
├── weights/           # Trained model weights
│   ├── best.pt       # Best model (90% mAP50)
│   └── last.pt       # Last epoch
├── predict_video.py  # Video inference script
├── main.py          # Main training script
├── args.yaml        # Training arguments
├── results.csv      # Training metrics
└── *.png            # Training visualization plots
```

## Quick Start

### Installation
```bash
pip install ultralytics opencv-python
```

### Run Inference
```bash
python predict_video.py
```

## Results

- **mAP50**: ~90%
- **Training Time**: 50 epochs (~3 hours on RTX 3070)
- **Model**: YOLOv8s

## Training Metrics

View the training results:
- `results.csv` - Detailed metrics per epoch
- `results.png` - Training curves
- `confusion_matrix.png` - Model performance
- Various curve plots (F1, P, R, PR)

## Model Weights

The trained weights are located in the `weights/` folder:
- `best.pt` - Best validation performance
- `last.pt` - Final training epoch
