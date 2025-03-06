# Face Detection

## Overview
This project captures video from a webcam, detects faces in real-time using OpenCV's Haar Cascade classifier, and collects facial image data. It highlights detected faces with rectangles and counts the number of faces detected in each frame.

## Features
- Real-time face detection using OpenCV.
- Captures and stores up to 100 facial images.
- Draws bounding boxes around detected faces.
- Displays the number of detected faces on the video feed.
- Stops capturing when the 'q' key is pressed.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install opencv-python numpy
```

## How to Run
1. Install the required dependencies.
2. Run the script:

```bash
python face_detection.py
```

3. The webcam feed will open, detecting faces in real-time.
4. Press 'q' to stop the script and close the window.

## Code Explanation
- Captures video feed using OpenCV's `cv2.VideoCapture(0)`.
- Converts frames to grayscale for better face detection.
- Uses `haarcascade_frontalface_default.xml` for face detection.
- Extracts and resizes detected faces to 50x50 pixels.
- Stores up to 100 face images in a list.
- Displays the count of detected faces on the video feed.
- Terminates upon pressing the 'q' key.

## Possible Enhancements
- Save collected face images to disk for future use.
- Implement deep learning-based face detection for higher accuracy.
- Add facial recognition to identify known faces.

## License
This project is open-source and free to use.

