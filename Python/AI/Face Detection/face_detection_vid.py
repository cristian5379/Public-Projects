from turtle import clear
import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

webcam = cv2.VideoCapture(0)
######################### 0 -> default webcam
######################### "name.mp4" -> video

while True:
    successful_frame_read, frame = webcam.read()

    grayscale_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

    for face in face_coordinates:
        (x,y,w,h)  = face
        cv2.rectangle(frame, (x,y), (x+w, y+h) , (randrange(256) , randrange(256) , randrange(256) ), 10 )
        ################## top ### buttom ######## B ############## G ############### R ########## thickness

    cv2.imshow('', frame)

    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

webcam.release()

print("code")    
    
