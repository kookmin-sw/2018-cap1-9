import cv2
import requests

url = 'http://34.225.233.100/VT_WEB/show_smart_mirror_screen.php'
data = None 
#camera number /dev/video0
cap = cv2.VideoCapture(0) #return 0 or -1

#save video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('sample_video/LowerBody##.avi', fourcc, 20.0, (640,480))

upper_path = 'haarcascade_upperbody.xml'
lower_path = 'haarcascade_lowerbody.xml'
upperCascade = cv2.CascadeClassifier(upper_path)
lowerCascade = cv2.CascadeClassifier(lower_path)

while cap.isOpened():
    ret, img = cap.read()
    findRects = []
    
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    if not ret:
        print('no camera connected!')
    else:
        imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        lowerRect = lowerCascade.detectMultiScale(imageGray, scaleFactor=3.1, minNeighbors=1, minSize=(1,1)) 
    
        #return the finded object list
        if len(lowerRect) > 0:
            findRects.append(lowerRect[0])
            print(findRects)

        try:
            for x,y,w,h in findRects:
                print("%d, %d, %d, %d"%(x,y,w,h))
                #img= cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2) 
                upperRect = lowerCascade.detectMultiScale(imageGray, scaleFactor=3.1, minNeighbors=1, minSize=(1,1)) 
                try:
                    for lx,ly,lw,lh in upperRect:
                        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2) 
                except ValueError as ee:
                    print("ERROR: " + str(e))
        except ValueError as e:
            print("ERROR: " + str(e))

        #frame = cv2.flip(img, 180)
        #out.write(frame)
        cv2.imshow('camera-0', img)

cap.release()
#out.release()
cv2.destroyAllWindows()
