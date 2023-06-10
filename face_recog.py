from tkinter import *
import numpy as np
import os
import cv2
from datetime import datetime
import face_recognition


class Face_Recognizer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("30x10+0+0")
       

        path = 'data'
        images = []
        classNames = []
        myList = os.listdir(path)
        print(myList)
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        print(classNames)

        def findEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList


        def markAttendance(name):
            with open('anurag.csv','r+') as f:
                myDataList = f.readlines()
                nameList = []
                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    d1=now.strftime('%d/%m/%Y')
                    dtsting=now.strftime('%H:%M:%S')
                    f.writelines(f'\n{name},{d1},{dtsting},present')
        

        encodeListKnown = findEncodings(images)
        print('Encoding Complete')
        
        cap = cv2.VideoCapture(0)
 
        while True:
            success, img = cap.read()
            #img = captureScreen()
            imgS = cv2.resize(img,(0,0),None,0.25,0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
        
            for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
                #print(faceDis)
                matchIndex = np.argmin(faceDis)
        
                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    #print(name)
                    y1,x2,y2,x1 = faceLoc
                    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                else:
                    y1,x2,y2,x1 = faceLoc
                    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(img,"unknown",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

                    markAttendance(name)
                    
    
            cv2.imshow('Webcam',img)
            if cv2.waitKey(10)==13:
                break
                
    


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognizer(root)
    root.mainloop()
