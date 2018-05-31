import numpy as np
import cv2
import argparse
import base64
import os

from picamera.array import PiRGBArray
from picamera import PiCamera

#camera = PiCamera()
#camera.resolution = (480,320)
#camera.framerate = 32
#rawCapture = PiRGBArray(camera, size = (480,320))

def main(photo_file) :
    contour(photo_file)
    colorfilter(photo_file)
    os.system("aws s3 cp %s s3://clothes-image" %photo_file)
    return 0

def contour(photo_file):
    img = cv2.imread(photo_file)
 
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

    
    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def colorfilter(photo_file):
    img = cv2.imread(photo_file)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_black = np.array([0,0,0])
    upper_black = np.array([80,80,80])

    mask = cv2.inRange(hsv, lower_black, upper_black)
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img, img, mask= ~mask)
    cv2.imwrite(photo_file, res)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help = 'The image you\'d like to remove background.')
    args = parser.parse_args()
    parser = argparse.ArgumentParser()
                    
    main(args.image_file)
