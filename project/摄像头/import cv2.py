import cv2
facedetect =cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cam = cv2.VideoCapture(0)
cv2.namedWindow('came',cv2.WINDOW_GUI_NORMAL)
cv2.resizeWindow('came',800,600)
while(1):
    flag,img = cam.read()
    faces =facedetect.detectMultiScale(img)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('fac',img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()