from picamera import PiCamera
from time import sleep
from gpiozero import Button

import os

button = Button(21)

with PiCamera() as camera :
    #camera.rotation = 180
    camera.start_preview(fullscreen=False, window=(100,20,640,480))
    button.wait_for_press()
    camera.capture('1.jpg')
    camera.stop_preview()
    
os.system("python remove_background.py")
os.system("python show_label.py 1.jpg")

