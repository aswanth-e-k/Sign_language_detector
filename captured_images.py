import os 
import cv2 # type: ignore
import time
import uuid

IMAGE_PATH = "CollectedImages"  # Corrected variable name

labels = ["hello", "thanks", "yes", "no", "iloveyou"]
number_imgs = 10

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)  # Added exist_ok=True to avoid errors if the directory already exists
    cap = cv2.VideoCapture(0)
    print("Collecting images for {}".format(label))
    time.sleep(5)
    for i in range(number_imgs):
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image. Skipping...")
            continue
        img_name = os.path.join(img_path, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(img_name, frame)
        cv2.imshow("Capturing images", frame)
        time.sleep(2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
cv2.destroyAllWindows()  # Ensure all OpenCV windows are closed