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
        for landmark in landmarks:
            pt1 = np.int_(landmark[0, 0]), np.int_(landmark[0, 1])
            pt2 = np.int_(landmark[1, 0]), np.int_(landmark[1, 1])
            pt3 = np.int_(landmark[3, 0]), np.int_(landmark[3, 1])
            pt4 = np.int_(landmark[4, 0]), np.int_(landmark[4, 1])
            features_width = utils.dist(pt1, pt2)
            features_height = utils.dist(pt2, pt3)
            nose_size = int(features_width / 3)  # Approximate nose size
            # Nose is located at landmark[2:3, 0], landmark[2:3, 1]
            cv2.circle(rev, (int(landmark[2:3, 0]), int(landmark[2:3, 1])),
                       nose_size, (0, 0, 255), thickness=-1)
            # DEBUG: cv2.rectangle(frame, pt1, pt4, (0, 0, 255), thickness=1)
            cv2.imwrite('images/recent_out.jpg', rev)
            return True
    else:
        return False
