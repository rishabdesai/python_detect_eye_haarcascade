import cv2

# Load the cascade

face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
#face_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
#face_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')

# Read the input image
img = cv2.imread('assets/test_image.jpg')

# Convert RGB into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
# three arguments - grey scale image, scale factor, minimum neighbours
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # (255,0,0) is color of rectangle, and 2 is thk of it.

# Display the output
cv2.imshow('img', img)
cv2.waitKey()
