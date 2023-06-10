from tkinter import*
import tkinter as ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector


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
        labl1=Label(frame1,text="First Name",font=("times new roman",15,),bg='white',borderwidth=0,relief=GROOVE)
        labl1.place(x=40,y=100)
        entry1=ttk.Entry(frame1,bg='white',textvariable=self.var_fname)
        entry1.place(x=40,y=125,width=200)

        labl2=Label(frame1,text="Last Name",font=("times new roman",15,),bg='white',borderwidth=0)
        labl2.place(x=300,y=100)
        entry2=ttk.Entry(frame1,bg='white',textvariable=self.var_lname)
        entry2.place(x=300,y=125,width=200)
        
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

        male=ttk.Checkbutton(frame1,text='male',bg='white',onvalue=1,offvalue=1)
        male.place(x=40,y=330)

        
        female=ttk.Checkbutton(frame1,text='female',bg='white',onvalue=0,offvalue=0)
        female.place(x=100,y=330)


        # condition=ttk.Checkbutton(frame1,text='I aggree term and conditions',bg='white',onvalue=1,offvalue=0,textvariable=self.var_aggree)
        # condition.place(x=200,y=330)



        b1=Button(frame1,text="Clear",font=("times new roman",15,),fg='black',bg='lightblue',activebackground='lightblue',cursor='hand2',activeforeground='black',borderwidth=0,relief=GROOVE)
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

           








if __name__ == "__main__":
    root=Tk()
    obj = register_(root)
    root.mainloop()                  