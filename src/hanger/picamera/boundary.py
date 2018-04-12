import numpy as np
import cv2

from picamera.array import PiRGBArray
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (480,320)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size = (480,320))


for frame in camera.capture_continuous(rawCapture, format = 'bgr', use_video_port = True):
    image = frame.array
    cv2.imshow('Frame', image)
    key = cv2.waitKey(0)
    rawCapture.truncate(0)
    cv2.imwrite('Frame.jpg', image)
    if (key == 27) :
        break
    
def contour():
    img = cv2.imread('Frame.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(img, contours, -1, (0,0,255),1)
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
contour()
