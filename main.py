from tkinter import*
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from datetime import date
from time import strftime
from student import student
from train import train_data
from face_recog import Face_Recognizer
from chatbot import chat_bot
from face_recog import Face_Recognizer
from attendance import attendance_
import os




class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

       
        self.root.config(bg="white")

        #root.overrideredirect()

        title_bar=Frame(self.root,bg="#48483D",relief="raised",bd=0)
        title_bar.pack(expand=1,fill=X)

        title_label=Label(title_bar,text="Face Recognition Attendance system",bg="#A9A9A9")
        title_label.pack(side=LEFT,pady=2)

        img = Image.open(r"imgs\\depositphotos_270570388-stock-illustration-low-poly-male-human-face.jpg")
        img=img.resize((1530,220),Image.Resampling.LANCZOS)
        self.img_=ImageTk.PhotoImage(img)

        f_lbl =Label(self.root,image=self.img_)
        f_lbl.place(x=0,y=0,width=1530,height=220)

        #bg img

        img1 = Image.open(r"imgs\\pexels-hasan-albari-1229861.jpg")
        img1=img1.resize((1530,570),Image.Resampling.LANCZOS)
        self.img1_=ImageTk.PhotoImage(img1)

        bg_img =Label(self.root,image=self.img1_)
        bg_img.place(x=0,y=220,width=1530,height=570)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20,"italic"),bg="black",fg="green",cursor="hand2",justify=CENTER)
        title_lbl.place(x=-100,y=0,width=1530,height=45)
        

          #dateTime 
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman",20,"italic"),bg="black",fg="green",cursor="hand2")
        lbl.place(x=68,y=0,width=200,height=50)  
        time() 

        def datet():
            today = date.today()
            lbl1.config(text=today)
        lbl1=Label(title_lbl,font=("times new roman",20,"italic"),bg="black",fg="green",cursor="hand2")
        lbl1.place(x=1280,y=0,width=200,height=50)
        datet() 

            

         

        #Student button
        img2 = Image.open(r"imgs\\st.jpg")
        img2=img2.resize((190,150),Image.Resampling.LANCZOS)
        self.img2_=ImageTk.PhotoImage(img2)

        b1=Button(bg_img,image=self.img2_,cursor="hand2",command=self.student_detials)
        b1.place(x=150,y=50,width=190,height=150)
        
        b1_tx=Button(bg_img,text="Student Detial",cursor="hand2",bg="white",relief=SUNKEN,fg="blue",font=("times new roman",15,"italic"),command=self.student_detials)
        b1_tx.place(x=150,y=200,width=190,height=20)

        #Face detection
        img3 = Image.open(r"imgs\\face_dt.jpg")
        img3=img3.resize((200,160),Image.Resampling.LANCZOS)
        self.img3_=ImageTk.PhotoImage(img3)

        b2=Button(bg_img,image=self.img3_,cursor="hand2",command=self.face_data)
        b2.place(x=420,y=50,width=200,height=160)
        b2_txt=Button(bg_img,text ="Face Detection",bg="white",relief=SUNKEN,fg="blue",font=("times new roman",15,"italic"),command=self.face_data)
        b2_txt.place(x=420,y=200,width=200,height=20)
        
        #Attendance 
        img4 = Image.open(r"imgs\\attendance.jpg")
        img4=img4.resize((200,160),Image.Resampling.LANCZOS)
        self.img4_=ImageTk.PhotoImage(img4)

        b4=Button(bg_img,image=self.img4_,cursor="hand2",command=self.atten)
        b4.place(x=670,y=50,width=200,height=160)
        b4_txt=Button(bg_img,text ="Attendance",bg="white",relief=SUNKEN,fg="blue",font=("times new roman",15,"italic"),command=self.atten)
        b4_txt.place(x=670,y=200,width=200,height=20)

        #help
        img5 = Image.open(r"imgs\\messagebox.ico")
        img5=img5.resize((200,160),Image.Resampling.LANCZOS)
        self.img5_=ImageTk.PhotoImage(img5)

        b5=Button(bg_img,image=self.img5_,cursor="hand2",command=self.help_disk)
        b5.place(x=920,y=50,width=200,height=160)
        b5_txt=Button(bg_img,text ="Help",bg="white",relief=SUNKEN,fg="blue",font=("times new roman",15,"italic"),command=self.help_disk)
        b5_txt.place(x=920,y=200,width=200,height=20)
        
        #train data
        img6 = Image.open(r"imgs\\train.jpg")
        img6=img6.resize((200,160),Image.Resampling.LANCZOS)
        self.img6_=ImageTk.PhotoImage(img6)

        b6=Button(bg_img,image=self.img6_,cursor="hand2",command=self.train)
        b6.place(x=150,y=250,width=200,height=160)

        b6_txt=Button(bg_img,text ="Train",bg="white",relief=SUNKEN,fg="blue",font=("times new roman",15,"italic"),command=self.train)
        b6_txt.place(x=150,y=390,width=200,height=20)

         #gallery
        img7 = Image.open(r"imgs\\photo.jpg")
        img7=img7.resize((200,160),Image.Resampling.LANCZOS)
        self.img7_=ImageTk.PhotoImage(img7)

        b7=Button(bg_img,image=self.img7_,cursor="hand2",command=self.photo_access)
        b7.place(x=420,y=250,width=200,height=160)

        b7_txt=Button(bg_img,text ="Gallery",bg="white",relief=SUNKEN,fg="blue",font=("times new roman",15,"italic"),command=self.photo_access)
        b7_txt.place(x=420,y=390,width=200,height=20)
        # #team
        # img8 = Image.open(r"imgs\\team.jpg")
        # img8=img8.resize((200,160),Image.Resampling.LANCZOS)
        # self.img8_=ImageTk.PhotoImage(img8)

        # b7=Button(bg_img,image=self.img8_,cursor="hand2")
        # b7.place(x=670,y=250,width=200,height=160)

        # b7_txt=Button(bg_img,text ="Devlopers",bg="white",relief=SUNKEN,fg="blue",font=("times new roman",15,"italic"))
        # b7_txt.place(x=670,y=390,width=200,height=20)

        #Exit
        img9 = Image.open(r"imgs\\exit.jpg")
        img9=img9.resize((200,160),Image.Resampling.LANCZOS)
        self.img9_=ImageTk.PhotoImage(img9)

        b9=Button(bg_img,image=self.img9_,cursor="hand2",command=self.exit_b)
        b9.place(x=670,y=250,width=200,height=160)

        b7_txt=Button(bg_img,text ="Exit",bg="white",relief=SUNKEN,fg="blue",font=("times new roman",15,"italic"),command=self.exit_b)
        b7_txt.place(x=670,y=390,width=200,height=20)




        #Access img dir
    def photo_access(self): 
            os.startfile("data")

    
    

    # def att_data(self):
    #     os.startfile("attendance.csv")

    # #======Access attendance==========  


    #======Exit funtion======
    def exit_b(self):
        self.lyou=messagebox.askyesno("Face Recogination Attendance System","Are you sure for exit?",parent=self.root)
        if self.lyou>0:
            self.root.destroy()
        else:
            return    


        #=============Functions for Buttons========

    def student_detials(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=train_data(self.new_window)  

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognizer(self.new_window)  

    def help_disk(self):
        self.new_window=Toplevel(self.root)
        self.app=chat_bot(self.new_window)  

    def atten(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance_(self.new_window)           

          
      













if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()    