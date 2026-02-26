# YOLO-Object-Detection-with-Streamlit-Frontend-Excel-Logging
# 🚀 YOLO Object Detection with Streamlit & Excel Export

## 📌 Project Overview

This project is a real-time Object Detection system built using YOLO (You Only Look Once) with a Streamlit web frontend.
It allows users to upload images, videos, or use a webcam for detection while automatically counting detected objects and exporting the results to an Excel (.xlsx) file.

The system uses pretrained YOLO models (COCO dataset) and supports custom class fine-tuning for domain-specific applications.

---

## 🧠 Key Features

* 🎯 Real-time object detection (YOLOv8/YOLOv5)
* 🖥️ Interactive Streamlit frontend UI
* 📷 Image, Video, and Webcam support
* 📊 Automatic object counting per class
* 📁 Excel (.xlsx) export of detection results
* 🧩 Support for custom trained classes
* ⚡ Fast and lightweight inference pipeline
* 📥 Downloadable Excel report from UI

---

## 🛠️ Tech Stack

* Python
* YOLO (Ultralytics)
* Streamlit
* OpenCV
* PyTorch
* Pandas
* OpenPyXL

---

## ⚙️ Installation

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install ultralytics opencv-python torch pandas openpyxl streamlit
```

---

## ▶️ Running the Application

### 🔹 Run Streamlit Frontend (Recommended)

```bash
streamlit run app.py
```

Then open the URL shown in terminal:

```
http://localhost:8501
```

---

## 🖥️ Streamlit App Features

* Upload image for detection
* Upload video for processing
* Live webcam detection
* Real-time bounding box visualization
* Dynamic object count display
* One-click Excel report download

---

## 📊 Excel Output (Detection Count Logging)

After detection, the system automatically generates an Excel file containing:

* Object Class Name
* Detection Count
* Timestamp
* Input Source

### Example Output:

| Class  | Count |
| ------ | ----- |
| person | 6     |
| car    | 3     |
| dog    | 1     |

📁 Saved at:

```
outputs/detection_counts.xlsx
```

---

## 🧪 Custom Dataset Training (Optional)

To detect custom objects not in COCO classes:

```bash
python train.py --data data.yaml --epochs 50 --weights yolov8n.pt
```

### Recommended Dataset Size:

* Minimum: 100 images per class
* Optimal: 300–500 images per class (with augmentation)

---

## 🛠️ How It Works

1. User uploads image/video or uses webcam via Streamlit UI
2. YOLO model performs object detection
3. Detected classes are counted in real-time
4. Counts are stored in a dictionary
5. Data is converted into a Pandas DataFrame
6. Excel file (.xlsx) is generated using OpenPyXL
7. User can download the Excel report directly from the UI

---

## 🌍 Use Cases

* Smart Surveillance Systems
* Retail Analytics (People Counting)
* Traffic Monitoring
* Industrial Inspection
* Robotics Vision
* AI Research Projects
* Computer Vision Dashboards

---

## 📈 Future Enhancements

* Object tracking (DeepSORT / ByteTrack)
* Live analytics charts in Streamlit
* Database logging (SQL/Firebase)
* Docker deployment
* Cloud deployment (AWS/GCP)
* REST API integration

---

## 📜 License

This project is licensed under the MIT License.

---

## 🏷️ GitHub Topics (Recommended)

```
yolo
streamlit
object-detection
computer-vision
deep-learning
yolov8
opencv
excel-export
object-counting
ai-dashboard
machine-learning
real-time-detection
```

---

## ⭐ Acknowledgements

* Ultralytics YOLO
* Streamlit
* OpenCV Community

