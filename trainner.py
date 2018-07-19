import os
import cv2
import numpy as np
from PIL import Image

recognizer=cv2.createLBPHFaceRecognizer();
path='dataSet';

def getImageWithID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg,'uint8') #faceImg contains imag and uint8 type
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        
        print ID
        faces.append(faceNp)
        IDs.append(ID)
        
        cv2.imshow("training",faceNp) #training heading of the window
        cv2.waitKey(10);
        
    IDs=np.array(IDs)
    return IDs, faces

IDs,faces = getImageWithID(path)
recognizer.train(faces,IDs)
recognizer.save('recognizer/trainningData.yml')
cv2.destroyAllWindows()
