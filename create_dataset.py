import cv2
import os
import time

# --- 1. SET UP YOUR PARAMETERS ---
# The name of the person you are collecting data for
person_name = input("Enter the name of the person: ").upper()

# The main folder to save all datasets
DATA_DIR = 'ImagesAttendance'

# Path to the specific person's folder
person_path = os.path.join(DATA_DIR, person_name)

# Create the folder if it doesn't exist
if not os.path.exists(person_path):
    os.makedirs(person_path)
    print(f"Created directory: {person_path}")

# --- 2. INITIALIZE WEBCAM ---
cap = cv2.VideoCapture(0)
print("\nWebcam started. Press 's' to start collecting images.")
print("Once started, move your head slowly in different angles and lighting.")
print("Press 'q' at any time to quit.")

# --- 3. MAIN LOOP ---
image_count = 0
collecting = False

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image from webcam.")
        break

    # Display instructions on the screen
    if collecting:
        # Display a green "RECORDING" status
        cv2.putText(img, f"RECORDING... Count: {image_count}", (30, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Save the image
        image_name = f'{person_name}_{int(time.time())}_{image_count}.jpg'
        cv2.imwrite(os.path.join(person_path, image_name), img)
        image_count += 1
        
    else:
        # Display a red "PAUSED" status
        cv2.putText(img, "PAUSED - Press 's' to start", (30, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Image Collector', img)
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        collecting = not collecting # Toggle collecting state
        if collecting:
            print("Starting image collection...")
        else:
            print("Paused image collection.")

    if key == ord('q'):
        print(f"\nQuitting. Collected {image_count} images for {person_name}.")
        break

cap.release()
cv2.destroyAllWindows()