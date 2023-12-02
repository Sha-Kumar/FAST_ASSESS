from typing import Union
from fastapi import FastAPI

import cv2
import base64
import time
import os

app = FastAPI()

def time_calculator():
    # Milliseconds Precision time data
    return int(time.time() * 1000)


def image_capture(cap,timestamp,filePrefix):

    #Initalization
    currentFrame = 0

    # Run a loop to continuously capture and save images
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            break

        # Construct the filename with the timestamp
        file_path = f"{filePrefix}/{timestamp}/image_{currentFrame}.jpg"

        # Save the image to the specified file path
        cv2.imwrite(file_path, frame)

        # Increment loop parameter
        currentFrame += 1

        # # Display the captured frame (optional, you can remove this line if not needed)
        # cv2.imshow('Captured Image', frame)

        if currentFrame > 9:
            break
        
    if currentFrame > 9:
        return True
    return False



def capture():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "Error: Could not open webcam."

    folderName = "CAPTURES"

    # Create a directory for storing captured images if it doesn't exist
    os.makedirs(folderName, exist_ok=True)

    # write images
    success = image_capture(cap,time_calculator(),folderName)
    if success == True:
        return "Images Captured Successfully"

    return "Something Went wrong"


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test")
def test():
    return {"Hello": "Test API"}

@app.get("/access")
def access():
    return capture()