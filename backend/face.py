import cv2
import sys
from tkinter import *
from tkinter import messagebox
from flask import Flask,request, render_template
from flask_cors import CORS , cross_origin


image = cv2.imread("image.jpg")
if image is None:
        print("Image is Empty")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30)
        )
    print("[INFO] Found {} Faces!".format(len(faces)))
    number_face = "{}".format(len(faces))
    print(number_face)
    for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    status = cv2.imwrite('faces_detected.jpg', image)
    if number_face=="1":
        print("Uploaded image is correct")
    else:
        print("Please upload the correct image")
    if number_face=="0":
        top =Tk()
        top.geometry("100x100")
        messagebox.showerror('Student Photo', 'Student Photo Uploaded is Incorrect')
        top.mainloop()
    else:
        top =Tk()
        top.geometry("100x100")
        messagebox.showinfo('Student Photo', 'Student Photo Uploaded is Correct')
        top.mainloop()