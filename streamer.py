# streamer.py

from flask import Response
from camera_logic import get_latest_frame
import cv2

def generate_mjpeg():
    while True:
        frame = get_latest_frame()
        if frame is None:
            continue
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n')
