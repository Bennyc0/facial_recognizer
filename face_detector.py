import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
# eyeCascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
 
while(True):
    ret, img = cap.read()
    # frame = cv2.flip(frame, -1) # Flip camera vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
       
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        # # Uncomment this section if adding an eye detector
        
        # eyes = eyeCascade.detectMultiScale(
        #     roi_gray,
        #     scaleFactor= 1.5,
        #     minNeighbors=10,
        #     minSize=(5, 5),
        # )
       
        
        # for (ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        
    
    cv2.imshow('frame', img)
    cv2.imshow('gray', gray)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27 or k == ord('q'): # press 'ESC' or 'Q' to quit
        break

cap.release()
cv2.destroyAllWindows()