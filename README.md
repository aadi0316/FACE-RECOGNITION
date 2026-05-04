**Face Recognition Attendance System**

**Face Recognition Attendance System** is an innovative application designed to automate attendance logging in real-time. By leveraging cutting-edge technologies like AI, deep learning, and computer vision, this app provides accurate face recognition, automated attendance marking, and real-time visual feedback.

##Features

1. **Real-Time Face Detection**

-Detects faces using Haar Cascade Classifiers for fast and accurate face localization.
-Provides instant visual feedback with bounding boxes and confidence percentages.


2. **Deep Learning Recognition**

-Uses a Convolutional Neural Network (CNN) trained on custom datasets to identify individuals.
-Matches detected faces against authorized users listed in class_names.txt.


3. **Automated Attendance Logging**

-Saves attendance records with User ID and precise Entry Time to Attendance.csv automatically.


4. **Preprocessing Pipeline**

-Converts frames to grayscale and resizes them to 96x96 pixels for model compatibility.
-Normalizes pixel values to a 0-1 range for faster and more accurate inference.


5. **Custom Dataset Support**

-Allows users to capture their own face images and retrain the model using prepare_data.py and train_model.py.

---


##Tech Stack

- **Language**: Python
- **Computer Vision**: OpenCV, Haar Cascade Classifier
- **Deep Learning**: TensorFlow, Keras (Sequential CNN)
- **Numerical Computing**: NumPy

---

##Installation

##Prerequisites
-Python 3.10 or later
-pip package manager
-Webcam
-Virtual environment (optional but recommended)

##Steps

1.Clone this repository:

```bash
git clone https://github.com/yourusername/FACE-RECOGNITION.git
cd FACE-RECOGNITION
```

2.Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3.Install dependencies:

```bash
pip install opencv-python numpy tensorflow
```

(Optional) Capture your own face dataset:

```bash
python prepare_data.py
```

(Optional) Train the model on your dataset:

```bash
python train_model.py
```

4.Run the recognition system:

```bash
python recognize_faces.py
```

---

##Usage

1.Ensure your webcam is connected and working.
2.Run the main recognition script.
3.Stand in front of the webcam — the system will detect and recognize your face.
4.Attendance is automatically logged with your name and timestamp.
5.Press q to exit the camera view.
6.Open Attendance.csv to review the logged entries.

---

##Roadmap

-Add support for multiple face recognition in a single frame.
-Integrate a web dashboard to view attendance records.
-Implement email or SMS notifications on attendance marking.
-Develop a mobile version for on-the-go attendance tracking.

---

##Contribution

Contributions are welcome! Please follow these steps:

1.Fork this repository.
2.Create a feature branch:

```bash
git checkout -b feature-name
```

3.Commit changes and push to your fork:

```bash
 git commit -m "Add feature-name"
 git push origin feature-name
```

4.Open a pull request on the main repository.

---

##Acknowledgments

-**OpenCV** for enabling robust real-time computer vision and face detection.
-**TensorFlow and Keras** for providing powerful deep learning tools.
-**Haar Cascade Classifiers** for fast and reliable frontal face detection.
-The open-source community for inspiring innovation in AI and computer vision.

---

##Contact
For questions or suggestions, feel free to contact:

**Name**: Aditya Rana

**Email**: adityarana4010@gmail.com

**LinkedIn**: [Aditya Rana](https://www.linkedin.com/in/aditya-rana-7490a7366/)

Happy Recognizing! 📸
