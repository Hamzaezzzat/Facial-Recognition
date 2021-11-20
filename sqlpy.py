#!/usr/bin/python
import cv2
import sqlite3
import numpy as np
import sqlite3

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

def displayDatabase():
	conn= sqlite3.connect('FaceBase.db')
	cmd="SELECT * FROM Student "
	cursor=conn.execute(cmd)
	print "ID\t\tNAME\t\t\tMAIL"
	for row in cursor:
   		   print row[0],"\t",row[1],"\t\t",row[3]
   		   print "  "
	conn.commit()
	conn.close()

