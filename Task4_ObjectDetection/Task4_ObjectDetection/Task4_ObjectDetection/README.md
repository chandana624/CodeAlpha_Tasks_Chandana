# Object Detection and Tracking

## Project Description

The Object Detection application is a web-based project that detects objects in uploaded images using the YOLO deep learning model.

The application allows the user to upload an image and displays the detected objects with bounding boxes and labels.

## Features

- Upload an image
- Detect objects using YOLO
- Display bounding boxes
- Display detected object labels
- Simple web interface
- Flask-based application

## Technologies Used

- Python
- Flask
- OpenCV
- Ultralytics YOLO
- HTML
- CSS

## How It Works

1. User uploads an image.
2. Flask receives the uploaded image.
3. YOLO processes the image.
4. Objects are detected in the image.
5. OpenCV saves the annotated image.
6. The detected image is displayed on the webpage.

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
Run the application:

python app.py

Open the application in a web browser:

http://127.0.0.1:5000
Internship

This project is developed as part of the CodeAlpha Artificial Intelligence Internship.
