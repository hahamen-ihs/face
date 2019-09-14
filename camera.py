import cv2
import urllib
import pdb
import numpy as np
import face_recognition
import argparse
import imutils
import pickle
import time


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder

        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')


def __del__(self):
    self.video.release()


def get_frame(self):
    while True:
    # pdb.set_trace()
        success, img = self.video.read(1024)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            ret, jpeg = cv2.imencode('.jpg', img)
            return jpeg.tobytes()



encodings = face_recognition.face_encodings(rgb, boxes)
names = []

# loop di semua wajah yang terdeteksi

for encoding in encodings:
    matches = face_recognition.compare_faces(data["encodings"],
			encoding)
    name = "Unknown"

# check apakah ada wajah yang di kenali
if True in matches:
    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
    counts = {}
for i in matchedIdxs:
    name = data["names"][i]
    counts[name] = counts.get(name, 0) + 1
    name = max(counts, key=counts.get)
    names.append(name)

# loop di semua wajah yang sudah di kenali
for ((top, right, bottom, left), name) in zip(boxes, names):
# tampilkan nama di wajah yang di kenali
    cv2.rectangle(img, (left, top), (right, bottom),(0, 255, 0), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv2.putText(img, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)