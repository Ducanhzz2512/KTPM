import os
import cv2

# ====== ĐƯỜNG DẪN LƯU DATASET ======
DATA_DIR = r'C:\Users\Admin\Desktop\KTPMProject\sign_data\dataset'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# ====== CẤU HÌNH DATASET ======
number_of_classes = 21     
dataset_size = 200        

# ====== CAMERA ======
cap = cv2.VideoCapture(0)  

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Collecting data for class {j}')

    # ====== ĐỢI BẮT ĐẦU ======
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.putText(
            frame,
            f'Class {j} - Press Q to start',
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )
        cv2.imshow('frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # ====== THU ẢNH ======
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.imshow('frame', frame)
        cv2.waitKey(25)

        img_path = os.path.join(class_dir, f'{counter}.jpg')
        cv2.imwrite(img_path, frame)

        counter += 1

    print(f'Finished class {j}')

cap.release()
cv2.destroyAllWindows()
