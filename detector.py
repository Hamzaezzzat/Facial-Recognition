import os
import cv2
import numpy as np
from PIL import Image
import pickle
import sqlite3

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()

rec.read("recognizer/trainningData.yml")

def getProfile(id):
       conn = sqlite3.connect("FaceBase.db")
       cmd = "SELECT * FROM Student WHERE ID = "+str(id)
       cursor = conn.execute(cmd)
       profile = None
       for row in cursor:
              profile = row
       conn.close()
       return profile

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
              ret,img= cam.read(0)
              gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
              faces= face_cascade.detectMultiScale(gray,1.3,5)
              for (x,y,w,h) in faces:
                     cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),10)
                     id,conf = rec.predict(gray[y:y+h,x:x+w])
                     profile = getProfile(id)
                     if (profile != None):
                            cv2.putText(img,str(profile[1]),(x,y+h+40), font, 1.5,(200,60,50),2,cv2.LINE_AA)
                            cv2.putText(img,str(profile[0]),(x,y+h+80), font, 1.5,(200,60,50),2,cv2.LINE_AA)
                            cv2.putText(img,"Student",(x,y+h+120), font, 1.5,(200,60,50),2,cv2.LINE_AA)
                            cv2.putText(img,'Press "Q" To Exit',(20,450), font, .5,(0,0,0),1,cv2.LINE_AA)

                            #cv2.putText(img,str(profile[4]),(x,y+h+160), font, 1.5,(200,60,50),2,cv2.LINE_AA)
              cv2.imshow("Face",img)
              if(cv2.waitKey(1) == ord('q')):
                     break
cam.release()
cv2.destroyAllWindows()
