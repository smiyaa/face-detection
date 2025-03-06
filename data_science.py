import cv2
import numpy as np

video=cv2.VideoCapture(0)

face_detect=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

face_data=[]
i=0


# capturing frames
while True:
    ret,frame=video.read()
    if not ret:
        break

    # frame to grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # detect faces
    faces=face_detect.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5,minSize=(50,50))

    # processing
    for(x,y,w,h) in faces:
        crop_img=frame[y:y+h,x:x+w]
        resized_img=cv2.resize(crop_img,(50,50))
    
        if len(face_data)<100:
            face_data.append(resized_img)   
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
    cv2.putText(frame,f"Faces:{len(faces)}",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
    

    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()