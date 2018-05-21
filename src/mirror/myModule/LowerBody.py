import cv2

def findBody():
    #camera number /dev/video0
    cap = cv2.VideoCapture(0) #return 0 or -1

    #save video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('sample_video/LowerBody##.avi', fourcc, 20.0, (640,480))

    while cap.isOpened():
        ret, img = cap.read()
        findRects = []
        if cv2.waitKey(1)&0xFF == ord('q'):
            break
        if not ret:
            print('no camera connected!')
        else:
            path = "haarcascade_lowerbody.xml"
            imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            lowerCascade = cv2.CascadeClassifier(path)
            lowerRect = lowerCascade.detectMultiScale(imageGray, scaleFactor=3.1, minNeighbors=1, minSize=(1,1)) 
            
            #return the finded object list
            if len(lowerRect) > 0:
                findRects.append(lowerRect[0])
                print(findRects)

            try:
                for obj in findRects:
                    print(obj)
                    #img= cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2) 
                    img = cv2.rectangle(img, (obj[0],obj[1]), (obj[0]+obj[2], obj[1]+obj[3]), (0, 255, 0), 2)
                    #frame = cv2.flip(img, 180)
                    #out.write(frame)
            except ValueError as e:
                print("ERROR: " + str(e))

            cv2.imshow('camera-0', img)
    cap.release()
    cv2.destroyAllWindows()

findBody()
