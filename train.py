from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import numpy as np
import os
import cv2

class train_data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train dataset")

        title_lbl = Label(text="Train Dataset", font=("times new roman", 15, "italic"),bg="black", fg="green", cursor="hand2", relief=SUNKEN, justify=CENTER)
        title_lbl.place(x=-100, y=0, width=1530, height=45)

        #font img
        img = Image.open( r"imgs\\data.jpg")
        img = img.resize((1530, 300), Image.Resampling.LANCZOS)
        self.img_ = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.img_)
        f_lbl.place(x=0, y=44, width=1530, height=300)

       #button 

        b7_txt=Button(self.root,text ="Train data",bg="black",relief=SUNKEN,fg="blue",font=("times new roman",17,"italic"),highlightbackground="red",activebackground="gray",command=self.train_classifier,cursor="hand2")
        b7_txt.place(x=-100,y=340,width=1530,height=60)

         #down image
        img1 = Image.open( r"imgs\\cc.jpg")
        img1 = img1.resize((1530, 300), Image.Resampling.LANCZOS)
        self.img1_ = ImageTk.PhotoImage(img1)

        f_lbl2 = Label(self.root, image=self.img1_)
        f_lbl2.place(x=0, y=400, width=1530, height=300)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image 
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[-1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13 
        ids=np.array(ids)


        #=====================classifier training===========   
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("anurag.yml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")








if __name__ == "__main__":
    root=Tk()
    obj = train_data(root)
    root.mainloop() 