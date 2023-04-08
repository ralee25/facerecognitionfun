import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#img = cv2.imread('rachel.jpg')

cap = cv2.VideoCapture(0) #captures video from webcam

while True:
    _, img = cap.read() #returns flag(whether frame was read correctly or not) and the frame itself (img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        
    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27: #if esc key is pressed, loop stops
        break
cap.release()