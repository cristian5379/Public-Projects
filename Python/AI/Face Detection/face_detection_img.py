from turtle import clear
import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread('people.jpg')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscale_img)
 
# print(face_coordinates)

for face in face_coordinates:
    (x,y,w,h) = face

    cv2.rectangle(img, (x,y), (x+w, y+h) , (randrange(256) , randrange(256) , randrange(256) ), 10 )
    ################## top ### buttom ######## B ############## G ############### R ########## thickness

cv2.imshow('',img)
cv2.waitKey()

# cv2.imshow('',grayscale_img)
# cv2.waitKey()
