import cv2
import numpy as np
import tensorflow as tf

# Load everything
model = tf.keras.models.load_model("fcm.h5")
with open("class_names.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

print("--- Starting Recognition ---")
while True:
    ret, frame = cap.read()
    if not ret: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # Blue box for detection

        # Preprocessing (Match your training!)
        roi = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi, (96, 96)) # Use the size your model expects
        roi = roi.astype("float32") / 255.0
        blob = np.reshape(roi, (1, 96, 96, 1))

        # Prediction
        preds = model.predict(blob, verbose=0)
        confidence = np.max(preds)
        index = np.argmax(preds)
        name = class_names[index]

        # Log to terminal so we can see the logic
        print(f"Seeing: {name} | Confidence: {confidence:.2f}")

        # Display on screen
        label = f"{name} ({int(confidence*100)}%)"
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.imshow("Testing Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
