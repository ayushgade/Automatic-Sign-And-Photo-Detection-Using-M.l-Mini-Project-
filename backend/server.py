
# from crypt import methods
import py_compile
from flask import Flask,request, render_template
from numpy import number
from werkzeug.utils import secure_filename
from flask_cors import CORS , cross_origin
import urllib.request
import js2py
from tkinter import *
from tkinter import messagebox
from PIL import Image
import cv2
# from face import number_face


# Initializing flask app
# UPLOAD_FOLDER = "..face"
app = Flask(__name__) # Creates an app object from flask
CORS(app)
# app.config['UPLOAD_PATH'] = UPLOAD_FOLDER

@app.route('/upload')
def upload_file():
   	return render_template('index.html')

# Route for seeing a data
@app.route('/photo', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Content-Type'])

def upload():
	if request.method == 'POST':
		f = request.files['studentimage']
		f.save("image.jpg")
		return"Succsfully uploaded the Image"
		# if number_face>1:
		# 	return ' correct'
		# else:
		# 	return 'upload the once again'
	
	return '',200 

@app.route('/photo', methods=['POST','GET'])
@cross_origin(origin='*',headers=['Content-Type'])

def upload_sign():
	if request.method == 'POST':
		f = request.files['studentsign']
		f.save("sign.jpg")
		return"Succsfully uploaded the sign"
		# if number_face>1:
		# 	return ' correct'
		# else:
		# 	return 'upload the once again'
	
# 	return '',200 
# def send():
# 	if request.method == 'POST':
# 		if number_face == 1:
# 		 	return 'file Uploaded correct'
	
# Running app
if __name__ == '__main__':
	app.run(debug=True)
