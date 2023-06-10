from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from datetime import datetime
from time import strftime



class chat_bot:
    def __init__(self,root):
        self.root=root
        self.root.geometry("600x600+0+0")
        self.root.title("Chatbot")
        self.root.bind('<Return>',self.enter_fun)

        main_frame = Frame(self.root, bd=3, bg="white", border=2, width=600)
        main_frame.pack()

        img2 = Image.open(r"imgs\chatbox.jpg")
        img2 = img2.resize((200, 70), Image.Resampling.LANCZOS)
        self.img2_ = ImageTk.PhotoImage(img2)

        bg_img = Label(main_frame,compound=LEFT,image=self.img2_,width=600,bd=3,anchor="nw",text="CHAT ME",font=("times new roman", 20 , "italic"),fg="blue")
        bg_img.pack(side=TOP)




        #=======datetime========
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(main_frame,font=("times new roman",20,"italic"),fg="green",cursor="hand2")
        lbl.place(x=400,y=40,width=200,height=50)  
        time()  



        #scroll bar
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame1 = Frame(self.root, bd=4,bg="white",width=600)
        btn_frame1.pack()

        self.entry=ttk.Entry(btn_frame1,width=30,font=('arial',17,'italic'))
        self.entry.grid(row=0,column=1,padx=5,sticky=W)

        self.send = Button(btn_frame1,text="Enter",fg="blue",width=10,command=self.send)
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        #icons
        # img3 = Image.open(r"imgs\\fb.png")
        # img3 = img3.resize((200, 70), Image.Resampling.LANCZOS)
        # self.img3_ = ImageTk.PhotoImage(img3)

        # bg_img1 = Label(btn_frame1,image=self.img3_,width=60,bd=3,anchor="nw")
        # bg_img1.grid(row=1,column=1)


        #empty message
        self.msg=''
        self.lbl1 =Label(btn_frame1, bg="white",text=self.msg, font=("times new roman", 15, "italic"),fg="red")
        self.lbl1.grid(row=0,column=0,sticky=W)



        # ====functions deceleardtion
    def enter_fun(self,event):
        self.send.invoke()
         



    def send(self):
        send = "You-"+ self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)
        if (self.entry.get())=="hello":
            self.text.insert(END,"\n"+"Bot- \n Hello! How can I help you today?") 
        elif (self.entry.get())=="hi":
            self.text.insert(END,"\n"+"Bot- Hello! How can I help you today?")       
        elif (self.entry.get())=="who are you":
            self.text.insert(END,"\n"+"Bot- Help Disk")  
        elif (self.entry.get())=="machine learning?":
            self.text.insert(END,"\n"+"Bot-\nMachine learning is the concept that a computer program can learn and adapt to new data without human interference. Machine learning is a field of artificial intelligence (AI) that keeps a computer’s built-in algorithms current regardless of changes in the worldwide economy.")
        elif (self.entry.get())=="face recognition?":
            self.text.insert(END,"\n"+"Bot-\nFace recognition is thus a form of person identification. Early face recognition systems relied on an early version of facial landmarks extracted from images, such as the relative position and size of the eyes, nose, cheekbone, and jaw.")   
        elif (self.entry.get())=="how does facial recognition work":
            self.text.insert(END,"\n"+"Bot-\nstep1:Fill student informations \n step2:take photo sample \n step3:Save data/information \n step4:Reconize your face for attendance")   
        elif self.entry.get()=="is face recognition secure?":
            self.text.insert(END,"\n" + "Bot-\nThe human face is endowed with several points, which are unique and noticeable even with the use of makeup, for example. Therefore, facial recognition has been considered as an option that meets high safety criteria. Facial recognition is now used on smartphones.")
        elif (self.entry.get()==''):
            self.msg='Enter input'
            self.lbl1.config(text=self.msg,fg='red') 
        else:
            self.msg=''
            self.lbl1.config(text=self.msg,fg='red')     

        self.entry.delete(0,END)

       
     










if __name__ == "__main__":
    root=Tk()
    obj = chat_bot(root)
    root.mainloop() 