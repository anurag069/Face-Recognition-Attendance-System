from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import numpy as np
from time import strftime
from datetime import datetime
import mysql.connector
import cv2


class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")
        # ==============variables===============
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_years = StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_fullname = StringVar()
        self.var_divs = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()

        # ======================fg image=================
        img = Image.open( r"imgs\depositphotos_270570388-stock-illustration-low-poly-male-human-face.jpg")
        img = img.resize((1530, 220), Image.Resampling.LANCZOS)
        self.img_ = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.img_)
        f_lbl.place(x=0, y=0, width=1530, height=150)

        # ==============bg image==============

        img2 = Image.open(r"imgs\bg.jpg")
        img2 = img2.resize((1530, 570), Image.Resampling.LANCZOS)
        self.img2_ = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.img2_)
        bg_img.place(x=0, y=155, width=1530, height=570)

        title_lbl = Label(bg_img,text="Student Managemet System", font=("times new roman", 15, "italic"),bg="black", fg="green", cursor="hand2", justify=CENTER)
        title_lbl.place(x=-100, y=0, width=1530, height=45)

        #datetime
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman",15,"italic"),bg="black",fg="green",cursor="hand2")
        lbl.place(x=68,y=0,width=200,height=50)  
        time()  

        main_frame = Frame(bg_img, bd=3, bg="white", border=2)
        main_frame.place(x=0, y=0, width=1500, height=650)

        # left side frame
        left_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE,text="Student Detial", font=("times new roman", 15, "italic"))
        left_frame.place(x=10, y=5, width=660, height=550)

        img3 = Image.open(r"imgs\banner1.jpg")
        img3 = img3.resize((660, 150), Image.Resampling.LANCZOS)
        self.img3_ = ImageTk.PhotoImage(img3)
        f_lbl = Label(left_frame, image=self.img3_)
        f_lbl.place(x=0, y=0, width=660, height=150)

        # current cource
        Cource_frame1 = LabelFrame(left_frame, bg="white", bd=2, relief=SUNKEN,text="Cource information", font=("times new roman", 15, "italic"))
        Cource_frame1.place(x=5, y=155, width=645, height=100)

        # department
        dep_label = Label(Cource_frame1, text="Deparment", font=("times new roman", 12, "italic"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(Cource_frame1, font=(
            "times new roman", 10, "italic"), state="readonly", textvariable=self.var_dep)
        dep_combo["values"] = ("Select Department", "Computer", "Civil", "IT")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        # Cource
        course_label = Label(Cource_frame1, text="Cource", font=("times new roman", 12, "italic"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(Cource_frame1, font=("times new roman", 10, "italic"), state="readonly", textvariable=self.var_course)
        course_combo["values"] = (" Select Courses", "Diploma", "Bechelor", "MD")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # years

        years_label = Label(Cource_frame1, text="years", font=("times new roman", 12, "italic"), bg="white")
        years_label.grid(row=1, column=0, padx=10, sticky=W)

        years_combo = ttk.Combobox(Cource_frame1, font=("times new roman", 10, "italic"), state="readonly", textvariable=self.var_years)
        years_combo["values"] = ("2076", "2077", "2078", "2079")
        years_combo.current(0)
        years_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # Semester
        sem_label = Label(Cource_frame1, text="Semester", font=("times new roman", 12, "italic"), bg="white")
        sem_label.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(Cource_frame1, font=("times new roman", 10, "italic"), state="readonly", textvariable=self.var_semester)
        sem_combo["values"] = ("I", "II", "III", "IV", "V", "VI")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # Student information frame
        student_frame1 = LabelFrame(left_frame, bg="white", bd=2, relief=SUNKEN,
                                    text="Class Student information", font=("times new roman", 15, "italic"))
        student_frame1.place(x=5, y=250, width=645, height=250)
        # Student Id

        studentid_label = Label(student_frame1, text="StudentID:", font=(
            "times new roman", 12, "italic"), bg="white")
        studentid_label.grid(row=0, column=0, padx=10, sticky=W)

        studentid_entry = ttk.Entry(student_frame1, width=25, font=(
            "times new roman", 9, "italic"), textvariable=self.var_id)
        studentid_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student fullname

        studentfullname_label = Label(student_frame1, text="Student fullname:", font=(
            "times new roman", 12, "italic"), bg="white")
        studentfullname_label.grid(row=0, column=2, padx=5, sticky=W)

        studentfullname_entry = ttk.Entry(student_frame1, width=25, font=(
            "times new roman", 9, "italic"), textvariable=self.var_fullname)
        studentfullname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class divsision
        studentdivsision_label = Label(student_frame1, text="Student divsision:", font=(
            "times new roman", 12, "italic"), bg="white")
        studentdivsision_label.grid(row=1, column=0, padx=10, sticky=W)

        divsision_combo = ttk.Combobox(student_frame1, font=(
            "times new roman", 10, "italic"), state="readonly", textvariable=self.var_divs)
        divsision_combo["values"] = ("Select divs", "A", "B", "C", "D", "E")
        divsision_combo.current(0)
        divsision_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll no
        studentrool_label = Label(student_frame1, text="Roll No:", font=(
            "times new roman", 12, "italic"), bg="white")
        studentrool_label.grid(row=1, column=2, padx=10, sticky=W)

        studentrool_entry = ttk.Entry(student_frame1, width=25, font=(
            "times new roman", 9, "italic"), textvariable=self.var_roll)
        studentrool_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Address
        studentgender_label = Label(student_frame1, text="Address:", font=(
            "times new roman", 12, "italic"), bg="white")
        studentgender_label.grid(row=2, column=0, padx=10, sticky=W)

        studentgender_entry = ttk.Entry(student_frame1, width=25, font=(
            "times new roman", 9, "italic"), textvariable=self.var_address)
        studentgender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # date of birth
        studentgender_label1 = Label(student_frame1, text="DOB:", font=(
            "times new roman", 12, "italic"), bg="white")
        studentgender_label1.grid(row=2, column=2, padx=10, sticky=W)

        studentgender_entry1 = ttk.Entry(student_frame1, width=25, font=(
            "times new roman", 9, "italic"), textvariable=self.var_dob)
        studentgender_entry1.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # email
        studentemail_label1 = Label(student_frame1, text="Email:", font=(
            "times new roman", 12, "italic"), bg="white")
        studentemail_label1.grid(row=3, column=0, padx=10, sticky=W)

        studentemail_entry1 = ttk.Entry(student_frame1, width=25, font=("times new roman", 9, "italic"), textvariable=self.var_email)
        studentemail_entry1.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # phone
        studentphone_label1 = Label(student_frame1, text="Phone:", font=("times new roman", 12, "italic"), bg="white")
        studentphone_label1.grid(row=3, column=2, padx=10, sticky=W)

        studentphone_entry1 = ttk.Entry(student_frame1, width=25, font=("times new roman", 9, "italic"), textvariable=self.var_phone)
        studentphone_entry1.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # radio button
        self.var_radio1 = StringVar()
        radio_btn1 = ttk.Radiobutton(
            student_frame1, text="Take photo sample", value="Yes", variable=self.var_radio1)
        radio_btn1.grid(row=5, column=0)

        self.var_radio2 = StringVar()
        radio_btn2 = ttk.Radiobutton(
            student_frame1, text="No photo sample", value="No", variable=self.var_radio1)
        radio_btn2.grid(row=5, column=1)

        # button fram
        btn_frame = Frame(student_frame1, bd=2, relief=SUNKEN, bg="white")
        btn_frame.place(x=0, y=150, width=660, height=33)

        save_btn = Button(btn_frame, text="Save", activebackground='darkblue',activeforeground='white',font=("times new roman", 9, "italic"), bg="darkblue", fg="white", width=22, command=self.add_data)
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update",activebackground='darkblue',activeforeground='white', font=("times new roman", 9, "italic"), bg="darkblue", fg="white", width=22, command=self.upadte_data)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",activebackground='darkblue',activeforeground='white', font=("times new roman", 9, "italic"), bg="darkblue", fg="white", width=22, command=self.delete_data)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",activebackground='darkblue',activeforeground='white', font=("times new roman", 9, "italic"), bg="darkblue", fg="white", width=22, command=self.reset_data)
        reset_btn.grid(row=0, column=3)
        # second btn frame
        btn_frame1 = Frame(student_frame1, bd=1, relief=SUNKEN, bg="white")
        btn_frame1.place(x=0, y=185, width=660, height=33)

        take_photo_btn = Button(btn_frame1, text="Take photo", activebackground='darkblue',activeforeground='white',font=(
            "times new roman", 9, "italic"), bg="darkblue", fg="white", width=45, command=self.generate_data)
        take_photo_btn.grid(row=0, column=0)

        updat_photo_btn = Button(btn_frame1, text="Upload photo", font=(
            "times new roman", 9, "italic"), bg="darkblue", fg="white", width=45)
        updat_photo_btn.grid(row=0, column=1)

        # right side frame
        right_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE,
                                 text="Student Detial", font=("times new roman", 15, "italic"))
        right_frame.place(x=680, y=5, width=660, height=550)

        img4 = Image.open(r"imgs\st.jpg")
        img4 = img4.resize((660, 150), Image.Resampling.LANCZOS)
        self.img4_ = ImageTk.PhotoImage(img4)
        f_lbl1 = Label(right_frame, image=self.img4_)
        f_lbl1.place(x=0, y=0, width=660, height=150)

        # ============Search System===========
        search_frame = LabelFrame(right_frame, bg="white", bd=1, relief=SUNKEN,
                                  text="Search System", font=("times new roman", 15, "italic"))
        search_frame.place(x=5, y=155, width=660, height=70)

        # search label

        search_label1 = Label(search_frame, text="Search:", font=("times new roman", 12, "italic"), bg="red")
        search_label1.grid(row=0, column=0, padx=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=( "times new roman", 10, "italic"), state="readonly")
        search_combo["values"] = (" Select", "Phone_No", "Gmail")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 9, "italic"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # search button

        search_btn = Button(search_frame, text="Delete", font=( "times new roman", 9, "italic"), bg="darkblue", fg="white", width=17)
        search_btn.grid(row=0, column=3, padx=3)

        showall_btn = Button(search_frame, text="Show All", font=("times new roman", 9, "italic"), bg="darkblue", fg="white", width=17)
        showall_btn.grid(row=0, column=4)

        # table frame
        table_frame = Frame(right_frame, bg="white", bd=1, relief=SUNKEN)
        table_frame.place(x=5, y=230, width=660, height=265)

        # scrool bar
        Scrollbar_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        Scrollbar_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("Dep", "course", "years", "sem", "id", "fullname", "divs", "roll","dob", "email", "phone", "address", "photo"), xscrollcommand=Scrollbar_x.set, yscrollcommand=Scrollbar_y.set)

        Scrollbar_x.pack(side=BOTTOM, fill=X)
        Scrollbar_y.pack(side=RIGHT, fill=Y)
        Scrollbar_x.config(command=self.student_table.xview)
        Scrollbar_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("course", text="Couse")
        self.student_table.heading("years", text="years")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("fullname", text="fullname")
        self.student_table.heading("divs", text="divsision")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="PhotoSample")
        self.student_table["show"] = "headings"

        self.student_table.column("Dep", width=100,anchor=CENTER)
        self.student_table.column("course", width=100,anchor=CENTER)
        self.student_table.column("years", width=100,anchor=CENTER)
        self.student_table.column("sem", width=100,anchor=CENTER)
        self.student_table.column("id", width=100,anchor=CENTER)
        self.student_table.column("fullname", width=100,anchor=CENTER)
        self.student_table.column("divs", width=100,anchor=CENTER)
        self.student_table.column("roll", width=100,anchor=CENTER)
        self.student_table.column("dob", width=100,anchor=CENTER)
        self.student_table.column("email", width=100,anchor=CENTER)
        self.student_table.column("phone", width=100,anchor=CENTER)
        self.student_table.column("address", width=100,anchor=CENTER)
        self.student_table.column("photo", width=100,anchor=CENTER)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.featch_data()
      # =====Function decration=======

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_fullname.get() == "" or self.var_id.get() == "": messagebox.showerror(
                "Error", "Fill Up all fields", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect( host="localhost", user="root", password="", database="student")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_years.get(),
                    self.var_semester.get(),
                    self.var_id.get(),
                    self.var_fullname.get(),
                    self.var_divs.get(),
                    self.var_roll.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.featch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    def featch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="student")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from students")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ==============Get cursor=======================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_years.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_fullname.set(data[5]),
        self.var_divs.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])

    # update functon

    def upadte_data(self):
        if self.var_dep.get() == "Select Department" or self.var_fullname.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "Fill Up all fields", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update student detail", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="student")
                    my_cursor = conn.cursor()

                    my_cursor.execute("update students set Dep=%s,course=%s,years=%s,sem=%s,fullname=%s,divs=%s,roll=%s,dob=%s,email=%s,phone=%s,address=%s,photo=%s where StudentId = %s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_years.get(),
                        self.var_semester.get(),
                        self.var_fullname.get(),
                        self.var_divs.get(),
                        self.var_roll.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        self.var_id.get()

                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Student details successfully update completed", parent=self.root)
                conn.commit()
                self.featch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)
    # delete function

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "StudentId is Compalsary", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Remove Student", "Dou you want to delete the Student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="", database="student")
                    my_cursor = conn.cursor()
                    sql = "delete from students where StudentId = %s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                messagebox.showinfo(
                    "Delete", "Successfully Deleted the student")
                conn.commit()
                self.featch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)
    # reset

    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select"),
        self.var_years.set("Select years"),
        self.var_semester.set("Select Semester"),
        self.var_id.set(""),
        self.var_fullname.set(""),
        self.var_divs.set("Select divsision"),
        self.var_roll.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_radio1.set("")
    # ================================ Generate data set or take photo===================

    def generate_data(self):
        if self.var_dep.get() == "Select Department" or self.var_fullname.get() == "" or self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Fill Up all fields", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect( host="localhost", user="root", password="", database="student")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from students")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1

                my_cursor.execute("update students set Dep=%s,course=%s,years=%s,sem=%s,fullname=%s,divs=%s,roll=%s,dob=%s,email=%s,phone=%s,address=%s,photo=%s where StudentId = %s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_years.get(),
                    self.var_semester.get(),
                    self.var_fullname.get(),
                    self.var_divs.get(),
                    self.var_roll.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_radio1.get(),
                    self.var_id.get() == id+1

                ))
                conn.commit()
                self.featch_data()
                self.reset_data()
                conn.close()

                face_cap = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,video_data=cap.read()
                    col=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
                    faces=face_cap.detectMultiScale(col,1.1,5)
                    

                    for(x,y,w,h) in faces:
                        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
                    file_fullname_path="data/anurag"+str(id)+"."+str(img_id)+".jpg"
                    img_id+=1
                    cv2.imshow("photo",video_data)
                    cv2.imwrite(file_fullname_path,col)
                    cv2.putText(faces,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                


               
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets compled!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    # root.wm_iconbitmap('C:\\Users\\__anurag\\OneDrive\\Desktop\\M_J__P\\User-Files-icon.png')
    root.mainloop()
