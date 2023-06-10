from tkinter import *
import tkinter as ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import os
from time import strftime
from student import student
from train import train_data
from datetime import date
from chatbot import chat_bot
from attendance import attendance_
from face_recog import Face_Recognizer




def main():
    win =Tk()
    app=login_sys(win)
    win.mainloop()


class login_sys:
    def __init__(self,root):
        self.root=root
        self.root.geometry("700x600+0+0")
        self.root.title("Login System")  

     

        #bg image

        img = Image.open(r"imgs\\login_bg.jpg")
        img=img.resize((700,600),Image.Resampling.LANCZOS)
        self.img_=ImageTk.PhotoImage(img)

        f_lbl =Label(self.root,image=self.img_)
        f_lbl.place(x=0,y=0,width=700,height=600)


        #datetime
        # def time():
        #     string=strftime('%H:%M:%S %p')
        #     lbl.config(text=string)
        #     lbl.after(1000,time)
        # lbl=Label(f_lbl,font=("times new roman",15,"italic"),fg="green",cursor="hand2",bg='lightblue',borderwidth=0)
        # lbl.place(x=5,y=0)  
        # time()


        #login frame
        frame1= Frame(self.root,bg='black')
        frame1.place(x=155,y=50,width=340,height=450)

        img1 = Image.open(r"imgs\\red.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.img1_=ImageTk.PhotoImage(img1)

        f_lbl1 =Label(frame1,image=self.img1_,bg="black",borderwidth=0)
        f_lbl1.place(x=120,y=0,width=100,height=100)

        labl=Label(frame1,text="Get Started",font=("times new roman",17,"bold"),bg='black',fg='white',borderwidth=0)
        labl.place(x=100,y=100)  

        #labels
        labl=Label(frame1,text="Username",font=("times new roman",15),bg='black',fg='white',borderwidth=0)
        labl.place(x=80,y=155)

        self.text_area=ttk.Entry(frame1,font=("times new roman",13,"italic"),background='white',relief=SUNKEN,borderwidth=0)
        self.text_area.place(x=60,y=180)

        labl1=Label(frame1,text="Password",font=("times new roman",15),bg='black',fg='white')
        labl1.place(x=80,y=220)

        self.text_area1=ttk.Entry(frame1,font=("times new roman",13,"italic"),background='white',borderwidth=0,relief=SUNKEN)
        self.text_area1.place(x=60,y=248)

        img2 = Image.open(r"imgs\\user.png")
        img2=img2.resize((20,20),Image.Resampling.LANCZOS)
        self.img2_=ImageTk.PhotoImage(img2)

        f_lbl2 =Label(frame1,image=self.img2_,bg="black",borderwidth=0)
        f_lbl2.place(x=58,y=155)

        img3 = Image.open(r"imgs\\password.png")
        img3=img3.resize((20,20),Image.Resampling.LANCZOS)
        self.img3_=ImageTk.PhotoImage(img3)

        f_lbl3 =Label(frame1,image=self.img3_,bg="black",borderwidth=0)
        f_lbl3.place(x=58,y=220)    
            

        #lognbtn
        self.loginbutton=Button(frame1,text="Login",command=self.values,activebackground="red",font=('times new roman',15,),bg='red',borderwidth=0,cursor='hand2')
        self.loginbutton.place(x=100,y=300,width=100,height=30)
        
        # #forgetpass
        # registerbutton=Button(frame1,text="Forget password",command=self.forget,activeforeground='white',activebackground='black',font=('times new roman',8,),bg='black',fg='white',borderwidth=0,cursor='hand2')
        # registerbutton.place(x=105,y=330)

        #register
        registerbutton=Button(frame1,text="New User Register",activebackground="black",command=self.register_data,font=('times new roman',8,),bg='black',fg='white',activeforeground='white',borderwidth=0,cursor='hand2')
        registerbutton.place(x=105,y=330)

        labl2=Label(frame1,text="@anurag Baitha",font=("times new roman",8),fg='limegreen',bg='black',borderwidth=0)
        labl2.place(x=260,y=430)
    #register data
    def register_data(self):
        self.new_window=Toplevel(self.root)
        self.app=register_(self.new_window)   
    
        

        

    #validations
    def values(self):

        if self.text_area.get()=='' or self.text_area1.get()=='':
            messagebox.showerror('Error','All filds are required')

        # elif self.text_area.get()=='pushpa'  or self.text_area1.get()=='anurag':
        #     messagebox.showinfo('Success','Welcome to my life')        

        else:
            try:
                conn = mysql.connector.connect( host="localhost", user="root", password="", database="student")
                my_cursor = conn.cursor()
                my_cursor.execute('select * from register where email= %s and pass=%s',(
                                                                self.text_area.get(),
                                                                self.text_area1.get()
                )) 
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Username & password')
                else:
                    open_main=messagebox.askyesno('Choice','are you sure?')
                    if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_system(self.new_window)
                    else:
                        if not open_main:
                            return    
                conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror('Error',f'Due to:{str}')    
    #=======rest pass=========
    # def for_pass(self):  
    #     if self.e.get()=='':
    #         messagebox.showerror('Error','Plese enter your Contact No')
    #     else:
    #        conn = mysql.connector.connect( host="localhost", user="root", password="", database="student")
    #        my_cursor = conn.cursor()
    #        quar=('select * from register where email=%s and contactNo=%s')
    #        value=(self.e.get(),)  
    #        my_cursor.execute(quar,value)
    #        row=my_cursor.fetchone()
    #        if row==None:
    #         messagebox.showerror('Error','Chack your ContactNo')
    #        else:
    #         quar=('update register set pass_word=%s where email=%s')
    #         value=(self.e.get())
    #         my_cursor.execute(quar,value)

    #         conn.commit()
    #         conn.close()
    #         messagebox.showinfo('Info','Your password has been reset')




              
    # #=======forget function==========
    def forget(self):
        if self.text_area.get()=='':
            messagebox.showerror('Error','Plese Enter your email for reset password')
        else:
             conn = mysql.connector.connect( host="localhost", user="root", password="", database="student")
             my_cursor = conn.cursor()  
             quary=('select * from register where email=%s')
             value=(self.text_area.get(),)
             my_cursor.execute(quary,value)
             row=my_cursor.fetchone()
            #  print (row) 

             if row==None:
                messagebox.showerror('Error','Enter Valid user name')
             else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title('Forget Password')
                self.root2.geometry('300x260+610+170') 

                labl0=Label(self.root2,text="Enter your Number",font=("times new roman",15),bg='white',fg='darkgreen',borderwidth=0)
                labl0.place(x=0,y=40,width=300)

                self.e=Entry(self.root2,font=("times new roman",15),bg='white',borderwidth=0)
                self.e.place(x=50,y=70)

                self.loginbutton=Button(self.root2,text="Reset",activebackground="red",font=('times new roman',15,),bg='red',borderwidth=0,cursor='hand2',command=self.for_pass)
                self.loginbutton.place(x=100,y=100,width=100,height=30)




                





          





class register_:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("__register") 

        # ===========text variables========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        
          

        img = Image.open(r"imgs\\register.jpg")
        img=img.resize((1530,790),Image.Resampling.LANCZOS)
        self.img_=ImageTk.PhotoImage(img)

        f_lbl =Label(self.root,image=self.img_)
        f_lbl.place(x=0,y=0,width=1530,height=790)

        
        #datetime
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(f_lbl,font=("times new roman",15,"italic"),fg="green",cursor="hand2",bg='white',borderwidth=0)
        lbl.place(x=5,y=0)  
        time()

        #second bg
        img1 = Image.open(r"imgs\\coffee.jpg")
        img1=img1.resize((470,550),Image.Resampling.LANCZOS)
        self.img1_=ImageTk.PhotoImage(img1)

        f_lbl1 =Label(self.root,image=self.img1_)
        f_lbl1.place(x=50,y=100,width=470,height=550)


        #mainframe
        frame1=Frame(self.root,bg='white')
        frame1.place(x=520,y=100,width=600,height=550)

        #regi
        labl=Label(frame1,text="REGISTER FORM",font=("times new roman",20,'italic'),bg='white',borderwidth=0,fg='darkgreen')
        labl.place(x=2,y=5)

        #name
        labl1=Label(frame1,text="First Name",font=("times new roman",15,),bg='white',borderwidth=0)
        labl1.place(x=50,y=100)
        entry1=ttk.Entry(frame1,bg='white',textvariable=self.var_fname)
        entry1.place(x=40,y=125,width=200)

        labl2=Label(frame1,text="Last Name",font=("times new roman",15,),bg='white',borderwidth=0)
        labl2.place(x=300,y=100)
        entry2=ttk.Entry(frame1,bg='white',textvariable=self.var_lname)
        entry2.place(x=290,y=125,width=200)
        
        #contact
        labl1=Label(frame1,text="Contact No",font=("times new roman",15,),bg='white',borderwidth=0)
        labl1.place(x=40,y=170)
        entry1=ttk.Entry(frame1,bg='white',textvariable=self.var_contact)
        entry1.place(x=40,y=190,width=200)

        #emailName
        labl2=Label(frame1,text="Email ",font=("times new roman",15,),bg='white',borderwidth=0)
        labl2.place(x=300,y=170)
        entry2=ttk.Entry(frame1,bg='white',textvariable=self.var_email)
        entry2.place(x=300,y=190,width=200)

        #password
        labl2=Label(frame1,text="Password ",font=("times new roman",15,),bg='white',borderwidth=0)
        labl2.place(x=40,y=240)
        entry2=ttk.Entry(frame1,bg='white',textvariable=self.var_pass)
        entry2.place(x=40,y=270,width=200)

        #conform pass
        labl2=Label(frame1,text="Confirm Password",font=("times new roman",15,),bg='white',borderwidth=0)
        labl2.place(x=300,y=240)
        entry2=ttk.Entry(frame1,bg='white',textvariable=self.var_confpass)
        entry2.place(x=300,y=270,width=200)

        #gender
        labl9=Label(frame1,text="Select Gender",font=("times new roman",15,),bg='white',borderwidth=0)
        labl9.place(x=40,y=310)

        male=ttk.Checkbutton(frame1,text='male',bg='white',onvalue=1,offvalue=0)
        male.place(x=40,y=330)

        
        female=ttk.Checkbutton(frame1,text='female',bg='white',onvalue=1,offvalue=0)
        female.place(x=100,y=330)




        b1=Button(frame1,text="Clear",font=("times new roman",15,),fg='black',bg='lightblue',activebackground='lightblue',cursor='hand2',activeforeground='black',borderwidth=0)
        b1.place(x=300,y=380,width=150)
        b2=Button(frame1,text="Submit",font=("times new roman",15,),command=self.validation,fg='black',bg='lightblue',activebackground='lightblue',cursor='hand2',activeforeground='black',borderwidth=0)
        b2.place(x=100,y=380,width=150)

       

        labl2=Label(frame1,text="@anurag Baitha",font=("times new roman",9),fg='limegreen',borderwidth=0)
        labl2.place(x=517,y=530)

    #===========function declear============
    def validation(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="":
            messagebox.showerror('Error','Fill up all fileds')
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror('Error','Password & confirm password must be same')   
        else:
            conn = mysql.connector.connect( host="localhost", user="root", password="", database="student")
            my_cursor = conn.cursor()
            quary=('select * from register where email=%s')
            value=(self.var_email.get(),)
            my_cursor.execute(quary,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror('Error','User already exist,try another email')
            else:
                my_cursor.execute('insert into register values(%s,%s,%s,%s,%s,%s)',(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_pass.get(),
                    self.var_confpass.get()


                ))  
            conn.commit()
            conn.close()
            messagebox.showinfo('Success','Register Successfully')   



class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

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
        
        # #train data
        # img6 = Image.open(r"imgs\\train.jpg")
        # img6=img6.resize((200,160),Image.Resampling.LANCZOS)
        # self.img6_=ImageTk.PhotoImage(img6)

        # b6=Button(bg_img,image=self.img6_,cursor="hand2",command=self.train)
        # b6.place(x=150,y=250,width=200,height=160)

        # b6_txt=Button(bg_img,text ="Train",bg="white",relief=SUNKEN,fg="blue",font=("times new roman",15,"italic"),command=self.train)
        # b6_txt.place(x=150,y=390,width=200,height=20)

         #gallery
        img7 = Image.open(r"imgs\\photo.jpg")
        img7=img7.resize((200,160),Image.Resampling.LANCZOS)
        self.img7_=ImageTk.PhotoImage(img7)

        b7=Button(bg_img,image=self.img7_,cursor="hand2",command=self.photo_access)
        b7.place(x=150,y=250,width=200,height=160)

        b7_txt=Button(bg_img,text ="Gallery",bg="white",relief=SUNKEN,fg="blue",font=("times new roman",15,"italic"),command=self.photo_access)
        b7_txt.place(x=150,y=390,width=200,height=20)
       
        #Exit
        img9 = Image.open(r"imgs\\exit.jpg")
        img9=img9.resize((200,160),Image.Resampling.LANCZOS)
        self.img9_=ImageTk.PhotoImage(img9)

        b9=Button(bg_img,image=self.img9_,cursor="hand2",command=self.exit_b)
        b9.place(x=420,y=250,width=200,height=160)

        b7_txt=Button(bg_img,text ="Exit",bg="white",relief=SUNKEN,fg="blue",font=("times new roman",15,"italic"),command=self.exit_b)
        b7_txt.place(x=420,y=390,width=200,height=20)


    #Access img dir
    def photo_access(self): 
        os.startfile("data")

    
    

    #======Access attendance==========  


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
   main()        