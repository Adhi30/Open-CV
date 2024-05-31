# -*- coding: utf-8 -*-
"""Webcam Using OpenCv.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_TjDZ7DQs6DZkORi_18LJe1nkIYvWaC5

**To Read WebCam**
"""

import cv2

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    if not success:
        break

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()