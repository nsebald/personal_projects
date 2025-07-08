# Computer Vision Final Project: Timeshock

This repository contains the Jupyter notebook for my Computer Vision final project: **Timeshock** - a comprehensive facial recognition system built for the DSAIS (Data Science & Artificial Intelligence Strategy) program at Emlyon Business School.

## Project Overview

This project demonstrates advanced computer vision techniques by building a complete facial recognition system that can identify multiple individuals. The system is designed for scenarios like building access control where students can be recognized and granted entry.

### Key Features
- **Face Detection**: Uses MTCNN (Multi-task Cascaded Convolutional Networks) to detect and crop faces from raw images
- **Face Recognition**: Implements a custom classifier using FaceNet (InceptionResnetV1) for multi-class classification
- **Real-time Recognition**: Includes live webcam functionality for real-time face tracking and identification
- **High Accuracy**: Achieves 69.38% test accuracy on a dataset of 46 different individuals

## Technical Implementation

### Phase 1: Face Detection
- **MTCNN Integration**: Automatically detects faces in raw images and creates cropped face datasets
- **Data Preprocessing**: Converts images to RGB format and applies tensor transformations
- **Dataset Creation**: Processes training and test datasets with 439 total images across 46 classes

### Phase 2: Face Recognition
- **Transfer Learning**: Uses pre-trained FaceNet model (InceptionResnetV1) with VGGFace2 weights
- **Custom Classifier**: Modifies the classification head to output 46 classes (one per person)
- **Training Process**: 
  - Freezes feature extraction layers
  - Trains only the classification layers
  - Uses SGD optimizer with CrossEntropyLoss
  - Achieves 98.44% validation accuracy after 3 epochs

### Phase 3: Real-time Application
- **Live Video Processing**: Implements webcam integration using OpenCV
- **Real-time Detection**: Continuously detects faces in video feed
- **Confidence Scoring**: Displays prediction confidence percentages
- **Visual Feedback**: Draws bounding boxes and labels around detected faces

## Dataset Structure
- **Training Data**: 400 images across 46 individuals (10-11 images per person)
- **Test Data**: 39 images for validation
- **Classes**: 46 different people including team members and classmates

## Technologies Used
- **PyTorch**: Deep learning framework for model training and inference
- **FaceNet**: Pre-trained face recognition model
- **MTCNN**: Face detection and alignment
- **OpenCV**: Computer vision operations and webcam integration
- **PIL/Pillow**: Image processing
- **Matplotlib**: Visualization and plotting
- **NumPy**: Numerical computations

## Performance Metrics
- **Training Accuracy**: 96.63% (final epoch)
- **Validation Accuracy**: 98.44% (final epoch)
- **Test Accuracy**: 69.38%
- **Model Architecture**: InceptionResnetV1 with custom classification head

## File Structure
- `Final Project_Timeshock.ipynb` — Complete Jupyter notebook with all implementation
- `samples/train/` — Original training images
- `samples/train_cropped/` — Processed face crops for training
- `samples/test/` — Original test images  
- `samples/test_cropped/` — Processed face crops for testing

## How to Use
1. Clone or download this repository
2. Install required dependencies (see Requirements section)
3. Open `Final Project_Timeshock.ipynb` in Jupyter Notebook or JupyterLab
4. Run cells sequentially to:
   - Process and crop face images
   - Train the face recognition model
   - Test on validation data
   - Run real-time face recognition via webcam

## Requirements
- Python 3.x
- Jupyter Notebook or JupyterLab
- PyTorch
- facenet-pytorch
- OpenCV
- PIL/Pillow
- Matplotlib
- NumPy

Install dependencies with:
```bash
pip install torch facenet-pytorch opencv-python pillow matplotlib numpy
```

## Portfolio
This project showcases advanced computer vision skills including:
- Deep learning model customization
- Transfer learning implementation
- Real-time video processing
- Multi-class classification
- Computer vision pipeline development

For more projects, visit my [GitHub profile](https://github.com/).

---
*Note: This project was developed as part of the Introduction to Deep Learning course at Emlyon Business School's DSAIS program.* 