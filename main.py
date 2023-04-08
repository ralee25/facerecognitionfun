import cv2
from simple_facerec import SimpleFacerec
import face_recognition


# encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/") # path where all the images are

cap = cv2.VideoCapture(0) #load camera (0) loads the 1st camera 




while True:
    ret, frame = cap.read()

    # detect faces 
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_TRIPLEX, 3, (75, 0, 130), 3)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (75, 0, 130), 6)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


#
# this stuff is for comparing the equalness of two faces (not live)
#

#img = cv2.imread("taehyung1.jpeg") #reads in taehyung1.jpeg

#now we must encode face in order to compare to other faces...
#rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #converts img to grayscale
#img_encoding = face_recognition.face_encodings(rgb_img)[0]


#img2 = cv2.imread("images/taehyung.jpeg") #reads in park seo joon

#now we must encode face in order to compare to other faces...
#rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) #converts img to grayscale
#img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

#result = face_recognition.compare_faces([img_encoding], img_encoding2)
#print("Result: ", result)

#cv2.imshow("Img", img) #shows taehyung in frame called "Img"
#cv2.imshow("Img 2", img2) #shows taehyung in frame called "Img"
#cv2.waitKey(0)





