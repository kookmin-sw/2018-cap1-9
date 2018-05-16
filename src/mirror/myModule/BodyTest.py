import cv2

def detectLowerBody(image):
    cascadePath = "/usr/local/share/OpenCV/haarcascades/haarcascade_lowerbody.xml"
    result = image.copy()
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascadePath)
    #Detects objects of different size in the input image. The detected objects are returned as a list of rectangles.
    #scaleFactor - Parameter specifying how much the image size is reduced at each image scale.
    Rect = cascade.detectMultiScale(imageGray, scaleFactor=1.1, minNeighbors=1, minSize=(1,1)) 
    if len(Rect) <= 0:
	return False	
    else:
	return Rect

def detectUpperBody(image):
    cascadePath = "/usr/local/share/OpenCV/haarcascades/haarcascade_upperbody.xml"
    result = image.copy()
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascadePath)
    #Detects objects of different size in the input image. The detected objects are returned as a list of rectangles.
    #scaleFactor - Parameter specifying how much the image size is reduced at each image scale.
    Rect = cascade.detectMultiScale(imageGray, scaleFactor=1.1, minNeighbors=1, minSize=(1,1)) 
    if len(Rect) <= 0:
	return False	
    else:
	return Rect



#MIAN

#camera number /dev/video0
cap = cv2.VideoCapture(0) #return 0 or -1

#save video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.mkv', fourcc, 20.0, (640,480))

while cap.isOpened():
    ret, img = cap.read()
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    findRects = []
    if cv2.waitKey(1)&0xFF == ord('q'):
	break
    if not ret:
	print('no camerea connected!')
    else: 
        #return the finded object list
	upperBody = detectUpperBody(img)
	lowerBody = detectLowerBody(img)
	if upperBody is False:
	    continue
	else:
	    findRects.append(detectUpperBody(img))
	if lowerBody is False:
	    continue
	else:	
	    findRects.append(detectLowerBody(img))
	#cannot find any object
        if findRects is False:
	    print("False")
	    cv2.imshow('camera-0', img)
            continue
        for (x,y,w,h) in findRects:
        #rect(x, y, w, h)
            img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2) 
        cv2.imshow('camera-0', img)
cap.release()
#out.release()
cv2.destroyAllWindows()
