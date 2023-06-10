from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from time import strftime
import os
import csv
from tkinter import filedialog

mydata=[]
class attendance_:
    def __init__(self,root):
        self.root=root
        self.root.geometry("650x450+0+0")
        self.root.title("attendance_") 

        # ==============variables===============
        self.var_name = StringVar()
        self.var_datetime = StringVar()
        self.var_status = StringVar()
        self.var_time = StringVar()
       
        

        img = Image.open(r"imgs\\depositphotos_270570388-stock-illustration-low-poly-male-human-face.jpg")
        img=img.resize((650,220),Image.Resampling.LANCZOS)
        self.img_=ImageTk.PhotoImage(img)

        f_lbl =Label(self.root,image=self.img_)
        f_lbl.place(x=0,y=0,width=650,height=220)

        img2 = Image.open(r"imgs\bg.jpg")
        img2 = img2.resize((650, 570), Image.Resampling.LANCZOS)
        self.img2_ = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.img2_)
        bg_img.place(x=0, y=155, width=650, height=570)

        title_lbl = Label(bg_img,text="Attendance Managemet System", font=("times new roman", 15, "italic"),bg="black", fg="green", cursor="hand2", justify=CENTER)
        title_lbl.place(x=-50, y=0, width=650, height=45)

        #datetime
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(450,time)
        lbl=Label(title_lbl,font=("times new roman",15,"italic"),bg="black",fg="green",cursor="hand2")
        lbl.place(x=68,y=0,width=200,height=50)  
        time()  

        main_frame = Frame(bg_img, bd=3, bg="white", border=2)
        main_frame.place(x=0, y=0, width=1450, height=650)

        # left side frame
        left_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE,text="Student Detial", font=("times new roman", 15, "italic"))
        left_frame.place(x=5, y=5, width=315, height=280)


        name_label = Label(left_frame, text="Name", font=("times new roman", 13, "italic"), bg="white")
        name_label.grid(row=0, column=0, padx=5, sticky=W)
        studentid_entry = ttk.Entry(left_frame,textvariable=self.var_name, width=25, font=("times new roman", 10, "italic"))
        studentid_entry.grid(row=0, column=1, padx=5, sticky=W)

        date_label = Label(left_frame, text="Date", font=("times new roman", 13, "italic"), bg="white")
        date_label.grid(row=1, column=0, padx=5, sticky=W)
        timed_entry = ttk.Entry(left_frame,textvariable=self.var_datetime, width=25, font=("times new roman", 10, "italic"))
        timed_entry.grid(row=1, column=1, padx=5, sticky=W)

        studentrool_label = Label(left_frame, text="Time", font=("times new roman", 13, "italic"), bg="white")
        studentrool_label.grid(row=2, column=0, padx=5, sticky=W)
        studentrool_entry = ttk.Entry(left_frame,textvariable=self.var_time, width=25, font=( "times new roman", 10, "italic"))
        studentrool_entry.grid(row=2, column=1, padx=5, sticky=W)

        studentdivsision_label = Label(left_frame, text="Student Satus", font=("times new roman", 13, "italic"), bg="white")
        studentdivsision_label.grid(row=3, column=0, padx=5, sticky=W)
        divsision_combo = ttk.Combobox(left_frame, font=("times new roman", 12, "italic") ,textvariable=self.var_status,state="readonly")
        divsision_combo["values"] = ("Status", "Present", "absent")
        divsision_combo.current(0)
        divsision_combo.grid(row=3, column=1, padx=5, pady=5, sticky=W)

         # button fram
        btn_frame = Frame(left_frame, bd=2, relief=SUNKEN, bg="white")
        btn_frame.place(x=0, y=150, width=315, height=33)

        save_btn = Button(btn_frame, text="Import csv",command=self.import_csv,activebackground='darkblue',activeforeground='white', font=("times new roman", 9, "italic"), bg="darkblue", fg="white", width=22, )
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv",command=self.export_csv, activebackground='darkblue',activeforeground='white',font=("times new roman", 9, "italic"), bg="darkblue", fg="white", width=22,)
        update_btn.grid(row=0, column=1)

        #second button frame

        # btn_frame1 = Frame(left_frame, bd=2, relief=SUNKEN, bg="white")
        # btn_frame1.place(x=0, y=185, width=315, height=33)
        # delete_btn = Button(btn_frame1, text="Update",activebackground='darkblue',activeforeground='white', font=("times new roman", 9, "italic"), bg="darkblue", fg="white", width=22, )
        # delete_btn.grid(row=0, column=0)

        # reset_btn = Button(btn_frame1, text="Reset",command=self.reset_data,activebackground='darkblue',activeforeground='white', font=("times new roman", 9, "italic"), bg="darkblue", fg="white", width=22, )
        # reset_btn.grid(row=0, column=1)

        #inner frame
        inner_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE,text="Attendance detial", font=("times new roman", 15, "italic"))
        inner_frame.place(x=330, y=5, width=295, height=280)

         # table frame
        table_frame = Frame(inner_frame, bg="white", bd=1, relief=SUNKEN)
        table_frame.place(x=3, y=5, width=285, height=245)

        # scrool bar
        Scrollbar_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        Scrollbar_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=('Name','DateTime','time','Status'), xscrollcommand=Scrollbar_x.set, yscrollcommand=Scrollbar_y.set)

        Scrollbar_x.pack(side=BOTTOM, fill=X)
        Scrollbar_y.pack(side=RIGHT, fill=Y)
        Scrollbar_x.config(command=self.student_table.xview)
        Scrollbar_y.config(command=self.student_table.yview)

        
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("DateTime", text="Date")
        self.student_table.heading("Status", text="Status")
        self.student_table.heading("time", text="Time")
        self.student_table["show"] = "headings"

        
        self.student_table.column("Name", width=100,anchor=CENTER)
        self.student_table.column("DateTime", width=100,anchor=CENTER)
        self.student_table.column("Status", width=100,anchor=CENTER)
        self.student_table.column("time", width=100,anchor=CENTER)
        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind('<ButtonRelease>',self.get_cursor)



        #============fetch data=========
    def fetch_data(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)   

    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(('CSV File','*.csv'),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=',')
            for i in csvread:
                mydata.append(i)

            self.fetch_data(mydata)   


    #============export data===============
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror('Error','No data found',parent=self.root)   
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(('CSV File','*.csv'),("ALL File","*.*")),parent=self.root) 
            with open(fln,mode='w',newline='') as myfile:
                exp_data=csv.writer(myfile,delimiter=',')
                for i in mydata:
                 exp_data.writerows(i)
                 messagebox.showinfo('Data Exort',"Your data exported to "+os.path.basename(fln) + " Successfully")  
        except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)
    def get_cursor(self,event=''):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        rows=content['values']
        self.var_name.set(rows[0]) 
        self.var_datetime.set(rows[1])            
        self.var_status.set(rows[2])   


    def reset_data(self):
        self.var_name.set('') 
        self.var_datetime.set('')            
        self.var_status.set('')   


                   
        










    
        
       









if __name__ == "__main__":
    root=Tk()
    obj = attendance_(root)
    root.mainloop()                          