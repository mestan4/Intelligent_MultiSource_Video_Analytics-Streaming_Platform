# camera_logic.py

from ultralytics import YOLO
import cv2
import threading

model = YOLO("yolov8n.pt")

running = False
frame_lock = threading.Lock()
latest_frame = None

def detect():
    global running, latest_frame
    cap = cv2.VideoCapture(0)
    try:
        while running:
            ret, frame = cap.read()
            if not ret:
                continue
            results = model(frame)
            annotated = results[0].plot()
            with frame_lock:
                latest_frame = annotated
    finally:
        cap.release()

def start_camera():
    global running
    if not running:
        running = True
        threading.Thread(target=detect, daemon=True).start()

def stop_camera():
    global running
    running = False

def get_latest_frame():
    with frame_lock:
        return latest_frame.copy() if latest_frame is not None else None
