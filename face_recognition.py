from __future__ import print_function
import cv2
import argparse
from faces import *


def detectAndDisplay(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    # -- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        face = Face((x, y, w, h))
        center = face.getFaceCenter()
        # frame = cv2.ellipse(frame, center, (face.w // 2, face.h // 2), 0, 0, 360, (255, 0, 255), 4)
        # or draw clown stuff (cv2.addWeighted) ^
        faceROI = frame_gray[face.y:face.y + face.h, face.x:face.x + face.w]
        # -- In each face, detect eyes and nose
        eyes = eyes_cascade.detectMultiScale(faceROI)
        noses = noses_cascade.detectMultiScale(faceROI)
        if len(eyes) != 2:
            break
        for (x2, y2, w2, h2) in eyes:
            eye = Eye((x2, y2, w2, h2), face)
            face.addEyeObject(eye)
            eye_center = eye.getEyeCenter()
            radius = int(round((w2 + h2) * 0.25))
            # frame = cv2.circle(frame, eye_center, radius, (255, 0, 0), 4)
            # or draw clown stuff (cv2.addWeighted) ^
        """noses dataset not good; estimate nose based on closest"""
        # distance from middle of eyes to detected nose
        (min_center, min_dist) = ((0, 0), float('inf'))
        (min_center_w2, min_center_h2) = (0, 0)
        for (x2, y2, w2, h2) in noses:
            nose = Nose((x2, y2, w2, h2), face)  # nose detection implies face and eyes also found
            nose_center = nose.getNoseCenter()
            # get coordinates in middle of eyes
            x_between_eyes = (face.eyes[0].getEyeCenter()[0] + face.eyes[1].getEyeCenter()[0]) // 2
            # DEBUG: frame = cv2.circle(frame, (x_between_eyes, nose_center[1]), 3, (100, 100, 100), 4)
            dist_from_between_eyes = abs(x_between_eyes - nose_center[0]) / 2
            if dist_from_between_eyes < min_dist:
                (min_center, min_dist) = (nose_center, dist_from_between_eyes)
                (min_center_w2, min_center_h2) = (w2, h2)
                face.setNoseObject(nose)
        nose_radius = int((min_center_w2 + min_center_h2) * 0.25)
        frame = cv2.circle(frame, min_center, nose_radius, (0, 0, 255), -1)  # drawing filled red circle on nose
    cv2.imshow('Capture - Face detection', frame)


parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.',
                    default='haar_cascade_weights/haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.',
                    default='haar_cascade_weights/haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--nose_cascade', help='Path to nose cascade.',
                    default='haar_cascade_weights/haarcascade_mcs_nose.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
noses_cascade_name = args.nose_cascade
face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()
noses_cascade = cv2.CascadeClassifier()
# -- 1. Load the cascades
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
if not noses_cascade.load(cv2.samples.findFile(noses_cascade_name)):
    print('--(!)Error loading noses cascade')
    exit(0)
camera_device = args.camera
# -- 2a. Read the video stream
cap = cv2.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    if cv2.waitKey(10) == 27:
        break

# -- 2b. Read image
'''
while True:
    img = cv2.imread("images/DeNiro.jpg")
    detectAndDisplay(img)
    if cv2.waitKey(10) == 27:
        break
'''
