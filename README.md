# facerecognitionfun

This project is a Python-based application that can detect and recognize faces from images and webcam video streams. It uses the face_recognition library, which is a popular open-source library that provides simple and easy-to-use API for face recognition.

How it works

The project uses the face_recognition library to perform face detection and recognition. It first loads known face encodings from a folder and then compares them to unknown face encodings. The comparison is done using a distance metric, and if the distance between the unknown face encoding and known face encoding is less than a threshold, the two faces are considered a match.

In the case of face detection, the project uses the OpenCV library to detect faces in an image or video stream. Once a face is detected, the face_recognition library is used to encode the face and compare it to known face encodings.

Credits

The face_recognition library is developed and maintained by Adam Geitgey. More information about the library can be found at: https://github.com/ageitgey/face_recognition.

License

This project is licensed under the MIT License - see the LICENSE file for details.
