#!/usr/bin/python
import cv2
import sqlite3
import numpy as np


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

def dataset():

	def insertOrUpdate (Id,name,mail):
		conn = sqlite3.connect("FaceBase.db")
		sql = ''' INSERT INTO Student (ID,Name,Mail) VALUES(?,?,?) '''
		task = (Id,name,mail)
		conn.execute(sql, task)
		conn.commit()
		conn.close()

	id = input("Enter user id : ")
	name = input("Enter user Name : ")
	mail = str(id) + "@std.neu.com"
	insertOrUpdate(id, name,mail)
	def datasetface(num):
	       while True:
			   ret,img= cam.read(0)
			   gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
			   faces= face_cascade.detectMultiScale(gray,1.3,5)
			   for (x,y,w,h) in faces:
				   num = num+  1
				   cv2.imwrite("dataset/" + str(name)+" . "+str(id)+"."+str(num)+".jpg",gray[y:y+h,x:x+w])
				   cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),10)
				   cv2.waitKey(100)
			   cv2.imshow("Face",img)
			   if (num>40) or (cv2.waitKey(1) == ord('q')) :
				   break
	datasetface(0)
	cam.release()
	cv2.destroyAllWindows()
	'''
	def dataset():

		def insertOrUpdate (Id,Name):
			conn = sqlite3.connect("FaceBase.db")
			cmd= "INSERT INTO Student (ID,Name) Values(" + str(Id) + "," + str(Name) + ")"
			conn.execute(cmd)
			conn.commit()
			conn.close()

		id = input("Enter user id : ")
		name = input("Enter user Name : ")
		insertOrUpdate(id,name)
		def datasetface(num):
	           while True:
				   ret,img= cam.read(0)
				   gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
				   faces= face_cascade.detectMultiScale(gray,1.3,5)
				   for (x,y,w,h) in faces:
					   num = num+  1
					   cv2.imwrite("dataset/" + str(name)+" . "+str(id)+"."+str(num)+".jpg",gray[y:y+h,x:x+w])
					   cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),10)
					   cv2.waitKey(100)
				   cv2.imshow("Face",img)
				   if (num>40) or (cv2.waitKey(1) == ord('q')) :
					   break
	   	   datasetface(0)
		   cam.release()
		   cv2.destroyAllWindows()
	'''
	#id = input("Enter user id : ")
	#name = input("Enter user Name : ")
