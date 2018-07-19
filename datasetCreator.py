import cv2
import sqlite3
import numpy as np

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

def insertOrUpdate(Id,Name,Age,Gender):
    #connect to the database
    conn=sqlite3.connect("FaceBase.db")
    # SELECT ID FROM people, etc
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor = conn.execute(cmd) # cursor return row by row data
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
        
    if(isRecordExist==1):
        cmd="UPDATE People SET Name="+str(Name)+" ,SET Age="+Age+" ,SET Gender="+str(Gender)+" WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO People(ID,Name,Age,Gender) Values("+Id+","+str(Name)+","+Age+","+str(Gender)+")"

    conn.execute(cmd)
    conn.commit() #commit changes
    conn.close() # close the connection


id=raw_input('Enter User ID ')
Name=raw_input('Enter Your Name ')
Age=raw_input('Enter Your Age ')
Gender=raw_input('Enter Gender ')
insertOrUpdate(id,Name,Age,Gender)
sampleNumber=0;
cam=cv2.VideoCapture(0);
while(True):
    ret,image=cam.read();
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY);
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNumber=sampleNumber+1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNumber)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100);
    cv2.imshow("Face",image);
    cv2.waitKey(1);
    if(sampleNumber>20):
        break;
    
cam.release();
cv2.destroyAllWindows();
