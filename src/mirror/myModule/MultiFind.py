import cv2


def findBody():
    cap = cv2.VideoCapture(0) #return 0 or -1

    """
    #save video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('sample_video/sample.avi', fourcc, 20.0, (640,480))
    """

    upper_path = '/home/wink/Documents/2018-cap1-9/src/mirror/myModule/haarcascade_upperbody.xml'
    lower_path = '/home/wink/Documents/2018-cap1-9/src/mirror/myModule/haarcascade_lowerbody.xml'
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
            lowerRect = lowerCascade.detectMultiScale(imageGray, scaleFactor=1.3, minNeighbors=1, minSize=(1,1)) 
            try:
                for x,y,w,h in lowerRect:
                    print("lower: %d, %d, %d, %d"%(x,y,w,h))
                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2) 
                    upperRect = lowerCascade.detectMultiScale(imageGray, scaleFactor=1.3, minNeighbors=1, minSize=(1,1)) 
                    for lx,ly,lw,lh in upperRect:
                        print("upper: %d, %d, %d, %d"%(lx,ly,lw,lh))
                        cv2.rectangle(img, (lx,ly), (lx+lw,ly+lh), (0,255,0),2) 
            except ValueError as e:
                print("ERROR: " + str(e))

            #frame = cv2.flip(img, 180)
            #out.write(frame)
            cv2.imshow('camera-0', img)

    cap.release()
    #out.release()
    cv2.destroyAllWindows()
