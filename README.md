# Intelligent Multi-Source Video Analytics & Streaming Platform

This project is a real-time, AI-powered video analytics system that:

- Aggregates webcam streams
- Applies person detection using YOLOv8
- Streams annotated video via Flask (MJPEG)
- Provides a REST API to start/stop analysis
- Includes a web interface for control

---

## 🔧 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/mestan4/Intelligent_MultiSource_Video_Analytics-Streaming_Platform.git
cd Intelligent_MultiSource_Video_Analytics-Streaming_Platform

2.Install dependencies:
pip install -r requirements.txt
# or manually:
pip install opencv-python flask ultralytics

3.Run The Application
python3 app.py

4.open in browser
http://127.0.0.1:5000
