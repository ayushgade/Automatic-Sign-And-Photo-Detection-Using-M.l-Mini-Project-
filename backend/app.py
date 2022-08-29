import numpy as np
import cv2
from tkinter import *
from tkinter import messagebox

# Load image and HSV color threshold
image = cv2.imread('image.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([90, 38, 0])
upper = np.array([145, 255, 255])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)
result[mask==0] = (255, 255, 255)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
sign = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=3,
                minSize=(30, 30)
)
signature = "{}".format(len(sign))
if signature=="0":
    print("[INFO] Signature Found in image!")
else:
    print("[INFO] Found No signature in image!")
    print("[INFO] Please upload the valid signature image!")
    
# Find contours on extracted mask, combine boxes, and extract ROI
cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = np.concatenate(cnts)
x,y,w,h = cv2.boundingRect(cnts)
cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
ROI = result[y:y+h, x:x+w]
status = cv2.imwrite('signature_detected.jpg', image)
if signature=="1":
    top =Tk()
    top.geometry("100x100")
    messagebox.showerror('Signature Image', 'Uploaded Signature Image is Incorrect')
    top.mainloop()
else:
    top =Tk()
    top.geometry("100x100")
    messagebox.showinfo('Signature Image', 'Uploaded Signsture Image is Correct')
    top.mainloop()

