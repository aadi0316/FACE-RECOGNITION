🛠️ Step 1: Create the file
In your VS Code, create a new file named README.md (if it's not already there) and paste the following content:

Markdown

# 📸 Face Recognition Attendance System

A real-time face recognition application built with **Python**, **OpenCV**, and **TensorFlow/Keras**. This system detects faces via webcam, recognizes individuals based on a trained CNN model, and logs attendance with timestamps.

## 🚀 Features
- **Real-time Detection:** Uses Haar Cascade Classifiers for fast and accurate face localization.
- **Deep Learning Recognition:** Powered by a Convolutional Neural Network (CNN) trained on custom datasets.
- **Automated Logging:** Saves attendance records to a `Attendance.csv` file automatically.
- **Visual Feedback:** Displays bounding boxes and recognition confidence percentages on-screen.

## 🏗️ Architecture
The system processes video frames through a specific pipeline to ensure compatibility with the trained model:
1. **Grayscale Conversion:** Reduces noise and matches the model's expected 1-channel input.
2. **Face ROI Extraction:** Crops the detected face area.
3. **Resizing:** Standardizes input to **96x96 pixels**.
4. **Normalization:** Scales pixel values to a `0-1` range for faster inference.



## 📋 Prerequisites
- Python 3.10+
- Webcam
- Virtual Environment (Recommended)

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/aadi0316/FACE-RECOGNITION.git](https://github.com/aadi0316/FACE-RECOGNITION.git)
   cd FACE-RECOGNITION
Create and activate a virtual environment:

Bash

python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
Install Dependencies:

Bash

pip install opencv-python numpy tensorflow
Prepare Data & Train (Optional):
If you want to add your own face:

Run prepare_data.py to capture images.

Run train_model.py to update fcm.h5.

🏃 Usage
Run the main recognition script:

Bash

python recognize_faces.py
Press 'q' to exit the camera view.

Check Attendance.csv for the logged entries.

🛠️ Tech Stack
OpenCV: Image processing and webcam integration.

TensorFlow/Keras: CNN model architecture and prediction.

NumPy: Numerical array manipulation.

Haar Cascades: Frontal face detection.

👤 Author
Name: Aditya Rana
Email: adityarana4010@gmail.com
LinkedIn: https://www.linkedin.com/in/aditya-rana-7490a7366/

Developed for educational purposes in Computer Vision and Deep Learning.


***

### 🛠️ Step 2: How to save it to GitHub
Once you have saved the file in VS Code, run these commands in your terminal to update your repository:

```powershell
git add README.md
git commit -m "Added a professional README"
git push origin main
