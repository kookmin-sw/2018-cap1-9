import cv2
import json
import logging
import numpy as np

logging.basicConfig(filename='test.log', format='%(message)s', level=logging.DEBUG)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(MyEncoder, self).default(obj)


def rotateImage(image, angle):
    (h,w) = image.shape[:2]
    (cX, cY) = (w//2, h//2)

    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0,0])
    sin = np.abs(M[0,1])

    nW = int((h*sin) + (w * cos))
    nH = int((h * cos) + (w* sin))

    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    return cv2.warpAffine(image, M, (nW, nH))


def findBody():
    cap = cv2.VideoCapture(0) #return 0 or -1
    #(center, angle, scale)


    upper_path = 'myModule/haarcascade_upperbody.xml'
    lower_path = 'myModule/haarcascade_lowerbody.xml'
    upperCascade = cv2.CascadeClassifier(upper_path)
    lowerCascade = cv2.CascadeClassifier(lower_path)

    while cap.isOpened():
        ret, img = cap.read()

        img = rotateImage(img, 90)
        #flip the image vertically
        img = cv2.flip(img, 1)

        out = {}

        if cv2.waitKey(1)&0xFF == ord('q'):
            break
        if not ret:
            print('no camera connected!')

        else:
            imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            try:
                lowerRect = lowerCascade.detectMultiScale(imageGray, scaleFactor=1.3, minNeighbors=1, minSize=(1,1))
                temp = []
                temp2 = []
                for x,y,w,h in lowerRect:
                    print("lower: %d, %d, %d, %d"%(x,y,w,h))
                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2) #green box 
                    upperRect = upperCascade.detectMultiScale(imageGray, scaleFactor=1.3, minNeighbors=1, minSize=(1,1))
                    temp.append({'h':h,'w':w,'y':y,'x':x})
                    for lx,ly,lw,lh in upperRect:
                        print("upper: %d, %d, %d, %d"%(lx,ly,lw,lh))
                        cv2.rectangle(img, (lx,ly), (lx+lw,ly+lh), (255,0,0),2) #red box
                        temp2.append({'h':lh,'w':lw,'y':ly,'x':lx})
                out['lower'] = temp
                out['upper'] = temp2
                print(out['lower'])
                print(out['upper'])
                logging.info(json.dumps(out, cls=MyEncoder))

            except ValueError as e:
                print("ERROR: " + str(e))

            cv2.imshow('camera-0', img)
    cap.release()
    cv2.destroyAllWindows()
