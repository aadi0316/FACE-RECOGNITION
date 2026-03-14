import cv2
import os

# --- 1. Define Folders ---
input_folder = 'myface'
output_folder = 'ProcessedImages'

# --- 2. Create Base Output Folder if it Doesn't Exist ---
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created base directory: {output_folder}")

# Load OpenCV face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# --- 3. Process Each Student's Folder ---
for student_name in os.listdir(input_folder):

    student_input_path = os.path.join(input_folder, student_name)
    student_output_path = os.path.join(output_folder, student_name)

    if os.path.isdir(student_input_path):

        os.makedirs(student_output_path, exist_ok=True)

        for filename in os.listdir(student_input_path):

            image_path = os.path.join(student_input_path, filename)

            image = cv2.imread(image_path)

            if image is None:
                print(f"Warning: Could not read {image_path}")
                continue

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5
            )

            if len(faces) > 0:

                x, y, w, h = faces[0]
                face_image = image[y:y+h, x:x+w]

                output_path = os.path.join(student_output_path, filename)
                cv2.imwrite(output_path, face_image)

                print(f"Processed {filename} for {student_name}")

            else:
                print(f"No face found in {filename}")

print("\nData preparation complete.")