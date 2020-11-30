import cv2
import imutils
import numpy as np


def nothing(*arg):
    pass


cv2.namedWindow("result")  # making main window
cv2.namedWindow("settings")  # making settings window

# создаем 6 бегунков для настройки начального и конечного цвета фильтра
# 6 inputs for colors range
cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
crange = [0, 0, 0, 0, 0, 0]

vs = cv2.VideoCapture("EXAMPLE_IMAGE")
# Getting image
img = vs.read()[1]

while True:
    frame = imutils.resize(img, width=640, height=360)
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    # Get values from inputs
    h1 = cv2.getTrackbarPos('h1', 'settings')
    s1 = cv2.getTrackbarPos('s1', 'settings')
    v1 = cv2.getTrackbarPos('v1', 'settings')
    h2 = cv2.getTrackbarPos('h2', 'settings')
    s2 = cv2.getTrackbarPos('s2', 'settings')
    v2 = cv2.getTrackbarPos('v2', 'settings')

    # creating colors
    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)

    # Apply filter on image
    thresh = cv2.inRange(hsv, h_min, h_max)

    # Display image
    cv2.imshow('result', thresh)

    ch = cv2.waitKey(5)
    if ch == 27:
        break
cv2.destroyAllWindows()
