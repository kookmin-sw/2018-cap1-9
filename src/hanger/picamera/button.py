from picamera.array import PiRGBArray
from picamera import PiCamera
from gpiozero import Button

import os
import glob
import cv2
import time

button = Button(21)

with PiCamera() as camera :
    #camera.rotation = 180
    for i in range(50):
        camera.start_preview(fullscreen=False, window=(100,20,640,480))
        button.wait_for_press()
        camera.capture('Frame.png')
        os.rename("Frame.png", str(i) + ".png")
        camera.stop_preview()
        os.system("python remove_background.py %s.png" %(i))
        print('complete remove_background')
        os.system("python show_label.py %s.png" %(i))
        print('complete show_label')
        key = cv2.waitKey()
    

