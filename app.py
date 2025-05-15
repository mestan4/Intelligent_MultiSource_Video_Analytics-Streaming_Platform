# app.py

from flask import Flask, jsonify, Response, render_template
from camera_logic import start_camera, stop_camera
from streamer import generate_mjpeg

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Web arayüzü

@app.route('/start', methods=['POST'])
def start():
    start_camera()
    return jsonify({"status": "Camera started"})

@app.route('/stop', methods=['POST'])
def stop():
    stop_camera()
    return jsonify({"status": "Camera stopped"})

@app.route('/stream')
def stream():
    return Response(generate_mjpeg(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
