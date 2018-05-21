import cv2
import json
import pickle
import logging
import numpy

logging.basicConfig(filename='test.log', format='%(message)s', level=logging.DEBUG)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return super(MyEncoder, self).default(obj)

def findBody():
    cap = cv2.VideoCapture(0) #return 0 or -1

    upper_path = '/home/wink/Documents/2018-cap1-9/src/mirror/myModule/haarcascade_upperbody.xml'
    lower_path = '/home/wink/Documents/2018-cap1-9/src/mirror/myModule/haarcascade_lowerbody.xml'
    upperCascade = cv2.CascadeClassifier(upper_path)
    lowerCascade = cv2.CascadeClassifier(lower_path)

    while cap.isOpened():
        ret, img = cap.read()
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
                    upperRect = lowerCascade.detectMultiScale(imageGray, scaleFactor=1.3, minNeighbors=1, minSize=(1,1))
                    temp.append({'x':x,'y':y,'w':w,'h':h})
                    for lx,ly,lw,lh in upperRect:
                        print("upper: %d, %d, %d, %d"%(lx,ly,lw,lh))
                        cv2.rectangle(img, (lx,ly), (lx+lw,ly+lh), (0,0,255),2) #red box
                        temp2.append({'x':lx,'y':ly,'w':lw,'h':lh})
                out['lower'] = temp
                out['upper'] = temp2
                print(out)
                logging.info(json.dumps(out, cls=MyEncoder))

                with open('out.txt', 'wb') as file:
                     file.write(pickle.dumps(out))
            except ValueError as e:
                print("ERROR: " + str(e))

            cv2.imshow('camera-0', img)
    cap.release()
    cv2.destroyAllWindows()

findBody()


