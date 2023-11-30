from typing import Union

from fastapi import FastAPI


# import cv2
import base64

app = FastAPI()
# Initialize the webcam
# cap = cv2.VideoCapture(0)

def capture_image():

    # Capture a frame from the webcam
    # ret, frame = cap.read()

    # Convert the image to base64
    # _, img_encoded = cv2.imencode('.jpg', frame)
    # img_base64 = base64.b64encode(img_encoded.tobytes()).decode('utf-8')

    return img_base64


# def capture():
#     try:
#         # Capture an image from the webcam
#         image_base64 = capture_image()

#         return jsonify({'image': image_base64})

#     except Exception as e:
#         return jsonify({'error': str(e)})



@app.get("/")
def read_root():
    return {"Hello": "World"}
    # return capture()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
