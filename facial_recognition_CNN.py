import math
import numpy as np
from facenet_pytorch import MTCNN
import cv2
import utils

# This implementation is slower, but more accurate compared to facial_recognition_haar.py
# It uses pre-trained CNN's rather than haar cascades

# Create face detector
def draw_nose(img_path):
    mtcnn = MTCNN(keep_all=True)
    img = cv2.imread(img_path)
    rev = img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect face
    _, _, landmarks = mtcnn.detect(img, landmarks=True)

    # Draw nose
    if landmarks is not None:
        found = False
        for landmark in landmarks:
            left_eye = np.int_(landmark[0, 0]), np.int_(landmark[0, 1]) # left eye
            right_eye = np.int_(landmark[1, 0]), np.int_(landmark[1, 1]) # right eye
            mouth_left = np.int_(landmark[3, 0]), np.int_(landmark[3, 1]) # left of mouth
            mouth_right = np.int_(landmark[4, 0]), np.int_(landmark[4, 1]) # right of mouth
            nose_x = int(landmark[2:3, 0])  # Nose x is located at landmark[2:3, 0]
            nose_y = int(landmark[2:3, 1])  # Nose y is located at landmark[2:3, 0]
            features_width = utils.dist(left_eye, right_eye)
            nose_size = int(features_width / 3)  # Approximate nose radius
            cv2.circle(rev, (nose_x, nose_y), nose_size, (0, 0, 255), thickness=-1)
            found = True
        cv2.imwrite('images/recent_out.jpg', rev)
        return found
    else:
        return False
