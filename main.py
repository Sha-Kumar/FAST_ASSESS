from fastapi import FastAPI, File, UploadFile, Body
from typing import List
from fastapi.middleware.cors import CORSMiddleware


import cv2
import time
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

slashOperator = "/"
imageCount = 10

def time_calculator():
    # Milliseconds Precision time data
    return int(time.time() * 1000)


async def image_capture(cap,timestamp,filePrefix):

    #Initalization
    currentFrame = 1

    # Run a loop to continuously capture and save images
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            break

        # Construct the filename with the timestamp
        file_path = f"{filePrefix}{slashOperator}{timestamp}{slashOperator}image_{currentFrame}.jpg"

        # Save the image to the specified file path
        cv2.imwrite(file_path, frame)

        # Increment loop parameter
        currentFrame += 1

        # # Display the captured frame (optional, you can remove this line if not needed)
        # cv2.imshow('Captured Image', frame)

        # Loop break condition
        if currentFrame > imageCount:
            break

    # Checking the possibilty of all images captured succefully or not  
    if currentFrame > imageCount:
        return True

    return False


async def capture():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return {"Error": "Could not open webcam."}

    timeCalc = time_calculator()
    folderName = "CAPTURES"

    # Create a directory for storing captured images if it doesn't exist
    os.makedirs(folderName, exist_ok=True)
    os.makedirs(folderName + slashOperator + str(timeCalc), exist_ok=True)


    # write images
    success = await image_capture(cap,timeCalc,folderName)

    if success == True:
        return {"msg":"Images Captured Successfully"}

    return {"error":"Something Went wrong, All images not captured"}


@app.get("/")
def read_root():
    return {"Hello World": "Hello World"}


@app.get("/test")
def test():
    return {"msg": "Test API"}

@app.get("/access")
async def access():
    try:
        return await capture()
    except:
        return {"exception":"Exceptions Occurred"}


async def store(files):
    timeCalc = time_calculator()
    folderName = "CAPTURES"

    # Create a directory for storing captured images if it doesn't exist
    os.makedirs(folderName, exist_ok=True)
    os.makedirs(folderName + slashOperator + str(timeCalc), exist_ok=True)


    # write images
    await image_store(files,timeCalc,folderName)
    return {"msg":"Images Stored Successfully"}


async def image_store(files,timestamp,filePrefix):

    # Iterate through the uploaded files
    currentFrame=1
    for file in files:
        # Read the image file
        contents = await file.read()
        np_array = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

        # Generate a unique filename
        file_path = f"{filePrefix}{slashOperator}{timestamp}{slashOperator}image_{currentFrame}.jpg"

        # Save the image to the specified directory
        cv2.imwrite(file_path, image)
        currentFrame+=1


@app.post("/upload-images/")
async def upload_images(files: List[UploadFile] = File(...)):
    try:
        print(files)
        value = await store(files)
        return {"done":"done"}
        # return JSONResponse(content=value, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={"error":"Something Went wrong"}, status_code=400)
