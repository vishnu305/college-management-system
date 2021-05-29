import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
#   from tkcalendar import Calendar
import sqlite3
from tkinter import messagebox
def insert():
    #sd1,sd3,sd4,sd5,sd6,sd15,sd11,sd13,reason1,reason,sd7,sd8,sd16,ad,sd12,sd14
    name = sd1.get()
    fname = sd3.get()
    mname = sd4.get()
    foccu = sd5.get()
    moccu = sd6.get()
    address = sd15.get()
    mobno = sd11.get()
    landno = sd13.get()
    section = reason1.get()
    course = reason.get()
    dob = sd7.get()
    gender = sd8.get()
    admdate = sd16.get()
    admnum = ad.get()
    bloodgroup = sd12.get()
    religion = sd14.get()

    conn = sqlite3.connect("student")
    conn.execute('''CREATE TABLE IF NOT EXISTS data_base(ADMISSION_NUMBER TEXT PRIMARY KEY , ADMISSION_DATE TEXT , STUDENT_NAME TEXT , FATHER_NAME TEXT , MOTHER_NAME TEXT , FATHER_OCCUPATION TEXT , MOTHER_OCCUPATION TEXT , MOBILE_NO TEXT , LANDLINE_NO TEXT , ADDRESS1 TEXT , COURSE TEXT , SECTION TEXT ,DATE_OF_BIRTH TEXT ,GENDER TEXT ,BLOOD TEXT ,RELIGION TEXT )''')
    

    conn.execute('''INSERT INTO data_base(ADMISSION_NUMBER,ADMISSION_DATE,STUDENT_NAME,FATHER_NAME,MOTHER_NAME,FATHER_OCCUPATION,MOTHER_OCCUPATION,MOBILE_NO,LANDLINE_NO,ADDRESS1,COURSE,SECTION,DATE_OF_BIRTH,GENDER,BLOOD,RELIGION)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (admnum,admdate,name,fname,mname,foccu,moccu,mobno,landno,address,course,section,dob,gender,bloodgroup,religion))
    
    conn.commit()
    #conn.close()
    messagebox.showinfo("New Student Data","Student Data Succesfully Created")
def search2(admnum,admdate,name,fname,mname,foccu,moccu,mobno,landno,address,course,section,dob,bloodgroup,religion):
       conn = sqlite3.connect("student")
       corr = conn.cursor()
       

       #corr.execute("SELECT * FROM data_base WHERE STUDENT_NAME = ? OR ADMISSION_NUMBER = ?", (name,admnum))
       #corr.execute("SELECT * FROM data_base WHERE ADMISSION_NUMBER = ?", admnum)
       try:
           corr.execute("SELECT * FROM data_base WHERE ADMISSION_NUMBER = ?", (admnum))
       except:
           messagebox.showerror("Error in Searching","The given admission number is wrong")
       rows = corr.fetchall()
       return rows
       
       conn.close()
def search1():
    for i in student_table.get_children():
        student_table.delete(i)
    student_table.insert('',END,values='')
    for row in search2(ad2.get(),sd162.get(),sd12.get(),sd32.get(),sd42.get(),sd52.get(),sd62.get(),sd112.get(),sd132.get(),sd152.get(),reason2.get(),reason12.get(),sd72.get(),sd122.get(),sd142.get()):
        #print(row)
        student_table.insert('',END,values=(row[0],row[2],row[10]))
                    
def updatestudent():
    conn = sqlite3.connect("student")
    cur = conn.cursor()
    #cur.execute("UPDATE data_base SET ADMISSION_NUMBER = ? , ADMISSION_DATE = ? , STUDENT_NAME = ? , FATHER_NAME = ? , MOTHER_NAME = ? , FATHER_OCCUPATION = ? , MOTHER_OCCUPATION = ? , MOBILE_NO = ? , LANDLINE_NO = ? , ADDRESS1 = ? , COURSE = ? , SECTION = ? , DATE_OF_BIRTH = ? , GENDER = ? , BLOOD = ? , RELIGION = ? WHERE ADMISSION_NUMBER = ?", (ad2.get(),sd162.get(),sd12.get(),sd32.get(),sd42.get(),sd52.get(),sd62.get(),sd112.get(),sd132.get(),sd152.get(),reason2.get(),reason12.get(),sd72.get(),sd82.get(),sd122.get(),sd142.get(),ad2.get()))
    try:
        cur.execute("UPDATE data_base SET ADMISSION_NUMBER = ? , ADMISSION_DATE = ? , STUDENT_NAME = ? , FATHER_NAME = ? , MOTHER_NAME = ? , FATHER_OCCUPATION = ? , MOTHER_OCCUPATION = ? , MOBILE_NO = ? , LANDLINE_NO = ? , ADDRESS1 = ? , COURSE = ? , SECTION = ? , DATE_OF_BIRTH = ? , GENDER = ? , BLOOD = ? , RELIGION = ? WHERE ADMISSION_NUMBER = ?", (ad2.get(),sd162.get(),sd12.get(),sd32.get(),sd42.get(),sd52.get(),sd62.get(),sd112.get(),sd132.get(),sd152.get(),reason2.get(),reason12.get(),sd72.get(),sd82.get(),sd122.get(),sd142.get(),ad2.get()))
        messagebox.showinfo("Updating","Successfully Updated")
    except:
        messagebox.showerror("updating error","Data not Updated")

    conn.commit()
    conn.close()
def deletestudent():
    conn = sqlite3.connect("student")
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM data_base WHERE ADMISSION_NUMBER = ?", ad2.get())
        messagebox.showinfo("Deleting","Data Deleted Successfully")
    except:
        messagebox.showerror("deleting error","Data not Deleted")

    conn.commit()
    conn.close()
def hi(e):

    try: 
        
        for row in search2(ad2.get(),sd162.get(),sd12.get(),sd32.get(),sd42.get(),sd52.get(),sd62.get(),sd112.get(),sd132.get(),sd152.get(),reason2.get(),reason12.get(),sd72.get(),sd122.get(),sd142.get()):
            #Entry_gender.delete(0, END)
            #Entry_gender.insert(END, selected_tuple[8])
            #religion11.delete(0,END)
            sd142.set(row[15])
            ad2.set(row[0])
            sd162.set(row[1])
            sd12.set(row[2])
            sd32.set(row[3])
            sd42.set(row[4])
            sd52.set(row[5])
            sd62.set(row[6])
            sd112.set(row[7])
            sd132.set(row[8])
            sd152.set(row[9])
            reason2.set(row[10])
            reason12.set(row[11])
            sd72.set(row[12])
            sd82.set(row[13])
            sd122.set(row[14])
    except IndexError:
        pass
        
def student(window1):
    
    
    
    global sd1,sd3,sd4,sd5,sd6,sd15,sd11,sd13,reason1,reason,sd7,sd8,sd16,ad,sd12,sd14

    sd1=StringVar()
    #sd2=StringVar()
    sd3=StringVar()
    sd4=StringVar()
    sd5=StringVar()
    sd6=StringVar()
    sd7=StringVar()
    sd8=StringVar()
    #sd9=StringVar()
    #sd10=StringVar()
    sd11=StringVar()
    #sd12=StringVar()
    sd13=StringVar()
    #sd14=StringVar()
    sd15=StringVar()
    sd16=StringVar()
    sd12= StringVar()
    sd14 = StringVar()
    ad=StringVar()
    window2 = Toplevel(window1)
    window2.geometry("1216x660+306+124")
    window2.title("Student Management")
    

        #dbase3=sqlite3.connect(my_data)
        #dbase3.execute('''CREATE TABLE IF NOT EXISTS data_base(DATE TEXT NOT NULL, PARTICULARS TEXT NOT NULL, WITHDRAWLS TEXT NOT NULL, DEPOSITS TEXT NOT NULL, BALANCE TEXT NOT NULL)''')
        #dbase3.execute('''INSERT INTO data_base(DATE,PARTICULARS,WITHDRAWLS,DEPOSITS,BALANCE)VALUES(?,?,?,?,?)''',(str(dt.datetime.now()),str(reason),str(atbt),'',str(updated_balance11)))
        #dbase3.commit()

    
    def admission():
        for widget in window2.winfo_children():
            widget.destroy()
        global sd1,sd3,sd4,sd5,sd6,sd15,sd11,sd13,reason1,reason,sd7,sd8,sd16,ad,sd12,sd14,reason1,reason

        sd1=StringVar()
        #sd2=StringVar()
        sd3=StringVar()
        sd4=StringVar()
        sd5=StringVar()
        sd6=StringVar()
        sd7=StringVar()
        sd8=StringVar()
        #sd9=StringVar()
        #sd10=StringVar()
        sd11=StringVar()
        #sd12=StringVar()
        sd13=StringVar()
        #sd14=StringVar()
        sd15=StringVar()
        sd16=StringVar()
        sd12= StringVar()
        sd14 = StringVar()
        ad=StringVar()
        Label(window2,text = "Enter Admission Number",bg="white",fg="black").place(x=50,y=50)
        ad=StringVar()
        Entry(window2,textvar = ad,width = 30).place(x=230,y=50)
        Label(window2,text = "Admissions",relief = "solid",font=("times new roman",15,"bold")).pack()
        Label(window2,text = "Enter Name",bg='white',fg='black').place(x=50,y=100)
        #Label(window2,text = "Last Name",bg='white',fg='black').place(x=500,y=100)
        Label(window2,text = "Father's Name",bg='white',fg='black').place(x=50,y=150)
        Label(window2,text = "Mother's Name",bg='white',fg='black').place(x=500,y=150)
        Label(window2,text = "Father's Occupation",bg='white',fg='black').place(x=50,y=200)
        Label(window2,text = "Mother's Occupation",bg='white',fg='black').place(x=500,y=200)
        Label(window2,text = "Date of Birth (DD/MM/YY)",bg='white',fg='black').place(x=50,y=250)
        Label(window2,text = "Gender",bg='white',fg='black').place(x=500,y=250)
        Label(window2,text = "Course",bg='white',fg='black').place(x=50,y=300)
        Label(window2,text = "Section",bg='white',fg='black').place(x=500,y=300)
        Label(window2,text = "Phone Number",bg='white',fg='black').place(x=50,y=350)
        Label(window2,text = "Blood Group",bg='white',fg='black').place(x=500,y=350)
        Label(window2,text = "Landline Number",bg='white',fg='black').place(x=50,y=400)
        Label(window2,text = "Religion",bg='white',fg='black').place(x=500,y=400)
        Label(window2,text = "Address",bg='white',fg='black').place(x=50,y=450)
        Label(window2,text = "Admission Date",bg='white',fg='black').place(x=500,y=50)
        
        Entry(window2,textvar=sd1,width= 30).place(x=230,y=100)
        #Entry(window2,textvar=sd2,width= 30).place(x=680,y=100)
        Entry(window2,textvar=sd3,width= 30).place(x=230,y=150)
        Entry(window2,textvar=sd4,width= 30).place(x=680,y=150)
        Entry(window2,textvar=sd5,width= 30).place(x=230,y=200)
        Entry(window2,textvar=sd6,width= 30).place(x=680,y=200)
        Entry(window2,textvar=sd7,width= 30).place(x=230,y=250)
        #sd7 = Calendar(window2,selectmode = 'day',cursor = 'hand1',year=2021,month = 2,day=5)
        #sd7.place(x=230,y=250)

        #Entry(window2,textvar=sd8,width= 30).place(x=680,y=250)
        r1=Radiobutton(window2,text="Male",variable = sd8,value = 'Male',bg='white').place(x=680,y=250)
        r2=Radiobutton(window2,text="Female",variable = sd8,value = 'Female',bg='white').place(x=760,y=250)
        #Entry(window2,textvar=sd9,width= 30).place(x=230,y=300)
        reason=StringVar()
        file2 = open("Course.txt","r")
        file2_data = file2.read()
        list11=file2_data.split('\n')
        #list11=["Inter 1st Year","Inter 2nd Year"]
        file2.close()
                    
        reason=ttk.Combobox(window2,value=list11,width=30)
        reason.set("Choose Course")
        reason.place(x=230,y=300)
        #Entry(window2,textvar=sd10,width= 30).place(x=680,y=300)
        reason1=StringVar()
        file1 = open("Section.txt","r")
        file1_data = file1.read()
        list12 = file1_data.split('\n')
        #list12=['A','B','C']
        file1.close()
                    #droplist11=OptionMenu(window11,reason,*list11)
                    #reason.set("Select Reason")
                    #droplist11.config(width=15)
                    #droplist11.place(x=500,y=196)
        reason1=ttk.Combobox(window2,value=list12,width=30)
        reason1.set("Choose Section")
        reason1.place(x=680,y=300)
        Entry(window2,textvar=sd11,width= 30).place(x=230,y=350)
        Entry(window2,textvar=sd12,width= 30).place(x=680,y=350)
        Entry(window2,textvar=sd13,width= 30).place(x=230,y=400)
        Entry(window2,textvar=sd14,width= 30).place(x=680,y=400)
        Entry(window2,textvar=sd15,width=80).place(x=230,y=450,height=100)#Text(window2,width = 80,height = 6).place(x=230,y=450)
        Entry(window2,textvar=sd16,width= 30).place(x=680,y=50)
        #name = " ", fname = " ", mname = " ", foccu = " ",moccu = " ",address = " ", mobno = " ",landno = " ", section = " ",course = " ", dob = " ", gender = " ",admdate = " ",admnum = " "
        Button(window2,text="Save",command = lambda: insert()).place(x=230,y=600)
        Button(window2,text = "Upload").place(x=1050,y=400)
        image2=Image.open('image2.png')
        photo2=ImageTk.PhotoImage(image2)
        lab1=Label(window2,image=photo2)
        lab1.config(height=225)
        lab1.place(x=940,y=150)

        menu = Menu(window2)
        window2.config(menu = menu)
        submenu1=Menu(window2)
        menu.add_cascade(label = "Admissions",menu=submenu1)
        submenu1.add_command(label = "Admissions",command = lambda: admission())
        submenu2=Menu(window2)
        menu.add_cascade(label='Search',menu = submenu2)
        submenu2.add_command(label = "Search",command = lambda: search())


    def search():
        for widget in window2.winfo_children():
            widget.destroy()
        
        
        global sd12,sd32,sd42,sd52,sd62,sd152,sd112,sd132,reason12,reason2,sd72,sd82,sd162,ad2,sd122,sd142,student_table,admission_number1,stname,ftname,mtname,ftoccu,mtoccu,dob11,mobileno,blood11,landlineno,religion11,address222,admission_date1

        sd12=StringVar()
        #sd2=StringVar()
        sd32=StringVar()
        sd42=StringVar()
        sd52=StringVar()
        sd62=StringVar()
        sd72=StringVar()
        sd82=StringVar()
        #sd9=StringVar()
        #sd10=StringVar()
        sd112=StringVar()
        #sd12=StringVar()
        sd132=StringVar()
        #sd14=StringVar()
        sd152=StringVar()
        sd162=StringVar()
        sd122= StringVar()
        sd142 = StringVar()
        reason12=StringVar()
        reason2=StringVar()
        ad2=StringVar()
        Label(window2,text = "Search",relief = "solid",font=("times new roman",15,"bold")).pack()
        Label(window2,text = "Enter Admission Number",bg="white",fg="black").place(x=50,y=50)
        ad=StringVar()
        admission_number1=Entry(window2,textvar = ad2,width = 30).place(x=230,y=50)
        
        Label(window2,text = "Enter Name",bg='white',fg='black').place(x=50,y=100)
        #Label(window2,text = "Last Name",bg='white',fg='black').place(x=500,y=100)
        Label(window2,text = "Father's Name",bg='white',fg='black').place(x=50,y=150)
        Label(window2,text = "Mother's Name",bg='white',fg='black').place(x=500,y=150)
        Label(window2,text = "Father's Occupation",bg='white',fg='black').place(x=50,y=200)
        Label(window2,text = "Mother's Occupation",bg='white',fg='black').place(x=500,y=200)
        Label(window2,text = "Date of Birth (DD/MM/YY)",bg='white',fg='black').place(x=50,y=250)
        Label(window2,text = "Gender",bg='white',fg='black').place(x=500,y=250)
        Label(window2,text = "Course",bg='white',fg='black').place(x=50,y=300)
        Label(window2,text = "Section",bg='white',fg='black').place(x=500,y=300)
        Label(window2,text = "Phone Number",bg='white',fg='black').place(x=50,y=350)
        Label(window2,text = "Blood Group",bg='white',fg='black').place(x=500,y=350)
        Label(window2,text = "Landline Number",bg='white',fg='black').place(x=50,y=400)
        Label(window2,text = "Religion",bg='white',fg='black').place(x=500,y=400)
        Label(window2,text = "Address",bg='white',fg='black').place(x=50,y=450)
        Label(window2,text = "Admission Date",bg='white',fg='black').place(x=500,y=50)
        
        stname=Entry(window2,textvar=sd12,width= 30).place(x=230,y=100)
        #Entry(window2,textvar=sd2,width= 30).place(x=680,y=100)
        ftname=Entry(window2,textvar=sd32,width= 30).place(x=230,y=150)
        mtname=Entry(window2,textvar=sd42,width= 30).place(x=680,y=150)
        ftoccu=Entry(window2,textvar=sd52,width= 30).place(x=230,y=200)
        mtoccu=Entry(window2,textvar=sd62,width= 30).place(x=680,y=200)
        dob11=Entry(window2,textvar=sd72,width= 30).place(x=230,y=250)
        #sd7 = Calendar(window2,selectmode = 'day',cursor = 'hand1',year=2021,month = 2,day=5)
        #sd7.place(x=230,y=250)

        #Entry(window2,textvar=sd8,width= 30).place(x=680,y=250)
        #r1=Radiobutton(window2,text="Male",variable = sd82,value = 'Male',bg='white').place(x=680,y=250)
        #r2=Radiobutton(window2,text="Female",variable = sd82,value = 'Female',bg='white').place(x=760,y=250)
        listsex = ["Male","Female"]
        sd82=ttk.Combobox(window2,value=listsex,width=30)
        sd82.set("Gender")
        sd82.place(x=680,y=250)
        #Entry(window2,textvar=sd9,width= 30).place(x=230,y=300)
        
        #list11=["Inter 1st Year","Inter 2nd Year"]
        file2 = open("Course.txt","r")
        file2_data = file2.read()
        list11=file2_data.split('\n')
        #list11=["Inter 1st Year","Inter 2nd Year"]
        file2.close()
                    
        reason2=ttk.Combobox(window2,value=list11,width=30)
        reason2.set("Choose Course")
        reason2.place(x=230,y=300)
        #Entry(window2,textvar=sd10,width= 30).place(x=680,y=300)
        
        #list12=['A','B','C']
        file1 = open("Section.txt","r")
        file1_data = file1.read()
        list12 = file1_data.split('\n')
        #list12=['A','B','C']
        file1.close()
                    #droplist11=OptionMenu(window11,reason,*list11)
                    #reason.set("Select Reason")
                    #droplist11.config(width=15)
                    #droplist11.place(x=500,y=196)
        reason12=ttk.Combobox(window2,value=list12,width=30)
        reason12.set("Choose Section")
        reason12.place(x=680,y=300)
        mobileno=Entry(window2,textvar=sd112,width= 30).place(x=230,y=350)
        blood11=Entry(window2,textvar=sd122,width= 30).place(x=680,y=350)
        landlineno=Entry(window2,textvar=sd132,width= 30).place(x=230,y=400)
        religion11=Entry(window2,textvar=sd142,width= 30).place(x=680,y=400)
        address222=Entry(window2,textvar=sd152,width=80).place(x=230,y=450,height=100)#Text(window2,width = 80,height = 6).place(x=230,y=450)
        admission_date1=Entry(window2,textvar=sd162,width= 30).place(x=680,y=50)
        #name = " ", fname = " ", mname = " ", foccu = " ",moccu = " ",address = " ", mobno = " ",landno = " ", section = " ",course = " ", dob = " ", gender = " ",admdate = " ",admnum = " "
        Button(window2,text="Save",command = lambda: insert()).place(x=230,y=600)
        Button(window2,text = "Upload").place(x=1050,y=400)
        image2=Image.open('image2.png')
        photo2=ImageTk.PhotoImage(image2)
        lab1=Label(window2,image=photo2)
        lab1.config(height=225)
        lab1.place(x=940,y=150)
        Button(window2,text="Update",command = lambda: updatestudent()).place(x=960,y=500)
        Button(window2,text = "Delete",command = lambda: deletestudent()).place(x=1020,y=500)
        Button(window2,text="Search",command = lambda: search1()).place(x=1080,y=500)
        student_table=ttk.Treeview(window2,columns=("Adm No","Name","Course"))
        Scroll = Scrollbar(student_table)
        Scroll.pack(side=RIGHT,  fill=Y)
        Scroll.config(command=student_table.yview)
        student_table.config(yscrollcommand=Scroll.set)
        #scroll_y.config(command=student_table.yview)
        #student_table.config(yscroll=window20.set)
        student_table.heading("Adm No",text="Adm No")
        student_table.heading("Name",text="Name")
        student_table.heading("Course",text="Course")
        student_table['show']='headings'
        student_table.pack(side = BOTTOM,fill = X)
        
        
        student_table.bind("<Double-1>", hi)




        menu = Menu(window2)
        window2.config(menu = menu)
        submenu1=Menu(window2)
        menu.add_cascade(label = "Admissions",menu=submenu1)
        submenu1.add_command(label = "Admissions",command = lambda: admission())
        submenu2=Menu(window2)
        menu.add_cascade(label='Search',menu = submenu2)
        submenu2.add_command(label = "Search",command = lambda: search())

    
    

    Label(window2,text = "Enter Admission Number",bg="white",fg="black").place(x=50,y=50)
    
    Entry(window2,textvar = ad,width = 30).place(x=230,y=50)
    Label(window2,text = "Admissions",relief = "solid",font=("times new roman",15,"bold")).pack()
    Label(window2,text = "Enter Name",bg='white',fg='black').place(x=50,y=100)
    #Label(window2,text = "Last Name",bg='white',fg='black').place(x=500,y=100)
    Label(window2,text = "Father's Name",bg='white',fg='black').place(x=50,y=150)
    Label(window2,text = "Mother's Name",bg='white',fg='black').place(x=500,y=150)
    Label(window2,text = "Father's Occupation",bg='white',fg='black').place(x=50,y=200)
    Label(window2,text = "Mother's Occupation",bg='white',fg='black').place(x=500,y=200)
    Label(window2,text = "Date of Birth (DD/MM/YY)",bg='white',fg='black').place(x=50,y=250)
    Label(window2,text = "Gender",bg='white',fg='black').place(x=500,y=250)
    Label(window2,text = "Course",bg='white',fg='black').place(x=50,y=300)
    Label(window2,text = "Section",bg='white',fg='black').place(x=500,y=300)
    Label(window2,text = "Phone Number",bg='white',fg='black').place(x=50,y=350)
    Label(window2,text = "Blood Group",bg='white',fg='black').place(x=500,y=350)
    Label(window2,text = "Landline Number",bg='white',fg='black').place(x=50,y=400)
    Label(window2,text = "Religion",bg='white',fg='black').place(x=500,y=400)
    Label(window2,text = "Address",bg='white',fg='black').place(x=50,y=450)
    Label(window2,text = "Admission Date",bg='white',fg='black').place(x=500,y=50)


    
    
    Entry(window2,textvar=sd1,width= 30).place(x=230,y=100)
    #Entry(window2,textvar=sd2,width= 30).place(x=680,y=100)
    Entry(window2,textvar=sd3,width= 30).place(x=230,y=150)
    Entry(window2,textvar=sd4,width= 30).place(x=680,y=150)
    Entry(window2,textvar=sd5,width= 30).place(x=230,y=200)
    Entry(window2,textvar=sd6,width= 30).place(x=680,y=200)
    Entry(window2,textvar=sd7,width= 30).place(x=230,y=250)
    #sd7 = Calendar(window2,selectmode = 'day',cursor = 'hand1',year=2021,month = 2,day=5)
    #sd7.place(x=230,y=250)

    #Entry(window2,textvar=sd8,width= 30).place(x=680,y=250)
    r1=Radiobutton(window2,text="Male",variable = sd8,value = 'Male',bg='white').place(x=680,y=250)
    r2=Radiobutton(window2,text="Female",variable = sd8,value = 'Female',bg='white').place(x=760,y=250)
    #Entry(window2,textvar=sd9,width= 30).place(x=230,y=300)
    reason=StringVar()
    #list11=['Inter 1st Year','Inter 2nd Year']
    file2 = open("Course.txt","r")
    file2_data = file2.read()
    list11=file2_data.split('\n')
    #list11=["Inter 1st Year","Inter 2nd Year"]
    file2.close()
                #droplist11=OptionMenu(window11,reason,*list11)
                #reason.set("Select Reason")
                #droplist11.config(width=15)
                #droplist11.place(x=500,y=196)
    reason=ttk.Combobox(window2,value=list11,width=30)
    reason.set("Choose Course")
    reason.place(x=230,y=300)
    #Entry(window2,textvar=sd10,width= 30).place(x=680,y=300)
    reason1=StringVar()
    #list12=['A','B','C']
    file1 = open("Section.txt","r")
    file1_data = file1.read()
    list12 = file1_data.split('\n')
    #list12=['A','B','C']
    file1.close()
                #droplist11=OptionMenu(window11,reason,*list11)
                #reason.set("Select Reason")
                #droplist11.config(width=15)
                #droplist11.place(x=500,y=196)
    reason1=ttk.Combobox(window2,value=list12,width=30)
    reason1.set("Choose Section")
    reason1.place(x=680,y=300)
    Entry(window2,textvar=sd11,width= 30).place(x=230,y=350)
    Entry(window2,textvar=sd12,width= 30).place(x=680,y=350)
    Entry(window2,textvar=sd13,width= 30).place(x=230,y=400)
    Entry(window2,textvar=sd14,width= 30).place(x=680,y=400)
    Entry(window2,textvar=sd15,width=80).place(x=230,y=450,height=100)#sd15 = Text(window2,width = 80,height = 6).place(x=230,y=450)
    Entry(window2,textvar=sd16,width= 30).place(x=680,y=50)
    
   
    
    

    Button(window2,text="Save",command = lambda: insert()).place(x=230,y=600)
    Button(window2,text = "Upload").place(x=1050,y=400)
    image2=Image.open('image2.png')
    photo2=ImageTk.PhotoImage(image2)
    lab1=Label(window2,image=photo2)
    lab1.config(height=225)
    lab1.place(x=940,y=150)

    menu = Menu(window2)
    window2.config(menu = menu)
    submenu1=Menu(window2)
    menu.add_cascade(label = "Admissions",menu=submenu1)
    submenu1.add_command(label = "Admissions",command = lambda: admission())
    submenu2=Menu(window2)
    menu.add_cascade(label='Search',menu = submenu2)
    submenu2.add_command(label = "Search",command = lambda: search())
    


    window2.mainloop()
def teachersave():
    name = sdd1.get()
    qualification = sdd3.get()
    email = sdd4.get()
    
    salary = sdd6.get()
    dob = sdd7.get()
    gender = sdd8.get()
    mobno = sdd10.get()
    subject = reasonsdd55.get()
    
    address = sdd11.get()
    

    conn = sqlite3.connect("staff")
    conn.execute('''CREATE TABLE IF NOT EXISTS data_base(FULL_NAME TEXT , QUALIFICATION TEXT , EMAIL_ID TEXT , SALARY TEXT , DATE_OF_BIRTH TEXT , GENDER TEXT , MOBILE_NO TEXT , SUBJECT1 TEXT , ADDRESS1 TEXT )''')
    

    conn.execute('''INSERT INTO data_base(FULL_NAME,QUALIFICATION,EMAIL_ID,SALARY,DATE_OF_BIRTH,GENDER,MOBILE_NO,SUBJECT1,ADDRESS1)VALUES(?,?,?,?,?,?,?,?,?)''', (name,qualification,email,salary,dob,gender,mobno,subject,address))
    
    conn.commit()
    #conn.close()
    messagebox.showinfo("New Staff Data","New Staff Data Succesfully Created")
def deleteteacher():
    conn = sqlite3.connect("staff")
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM data_base WHERE MOBILE_NO = ?", (sdd10.get(),))
        messagebox.showinfo("Deleting","Data Deleted Successfully")
    except:
        messagebox.showerror("deleting error","Data not Deleted")

    conn.commit()
    conn.close()
def updatedteacher():
    conn = sqlite3.connect("staff")
    cur = conn.cursor()
    #cur.execute("UPDATE data_base SET ADMISSION_NUMBER = ? , ADMISSION_DATE = ? , STUDENT_NAME = ? , FATHER_NAME = ? , MOTHER_NAME = ? , FATHER_OCCUPATION = ? , MOTHER_OCCUPATION = ? , MOBILE_NO = ? , LANDLINE_NO = ? , ADDRESS1 = ? , COURSE = ? , SECTION = ? , DATE_OF_BIRTH = ? , GENDER = ? , BLOOD = ? , RELIGION = ? WHERE ADMISSION_NUMBER = ?", (ad2.get(),sd162.get(),sd12.get(),sd32.get(),sd42.get(),sd52.get(),sd62.get(),sd112.get(),sd132.get(),sd152.get(),reason2.get(),reason12.get(),sd72.get(),sd82.get(),sd122.get(),sd142.get(),ad2.get()))
    
    try:
        cur.execute(" UPDATE data_base SET FULL_NAME = ? , QUALIFICATION = ? , EMAIL_ID = ? , SALARY = ? , DATE_OF_BIRTH = ? , GENDER = ? , MOBILE_NO = ? , SUBJECT1 = ? , ADDRESS1 = ? WHERE MOBILE_NO = ?",(sdd1.get(),sdd3.get(),sdd4.get(),sdd6.get(),sdd7.get(),sdd8.get(),sdd10.get(),reasonsdd55.get(),sdd11.get(),sdd10.get()))
        messagebox.showinfo("Updating","Successfully Updated")
        
    except:
        messagebox.showerror("updating error","Data not Updated")

    conn.commit()
    conn.close()

def teachersearch2(name):

    conn = sqlite3.connect("staff")
    corr = conn.cursor()
    
    #print(name)

    #corr.execute("SELECT * FROM data_base WHERE STUDENT_NAME = ? OR ADMISSION_NUMBER = ?", (name,admnum))
    #corr.execute("SELECT * FROM data_base WHERE ADMISSION_NUMBER = ?", admnum)
    a=0
    corr.execute('''SELECT * FROM data_base''')
    rows = corr.fetchall()
    for row in rows:
        if row[0] == name:
            row1 = row
            a = a+1
    if a == 0:
        messagebox.showerror("Error in Searching","The given name is wrong")
    #print(row1)
    return row1
    
    conn.close()
def teachersearch():
    for i in student_table1.get_children():
        student_table1.delete(i)
    student_table1.insert('',END,values='')
    row = teachersearch2(sdd1.get())
        #print(row)
    student_table1.insert('',END,values=(row[0],row[6],row[7]))
                    
def hi2(e):
    try:
        row = teachersearch2(sdd1.get())
        sdd1.set(row[0])
        sdd3.set(row[1])
        sdd4.set(row[2])
        sdd6.set(row[3])
        sdd7.set(row[4])
        sdd8.set(row[5])
        sdd10.set(row[6])
        reasonsdd55.set(row[7])
        sdd11.set(row[8])
    except IndexError:
        pass



def staff(window1):
    window3 = Toplevel(window1)
    window3.geometry("1216x660+306+124")
    window3.title("Staff Management")
    global sdd1,sdd3,sdd4,sdd6,sdd7,sdd8,sdd10,sdd11,reasonsdd55
    def new_staff():
        for widget in window3.winfo_children():
            widget.destroy()
        global sdd1,sdd3,sdd4,sdd6,sdd7,sdd8,sdd10,sdd11,reasonsdd55
        Button(window3,text = "New Staff",command = lambda: new_staff()).place(x=10,y=5)
        Button(window3,text = "Staff Info Search",command = lambda: staff_info()).place(x=90,y=5)
        Label(window3,text="New Staff",font = ("times new roman",20,"bold"),relief = "solid",bg="white",width = 30).pack()

        Label(window3,text = "Full Name",bg='white',fg='black').place(x=50,y=100)
        #Label(window3,text = "Last Name",bg='white',fg='black').place(x=500,y=100)
        Label(window3,text = "Qualification",bg='white',fg='black').place(x=50,y=150)
        Label(window3,text = "Email Address",bg='white',fg='black').place(x=500,y=150)
        Label(window3,text = "Subject",bg='white',fg='black').place(x=50,y=200)
        Label(window3,text = "Salary",bg='white',fg='black').place(x=500,y=200)
        Label(window3,text = "Date of Birth (DD/MM/YY)",bg='white',fg='black').place(x=50,y=250)
        Label(window3,text = "Gender",bg='white',fg='black').place(x=500,y=250)
        #Label(window3,text = "Course",bg='white',fg='black').place(x=50,y=300)
        
        Label(window3,text = "Phone Number",bg='white',fg='black').place(x=50,y=350)
        
        Label(window3,text = "Address",bg='white',fg='black').place(x=50,y=400)
        
        sdd1=StringVar()
        #sdd2=StringVar()
        sdd3=StringVar()
        sdd4=StringVar()
        #sd5=StringVar()
        sdd6=StringVar()
        sdd7=StringVar()
        sdd8=StringVar()
        #sd9=StringVar()
        sdd10=StringVar()
        sdd11=StringVar()
        
        Entry(window3,textvar=sdd1,width= 30).place(x=230,y=100)
        #Entry(window3,textvar=sdd2,width= 30).place(x=680,y=100)
        Entry(window3,textvar=sdd3,width= 30).place(x=230,y=150)
        Entry(window3,textvar=sdd4,width= 30).place(x=680,y=150)
        #Entry(window3,textvar=sd5,width= 30).place(x=230,y=200)
        #listsdd55=["Maths","Physics","Chemistry"]
        file2 = open("Subject.txt","r")
        file2_data = file2.read()
        listsdd55=file2_data.split('\n')
        #list11=["Inter 1st Year","Inter 2nd Year"]
        file2.close()
        reasonsdd55=StringVar()               
        reasonsdd55=ttk.Combobox(window3,value=listsdd55,width=30)
        reasonsdd55.set("Choose Subject")
        reasonsdd55.place(x=230,y=200)



        Entry(window3,textvar=sdd6,width= 30).place(x=680,y=200)
        Entry(window3,textvar=sdd7,width= 30).place(x=230,y=250)
        #sd7 = Calendar(window2,selectmode = 'day',cursor = 'hand1',year=2021,month = 2,day=5)
        #sd7.place(x=230,y=250)

        #Entry(window2,textvar=sd8,width= 30).place(x=680,y=250)
        r1=Radiobutton(window3,text="Male",variable = sdd8,value = 'Male',bg='white').place(x=680,y=250)
        r2=Radiobutton(window3,text="Female",variable = sdd8,value = 'Female',bg='white').place(x=760,y=250)
        #Entry(window3,textvar=sd9,width=30).place(x=230,y=300)
        #listsdd56=[]
        #reasonsdd56=StringVar()               
        #reasonsdd56=ttk.Combobox(window3,value=listsdd56,width=30)
        #reasonsdd56.set("Choose Course")
        #reasonsdd56.place(x=230,y=300)


        Entry(window3,textvar=sdd10,width= 30).place(x=230,y=350)
        
        address_sdd = Entry(window3,textvar=sdd11,width=80).place(x=230,y=400,height=100)
        
        Button(window3,text="Save",command = lambda: teachersave()).place(x=230,y=600)
        Button(window3,text = "Upload").place(x=1050,y=400)
        image2=Image.open('image2.png')
        photo2=ImageTk.PhotoImage(image2)
        lab1=Label(window3,image=photo2)
        lab1.config(height=225)
        lab1.place(x=940,y=150)

        
    def staff_info():
        for widget in window3.winfo_children():
            widget.destroy()
        global sdd1,sdd3,sdd4,sdd6,sdd7,sdd8,sdd10,sdd11,reasonsdd55,student_table1
        Button(window3,text = "New Staff",command = lambda: new_staff()).place(x=10,y=5)
        Button(window3,text = "Staff Info Search",command = lambda: staff_info()).place(x=90,y=5)
        Label(window3,text="Staff Info Search",font = ("times new roman",20,"bold"),relief = "solid",bg="white",width = 30).pack()

        Label(window3,text = "Full Name",bg='white',fg='black').place(x=50,y=100)
        #Label(window3,text = "Last Name",bg='white',fg='black').place(x=500,y=100)
        Label(window3,text = "Qualification",bg='white',fg='black').place(x=50,y=150)
        Label(window3,text = "Email Address",bg='white',fg='black').place(x=500,y=150)
        Label(window3,text = "Subject",bg='white',fg='black').place(x=50,y=200)
        Label(window3,text = "Salary",bg='white',fg='black').place(x=500,y=200)
        Label(window3,text = "Date of Birth (DD/MM/YY)",bg='white',fg='black').place(x=50,y=250)
        Label(window3,text = "Gender",bg='white',fg='black').place(x=500,y=250)
        #Label(window3,text = "Course",bg='white',fg='black').place(x=50,y=300)
        
        Label(window3,text = "Phone Number",bg='white',fg='black').place(x=50,y=350)
        
        Label(window3,text = "Address",bg='white',fg='black').place(x=50,y=400)
        
        sdd1=StringVar()
        #sd2=StringVar()
        sdd3=StringVar()
        sdd4=StringVar()
        #sd5=StringVar()
        sdd6=StringVar()
        sdd7=StringVar()
        sdd8=StringVar()
        #sd9=StringVar()
        sdd10=StringVar()
        sdd11=StringVar()
        
        Entry(window3,textvar=sdd1,width= 30).place(x=230,y=100)
        #Entry(window3,textvar=sd2,width= 30).place(x=680,y=100)
        Entry(window3,textvar=sdd3,width= 30).place(x=230,y=150)
        Entry(window3,textvar=sdd4,width= 30).place(x=680,y=150)
        #Entry(window3,textvar=sd5,width= 30).place(x=230,y=200)
        #listsdd55=["Maths","Physics","Chemistry"]
        file2 = open("Subject.txt","r")
        file2_data = file2.read()
        listsdd55=file2_data.split('\n')
        #list11=["Inter 1st Year","Inter 2nd Year"]
        file2.close()
        reasonsdd55=StringVar()               
        reasonsdd55=ttk.Combobox(window3,value=listsdd55,width=30)
        reasonsdd55.set("Choose Subject")
        reasonsdd55.place(x=230,y=200)



        Entry(window3,textvar=sdd6,width= 30).place(x=680,y=200)
        Entry(window3,textvar=sdd7,width= 30).place(x=230,y=250)
        #sd7 = Calendar(window2,selectmode = 'day',cursor = 'hand1',year=2021,month = 2,day=5)
        #sd7.place(x=230,y=250)

        #Entry(window3,textvar=sdd8,width= 30).place(x=680,y=250)
        listgender = ["Male","Female"]
        #sdd8=StringVar()
        sdd8=ttk.Combobox(window3,value=listgender,width=30)
        sdd8.set("Choose Gender")
        sdd8.place(x=680,y=250)
        #r1=Radiobutton(window3,text="Male",variable = sd8,value = 'Male',bg='white').place(x=680,y=250)
        #r2=Radiobutton(window3,text="Female",variable = sd8,value = 'Female',bg='white').place(x=760,y=250)
        #Entry(window3,textvar=sd9,width=30).place(x=230,y=300)
        #list56=[]
        #reason56=StringVar()               
        #reason56=ttk.Combobox(window3,value=list56,width=30)
        #reason56.set("Choose Course")
        #reason56.place(x=230,y=300)


        Entry(window3,textvar=sdd10,width= 30).place(x=230,y=350)
        
        #sdd11 = Text(window3,width = 80,height = 6).place(x=230,y=400)
        Entry(window3,textvar=sdd11,width=80).place(x=230,y=400,height=100)
        
        
        
        Button(window3,text="Update",command = lambda: updatedteacher()).place(x=960,y=500)
        Button(window3,text = "Delete",command = lambda: deleteteacher()).place(x=1020,y=500)
        Button(window3,text="Search",command = lambda: teachersearch()).place(x=1080,y=500)

        Button(window3,text = "Upload").place(x=1050,y=400)
        image2=Image.open('image2.png')
        photo2=ImageTk.PhotoImage(image2)
        lab1=Label(window3,image=photo2)
        lab1.config(height=225)
        lab1.place(x=940,y=150)

        student_table1=ttk.Treeview(window3,columns=("Name","Phone No","Subject"))
        Scroll = Scrollbar(student_table1)
        Scroll.pack(side=RIGHT,  fill=Y)
        Scroll.config(command=student_table1.yview)
        student_table1.config(yscrollcommand=Scroll.set)
        #scroll_y.config(command=student_table.yview)
        #student_table.config(yscroll=window20.set)
        student_table1.heading("Name",text="Name")
        student_table1.heading("Phone No",text="Phone No")
        student_table1.heading("Subject",text="Subject")
        student_table1['show']='headings'
        student_table1.pack(side = BOTTOM,fill = X)
        student_table1.bind("<Double-1>", hi2)


        

    Button(window3,text = "New Staff",command = lambda: new_staff()).place(x=10,y=5)
    Button(window3,text = "Staff Info Search",command = lambda: staff_info()).place(x=90,y=5)
    Label(window3,text="New Staff",font = ("times new roman",20,"bold"),relief = "solid",bg="white",width = 30).pack()

    Label(window3,text = "Full Name",bg='white',fg='black').place(x=50,y=100)
    #Label(window3,text = "Last Name",bg='white',fg='black').place(x=500,y=100)
    Label(window3,text = "Qualification",bg='white',fg='black').place(x=50,y=150)
    Label(window3,text = "Email Address",bg='white',fg='black').place(x=500,y=150)
    Label(window3,text = "Subject",bg='white',fg='black').place(x=50,y=200)
    Label(window3,text = "Salary",bg='white',fg='black').place(x=500,y=200)
    Label(window3,text = "Date of Birth (DD/MM/YY)",bg='white',fg='black').place(x=50,y=250)
    Label(window3,text = "Gender",bg='white',fg='black').place(x=500,y=250)
    #Label(window3,text = "Course",bg='white',fg='black').place(x=50,y=300)
    
    Label(window3,text = "Phone Number",bg='white',fg='black').place(x=50,y=350)
    
    Label(window3,text = "Address",bg='white',fg='black').place(x=50,y=400)
    
    sdd1=StringVar()
    #sdd2=StringVar()
    sdd3=StringVar()
    sdd4=StringVar()
    #sd5=StringVar()
    sdd6=StringVar()
    sdd7=StringVar()
    sdd8=StringVar()
    #sd9=StringVar()
    sdd10=StringVar()
    sdd11=StringVar()
    
    Entry(window3,textvar=sdd1,width= 30).place(x=230,y=100)
    #Entry(window3,textvar=sdd2,width= 30).place(x=680,y=100)
    Entry(window3,textvar=sdd3,width= 30).place(x=230,y=150)
    Entry(window3,textvar=sdd4,width= 30).place(x=680,y=150)
    #Entry(window3,textvar=sd5,width= 30).place(x=230,y=200)
    #listsdd55=["Maths","Physics","Chemistry"]
    file2 = open("Subject.txt","r")
    file2_data = file2.read()
    listsdd55=file2_data.split('\n')
    #list11=["Inter 1st Year","Inter 2nd Year"]
    file2.close()
    reasonsdd55=StringVar()               
    reasonsdd55=ttk.Combobox(window3,value=listsdd55,width=30)
    reasonsdd55.set("Choose Subject")
    reasonsdd55.place(x=230,y=200)



    Entry(window3,textvar=sdd6,width= 30).place(x=680,y=200)
    Entry(window3,textvar=sdd7,width= 30).place(x=230,y=250)
    #sd7 = Calendar(window2,selectmode = 'day',cursor = 'hand1',year=2021,month = 2,day=5)
    #sd7.place(x=230,y=250)

    #Entry(window2,textvar=sd8,width= 30).place(x=680,y=250)
    r1=Radiobutton(window3,text="Male",variable = sdd8,value = 'Male',bg='white').place(x=680,y=250)
    r2=Radiobutton(window3,text="Female",variable = sdd8,value = 'Female',bg='white').place(x=760,y=250)
    #Entry(window3,textvar=sd9,width=30).place(x=230,y=300)
    #listsdd56=["Maths","Physics","Chemistry"]
    #reasonsdd56=StringVar()               
    #reasonsdd56=ttk.Combobox(window3,value=listsdd56,width=30)
    #reasonsdd56.set("Choose Course")
    #reasonsdd56.place(x=230,y=300)


    Entry(window3,textvar=sdd10,width= 30).place(x=230,y=350)
    
    address_sdd = Entry(window3,textvar=sdd11,width=80).place(x=230,y=400,height=100)
    
    Button(window3,text="Save",command = lambda: teachersave()).place(x=230,y=600)
    Button(window3,text = "Upload").place(x=1050,y=400)
    image2=Image.open('image2.png')
    photo2=ImageTk.PhotoImage(image2)
    lab1=Label(window3,image=photo2)
    lab1.config(height=225)
    lab1.place(x=940,y=150)


    window3.mainloop()
def save_exam_data():
    name = md1.get()
    admnum = md2.get()
    marob = md3.get()
    totmar = md4.get()
    per = md5.get()
    course = cour.get()
    section = sect.get()
    description = des.get()
    conn = sqlite3.connect("exam_marks")
    conn.execute('''CREATE TABLE IF NOT EXISTS data_base(FULL_NAME TEXT , ADMISSION_NO TEXT , MARKS_OBTAINED TEXT , TOTAL_MARKS TEXT , PERCENTAGE TEXT , DESCRIPTION TEXT , COURSE TEXT , SECTION TEXT )''')
    
    

    conn.execute('''INSERT INTO data_base(FULL_NAME,ADMISSION_NO,MARKS_OBTAINED,TOTAL_MARKS,PERCENTAGE,DESCRIPTION,COURSE,SECTION)VALUES(?,?,?,?,?,?,?,?)''', (name,admnum,marob,totmar,per,description,course,section))
    
    conn.commit()
    #conn.close()
    messagebox.showinfo("Exam Data","New Marks Data Succesfully Created")
def search_exam_data1(name,des):
    conn = sqlite3.connect("exam_marks")
    corr = conn.cursor()
    

    #corr.execute("SELECT * FROM data_base WHERE STUDENT_NAME = ? OR ADMISSION_NUMBER = ?", (name,admnum))
    #corr.execute("SELECT * FROM data_base WHERE ADMISSION_NUMBER = ?", admnum)
    try:
        corr.execute("SELECT * FROM data_base WHERE FULL_NAME = ? AND DESCRIPTION = ?", (name,des,))
    except:
        messagebox.showerror("Error in Searching","The given details are wrong")
    rows = corr.fetchall()
    return rows
    
    conn.close()

def search_exam_data():
    name = md1.get()
    description = des.get()
    for i in student_table_exam1.get_children():
        student_table_exam1.delete(i)
    student_table_exam1.insert('',END,values='')
    row = search_exam_data1(name,description)
    row = row[0]
    #print(row)
    student_table_exam1.insert('',END,values=(row[1],row[0],row[7],row[6]))
def withe(e):
    try:
        row = search_exam_data1(md1.get(),des.get())
        row = row[0]
        md2.set(row[1])
        md3.set(row[2])
        md4.set(row[3])
        md5.set(row[4])
        des.set(row[5])
        cour.set(row[6])
        sect.set(row[7])
    except IndexError:
        pass

def update_exam_data():
    name = md1.get()
    admnum = md2.get()
    marob = md3.get()
    totmar = md4.get()
    per = md5.get()
    course = cour.get()
    section = sect.get()
    description = des.get()
    conn = sqlite3.connect("exam_marks")
    corr = conn.cursor()
    try:
        corr.execute(" UPDATE data_base SET FULL_NAME = ? , ADMISSION_NO = ? , MARKS_OBTAINED = ? , TOTAL_MARKS = ? , PERCENTAGE = ? , DESCRIPTION = ? , COURSE = ? , SECTION = ? WHERE FULL_NAME = ? AND DESCRIPTION = ?",(name,admnum,marob,totmar,per,description,course,section,name,description,))
        messagebox.showinfo("Updating","Successfully Updated")
        
    except:
        messagebox.showerror("updating error","Data not Updated")

    conn.commit()
    conn.close()
    
def delete_exam_data():
    conn = sqlite3.connect("exam_marks")
    corr = conn.cursor()
    try:
        corr.execute("DELETE FROM data_base WHERE FULL_NAME = ? AND DESCRIPTION = ?", (md1.get(),des.get(),))
        messagebox.showinfo("Deleting","Data Deleted Successfully")
    except:
        messagebox.showerror("deleting error","Data not Deleted")

    conn.commit()
    conn.close()

def search_the_marks():
    if ed51.get() == "" or ed51.get()==" ":#Description
        conn = sqlite3.connect("exam_marks")
        corr = conn.cursor()
        try:
            corr.execute("SELECT * FROM data_base WHERE DESCRIPTION = ?",(ed52.get(),))
            rows = corr.fetchall()
            conn.commit()
            conn.close()
            for i in student_table_exam2.get_children():
                student_table_exam2.delete(i)
            for row in rows:

                student_table_exam2.insert('',END,values=(row[1],row[0],row[2],row[3],row[4],row[5]))

        except:
            messagebox.showerror("Error","Error in searching via Description")
    else:
        conn = sqlite3.connect("exam_marks")
        corr = conn.cursor()
        try:
            corr.execute("SELECT * FROM data_base WHERE FULL_NAME = ?",(ed51.get(),))
            rows = corr.fetchall()
            conn.commit()
            conn.close()
            for i in student_table_exam2.get_children():
                student_table_exam2.delete(i)
            for row in rows:

                student_table_exam2.insert('',END,values=(row[1],row[0],row[2],row[3],row[4],row[5]))

        except:
            messagebox.showerror("Error","Error in searching via Description")

def search_via_desec():
    conn = sqlite3.connect("exam_marks")
    corr = conn.cursor()
    try:
        corr.execute("SELECT * FROM data_base WHERE DESCRIPTION = ? AND SECTION = ?",(ed52.get(),ed53.get(),))
        rows = corr.fetchall()
        conn.commit()
        conn.close()
        for i in student_table_exam2.get_children():
            student_table_exam2.delete(i)
        for row in rows:

            student_table_exam2.insert('',END,values=(row[1],row[0],row[2],row[3],row[4],row[5]))

    except:
        messagebox.showerror("Error","Error in searching via Description")


    

def exam(window1):
    window4 = Toplevel(window1)
    window4.geometry("1216x660+306+124")
    window4.title("Exam Management")
    global des,cour,sect,md1, md2, md3, md4, md5, student_table_exam1
    def result():
        for widget in window4.winfo_children():
            widget.destroy()
        global des,cour,sect,md1, md2, md3, md4, md5, student_table_exam1
        Button(window4,text = "Result",command = lambda: result()).place(x=10,y=5)
        Button(window4,text = "Data",command = lambda: data()).place(x=90,y=5)
        Label(window4,text="Result",font = ("times new roman",20,"bold"),relief = "solid",bg="white",width = 30).pack()
        Label(window4,text = "Name",bg='white',fg='black').place(x=50,y=100)
        
        Label(window4,text = "Admission Number",bg='white',fg='black').place(x=50,y=150)
        Label(window4,text = "Marks Obtained",bg='white',fg='black').place(x=50,y=200)
        Label(window4,text = "Total Marks",bg='white',fg='black').place(x=50,y=250)
        Label(window4,text = "Percentage",bg='white',fg='black').place(x=50,y=300)
        Label(window4,text = "Description",bg="white",fg='black').place(x=500,y=100)
        #des = StringVar()
        #Entry(window4,textvar = des,width = 30).place(x = 680,y=100)

        des=StringVar()
        file22 = open("Description.txt","r")
        file22_data = file22.read()
        listdesc=file22_data.split('\n')
        #list11=["Inter 1st Year","Inter 2nd Year"]
        file22.close()
                    
        des=ttk.Combobox(window4,value=listdesc,width=30)
        des.set("Choose Description")
        des.place(x=680,y=100)

        Label(window4,text = "Course",bg="white",fg="black").place(x=500,y=150)
        #cour = StringVar()
        #Entry(window4,textvar = cour,width = 30).place(x = 680,y = 150)

        cour=StringVar()
        file2 = open("Course.txt","r")
        file2_data = file2.read()
        list11=file2_data.split('\n')
        #list11=["Inter 1st Year","Inter 2nd Year"]
        file2.close()
                    
        cour=ttk.Combobox(window4,value=list11,width=30)
        cour.set("Choose Course")
        cour.place(x=680,y=150)

        Label(window4,text = "section",bg="white",fg = "black").place(x=500,y=200)
        #sect = StringVar()
        #Entry(window4,textvar = sect,width = 30).place(x=680,y=200)

        sect=StringVar()
        file1 = open("Section.txt","r")
        file1_data = file1.read()
        list12 = file1_data.split('\n')
        #list12=['A','B','C']
        file1.close()
                    #droplist11=OptionMenu(window11,reason,*list11)
                    #reason.set("Select Reason")
                    #droplist11.config(width=15)
                    #droplist11.place(x=500,y=196)
        sect=ttk.Combobox(window4,value=list12,width=30)
        sect.set("Choose Section")
        sect.place(x=680,y=200)


        md1 = StringVar()
        md2 = StringVar()
        md3 = StringVar()
        md4 = StringVar()
        md5 = StringVar()

        Entry(window4,textvar=md1,width= 30).place(x=230,y=100)
        
        Entry(window4,textvar=md2,width= 30).place(x=230,y=150)
        Entry(window4,textvar=md3,width= 30).place(x=230,y=200)
        Entry(window4,textvar=md4,width= 30).place(x=230,y=250)
        Entry(window4,textvar=md5,width= 30).place(x=230,y=300)
        Button(window4,text="Search",command = lambda: search_exam_data()).place(x=430,y=100)
        Button(window4,text="Save",command = lambda: save_exam_data()).place(x=230,y=350)
        Button(window4,text="Delete",command = lambda: delete_exam_data()).place(x=300,y=350)
        Button(window4,text = "Update",command = lambda: update_exam_data()).place(x=370,y=350)
        student_table_exam1=ttk.Treeview(window4,columns=("Sr No","Student Name","Section","Course"))
        Scroll = Scrollbar(student_table_exam1)
        Scroll.pack(side=RIGHT,  fill=Y)
        Scroll.config(command=student_table_exam1.yview)
        student_table_exam1.config(yscrollcommand=Scroll.set)
        #scroll_y.config(command=student_table.yview)
        #student_table.config(yscroll=window20.set)
        student_table_exam1.heading("Sr No",text = "Sr No")
        student_table_exam1.heading("Student Name",text="Student Name")
        student_table_exam1.heading("Section",text="Section")
        student_table_exam1.heading("Course",text="Course")
        student_table_exam1['show']='headings'
        student_table_exam1.pack(side = BOTTOM,fill = X)
        student_table_exam1.bind("<Double-1>", withe)
    def data():
        for widget in window4.winfo_children():
            widget.destroy()
        global ed51,ed52,student_table_exam2, ed53
        Button(window4,text = "Result",command = lambda: result()).place(x=10,y=5)
        Button(window4,text = "Data",command = lambda: data()).place(x=90,y=5)
        ed51 = StringVar()
        ed52 = StringVar()
        Label(window4,text = "Student Data",font = ("times new roman",15,"bold"),bg="white").pack()
        Label(window4,text = "Search By name:").place(x=10,y=80)
        Entry(window4,textvar = ed51,width = 30).place(x=120,y=80)
        Label(window4,text = "Search By Description:").place(x=280,y = 80)
        #Entry(window4,textvar = ed52,width = 30).place(x=420,y=80)
        ed52=StringVar()
        file22 = open("Description.txt","r")
        file22_data = file22.read()
        listdesc=file22_data.split('\n')
        #list11=["Inter 1st Year","Inter 2nd Year"]
        file22.close()
                    
        ed52=ttk.Combobox(window4,value=listdesc,width=30)
        ed52.set("Choose Description")
        ed52.place(x=420,y=80)

        Button(window4,text ='search',command = lambda: search_the_marks()).place(x=650,y=76)
        ed53=StringVar()
        file1 = open("Section.txt","r")
        file1_data = file1.read()
        list12 = file1_data.split('\n')
        #list12=['A','B','C']
        file1.close()
                    #droplist11=OptionMenu(window11,reason,*list11)
                    #reason.set("Select Reason")
                    #droplist11.config(width=15)
                    #droplist11.place(x=500,y=196)
        ed53=ttk.Combobox(window4,value=list12,width=30)
        ed53.set("Choose Section")
        ed53.place(x=720,y=80)
        Button(window4,text = "Search via Desc and Sec",command = lambda: search_via_desec()).place(x=950,y=76)
        
        student_table_exam2=ttk.Treeview(window4,columns=("SERIAL NO","STUDENT NAME","Marks Obtained","Total Marks","Percentage","Description"))
        Scroll = Scrollbar(student_table_exam2)
        Scroll.pack(side=RIGHT,  fill=Y)
        Scroll.config(command=student_table_exam2.yview)
        student_table_exam2.config(yscrollcommand=Scroll.set)
        #scroll_y.config(command=student_table.yview)
        #student_table.config(yscroll=window20.set)
        student_table_exam2.heading("SERIAL NO",text="SERIAL NO")
        student_table_exam2.heading("STUDENT NAME",text="STUDENT NAME")
        student_table_exam2.heading("Marks Obtained",text="Marks Obtained")
        student_table_exam2.heading("Total Marks",text="Total Marks")
        student_table_exam2.heading("Percentage",text="Percentage")
        student_table_exam2.heading("Description",text="Description")
        student_table_exam2['show']='headings'
        student_table_exam2.pack(fill = BOTH,pady=100,expand = 1)
        
        
    Button(window4,text = "Result",command = lambda: result()).place(x=10,y=5)
    Button(window4,text = "Data",command = lambda: data()).place(x=90,y=5)
    Label(window4,text="Result",font = ("times new roman",20,"bold"),relief = "solid",bg="white",width = 30).pack()
    Label(window4,text = "Name",bg='white',fg='black').place(x=50,y=100)
    
    Label(window4,text = "Admission Number",bg='white',fg='black').place(x=50,y=150)
    Label(window4,text = "Marks Obtained",bg='white',fg='black').place(x=50,y=200)
    Label(window4,text = "Total Marks",bg='white',fg='black').place(x=50,y=250)
    Label(window4,text = "Percentage",bg='white',fg='black').place(x=50,y=300)
    Label(window4,text = "Description",bg="white",fg='black').place(x=500,y=100)
    #des = StringVar()
    #Entry(window4,textvar = des,width = 30).place(x = 680,y=100)

    des=StringVar()
    file22 = open("Description.txt","r")
    file22_data = file22.read()
    listdesc=file22_data.split('\n')
    #list11=["Inter 1st Year","Inter 2nd Year"]
    file22.close()
                
    des=ttk.Combobox(window4,value=listdesc,width=30)
    des.set("Choose Description")
    des.place(x=680,y=100)

    Label(window4,text = "Course",bg="white",fg="black").place(x=500,y=150)
    #cour = StringVar()
    #Entry(window4,textvar = cour,width = 30).place(x = 680,y = 150)

    cour=StringVar()
    file2 = open("Course.txt","r")
    file2_data = file2.read()
    list11=file2_data.split('\n')
    #list11=["Inter 1st Year","Inter 2nd Year"]
    file2.close()
                
    cour=ttk.Combobox(window4,value=list11,width=30)
    cour.set("Choose Course")
    cour.place(x=680,y=150)
    Label(window4,text = "section",bg="white",fg = "black").place(x=500,y=200)
    #sect = StringVar()
    #Entry(window4,textvar = sect,width = 30).place(x=680,y=200)

    sect=StringVar()
    file1 = open("Section.txt","r")
    file1_data = file1.read()
    list12 = file1_data.split('\n')
    #list12=['A','B','C']
    file1.close()
                #droplist11=OptionMenu(window11,reason,*list11)
                #reason.set("Select Reason")
                #droplist11.config(width=15)
                #droplist11.place(x=500,y=196)
    sect=ttk.Combobox(window4,value=list12,width=30)
    sect.set("Choose Section")
    sect.place(x=680,y=200)
    md1 = StringVar()
    md2 = StringVar()
    md3 = StringVar()
    md4 = StringVar()
    md5 = StringVar()

    Entry(window4,textvar=md1,width= 30).place(x=230,y=100)
    
    Entry(window4,textvar=md2,width= 30).place(x=230,y=150)
    Entry(window4,textvar=md3,width= 30).place(x=230,y=200)
    Entry(window4,textvar=md4,width= 30).place(x=230,y=250)
    Entry(window4,textvar=md5,width= 30).place(x=230,y=300)
    Button(window4,text="Search",command = lambda: search_exam_data()).place(x=430,y=100)
    Button(window4,text="Save",command = lambda: save_exam_data()).place(x=230,y=350)
    Button(window4,text="Delete",command = lambda: delete_exam_data()).place(x=300,y=350)
    Button(window4,text = "Update",command = lambda: update_exam_data()).place(x=370,y=350)
    student_table_exam1=ttk.Treeview(window4,columns=("Sr No","Student Name","Section","Course"))
    Scroll = Scrollbar(student_table_exam1)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=student_table_exam1.yview)
    student_table_exam1.config(yscrollcommand=Scroll.set)
    #scroll_y.config(command=student_table.yview)
    #student_table.config(yscroll=window20.set)
    student_table_exam1.heading("Sr No",text = "Sr No")
    student_table_exam1.heading("Student Name",text="Student Name")
    student_table_exam1.heading("Section",text="Section")
    student_table_exam1.heading("Course",text="Course")
    student_table_exam1['show']='headings'
    student_table_exam1.pack(side = BOTTOM,fill = X)
    student_table_exam1.bind("<Double-1>", withe)


    window4.mainloop()

def fees(window1):
    window5 = Toplevel(window1)
    window5.geometry("1216x660+306+124")
    window5.title("Fees Management")
    def fees1():
        for widget in window5.winfo_children():
            widget.destroy()
        Button(window5,text = "Fees",command = lambda: fees1()).place(x=10,y=5)
        Button(window5,text = "Data",command = lambda: data()).place(x=90,y=5)
        Label(window5,text="Fees",font = ("times new roman",20,"bold"),relief = "solid",bg="white",width = 30).pack()
        Label(window5,text = "Search By Name",bg='white',fg='black').place(x=50,y=100)
        
        Label(window5,text = "Admission Number",bg='white',fg='black').place(x=500,y=100)
        Label(window5,text = "Paid Date(DD/MM/YY)",bg="white",fg="black").place(x=500,y=250)
        fd7=StringVar()
        Entry(window5,textvar=fd7,width=30).place(x=680,y=250)
        Label(window5,text = "Total Fees",bg='white',fg='black').place(x=50,y=150)
        Label(window5,text = "Year",bg='white',fg='black').place(x=50,y=200)
        Label(window5,text = "Paid",bg='white',fg='black').place(x=50,y=250)
        Label(window5,text = "Mode Of Payment",fg="black",bg="white").place(x=50,y=300)
        Label(window5,text = "Due Amount",fg="black",bg="white").place(x=50,y=350)
        fd1 = StringVar()
        fd2 = StringVar()
        fd3 = StringVar()
        fd4 = StringVar()
        fd5 = StringVar()
        fd6 = StringVar()
        Entry(window5,textvar=fd1,width= 30).place(x=230,y=100)
        
        Entry(window5,textvar=fd2,width= 30).place(x=680,y=100)
        Entry(window5,textvar=fd3,width= 30).place(x=230,y=150)
        #Entry(window5,textvar=fd4,width= 30).place(x=230,y=200)
        reason_fees=StringVar()
        list11=[1,2]
                        
        reason_fees=ttk.Combobox(window5,value=list11,width=30)
        reason_fees.set("Choose Year")
        reason_fees.place(x=230,y=200)
        pay=StringVar()
        r1=Radiobutton(window5,text="Cheque",variable = pay,value = 'Cheque',bg='white').place(x=230,y=300)
        r2=Radiobutton(window5,text="Cash",variable = pay,value = 'Cash',bg='white').place(x=310,y=300)



        Entry(window5,textvar=fd5,width= 30).place(x=230,y=250)
        Entry(window5,textvar=fd6,width = 30).place(x=230,y=350)
        Button(window5,text="Search").place(x=430,y=100)
        Button(window5,text="Save").place(x=230,y=400)
        Button(window5,text="Delete").place(x=300,y=400)
        Button(window5,text = "Update").place(x=370,y=400)
        student_table=ttk.Treeview(window5,columns=("Sr No","Student Name","Phone No","Course"))
        Scroll = Scrollbar(student_table)
        Scroll.pack(side=RIGHT,  fill=Y)
        Scroll.config(command=student_table.yview)
        student_table.config(yscrollcommand=Scroll.set)
        #scroll_y.config(command=student_table.yview)
        #student_table.config(yscroll=window20.set)
        student_table.heading("Sr No",text = "Sr No")
        student_table.heading("Student Name",text="Student Name")
        student_table.heading("Phone No",text="Phone No")
        student_table.heading("Course",text="Course")
        student_table['show']='headings'
        student_table.pack(side = BOTTOM,fill = X)
        
    def data():
        for widget in window5.winfo_children():
            widget.destroy()
        Button(window5,text = "Fees",command = lambda: fees1()).place(x=10,y=5)
        Button(window5,text = "Data",command = lambda: data()).place(x=90,y=5)
        s9 = StringVar()
        Label(window5,text = "Data",font = ("times new roman",20,"bold"),bg="white").pack()
        Label(window5,text = "Search By name:").place(x=40,y=80)
        Entry(window5,textvar = s9,width = 60).place(x=200,y=80)
        Button(window5,text ='search').place(x=620,y=76)
        
        student_table=ttk.Treeview(window5,columns=("Serial No","Student Name","Total Fees","Year","Fees Paid","Payment Date","Mode Of Payment","Fees Due"))
        Scroll = Scrollbar(student_table)
        Scroll.pack(side=RIGHT,  fill=Y)
        
        Scroll.config(command=student_table.yview)
        
        student_table.config(yscrollcommand=Scroll.set)
        
        
        #scroll_y.config(command=student_table.yview)
        #student_table.config(yscroll=window20.set)
        student_table.heading("Serial No",text="Serial No")
        student_table.heading("Student Name",text="Student Name")
        student_table.heading("Total Fees",text="Total Fees")
        student_table.heading("Year",text="Year")
        student_table.heading("Fees Paid",text="Fees Paid")
        student_table.heading("Payment Date",text="Payment Date")
        student_table.heading("Mode Of Payment",text = "Mode Of Payment")
        student_table.heading("Fees Due",text = "Fees Due")
        
        student_table.column("Serial No",width=10)
        student_table.column("Student Name",width=10)
        student_table.column("Total Fees",width=10)
        student_table.column("Year",width=10)
        student_table.column("Fees Paid",width=10)
        student_table.column("Payment Date",width=10)
        student_table.column("Mode Of Payment",width=10)
        student_table.column("Fees Due",width=10)

        student_table['show']='headings'
        student_table.pack(fill = BOTH,pady=100,expand = 1)
        
        
    
    Button(window5,text = "Fees",command = lambda: fees1()).place(x=10,y=5)
    Button(window5,text = "Data",command = lambda: data()).place(x=90,y=5)
    Label(window5,text="Fees",font = ("times new roman",20,"bold"),relief = "solid",bg="white",width = 30).pack()
    Label(window5,text = "Search By Name",bg='white',fg='black').place(x=50,y=100)
    
    Label(window5,text = "Admission Number",bg='white',fg='black').place(x=500,y=100)
    Label(window5,text = "Paid Date(DD/MM/YY)",bg="white",fg="black").place(x=500,y=250)
    fd7=StringVar()
    Entry(window5,textvar=fd7,width=30).place(x=680,y=250)
    Label(window5,text = "Total Fees",bg='white',fg='black').place(x=50,y=150)
    Label(window5,text = "Year",bg='white',fg='black').place(x=50,y=200)
    Label(window5,text = "Paid",bg='white',fg='black').place(x=50,y=250)
    Label(window5,text = "Mode Of Payment",fg="black",bg="white").place(x=50,y=300)
    Label(window5,text = "Due Amount",fg="black",bg="white").place(x=50,y=350)
    fd1 = StringVar()
    fd2 = StringVar()
    fd3 = StringVar()
    fd4 = StringVar()
    fd5 = StringVar()
    fd6 = StringVar()
    Entry(window5,textvar=fd1,width= 30).place(x=230,y=100)
    
    Entry(window5,textvar=fd2,width= 30).place(x=680,y=100)
    Entry(window5,textvar=fd3,width= 30).place(x=230,y=150)
    #Entry(window5,textvar=fd4,width= 30).place(x=230,y=200)
    reason_fees=StringVar()
    list11=[1,2]
                    
    reason_fees=ttk.Combobox(window5,value=list11,width=30)
    reason_fees.set("Choose Year")
    reason_fees.place(x=230,y=200)
    pay=StringVar()
    r1=Radiobutton(window5,text="Cheque",variable = pay,value = 'Cheque',bg='white').place(x=230,y=300)
    r2=Radiobutton(window5,text="Cash",variable = pay,value = 'Cash',bg='white').place(x=310,y=300)



    Entry(window5,textvar=fd5,width= 30).place(x=230,y=250)
    Entry(window5,textvar=fd6,width = 30).place(x=230,y=350)
    Button(window5,text="Search").place(x=430,y=100)
    Button(window5,text="Save").place(x=230,y=400)
    Button(window5,text="Delete").place(x=300,y=400)
    Button(window5,text = "Update").place(x=370,y=400)
    student_table=ttk.Treeview(window5,columns=("Sr No","Student Name","Phone No","Course"))
    Scroll = Scrollbar(student_table)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=student_table.yview)
    student_table.config(yscrollcommand=Scroll.set)
    #scroll_y.config(command=student_table.yview)
    #student_table.config(yscroll=window20.set)
    student_table.heading("Sr No",text = "Sr No")
    student_table.heading("Student Name",text="Student Name")
    student_table.heading("Phone No",text="Phone No")
    student_table.heading("Course",text="Course")
    student_table['show']='headings'
    student_table.pack(side = BOTTOM,fill = X)
    window5.mainloop()

def attendance(window1):
    window6 = Toplevel(window1)
    window6.geometry("1216x660+306+124")
    window6.title("Attendance")
    def student():
        for widget in window6.winfo_children():
            widget.destroy()
        Button(window6,text = "Student",command = lambda: student()).place(x=10,y=5)
        Button(window6,text = "Staff",command = lambda: staff()).place(x=90,y=5)
        Button(window6,text="Data",command=lambda: data()).place(x=170,y=5)
        Label(window6,text="Student Attendance",font = ("times new roman",20,"bold"),relief = "solid",bg="white",width = 30).pack()
        Label(window6,text = "Search By Name",bg='white',fg='black').place(x=50,y=100)
        
        Label(window6,text = "Admission Number",bg='white',fg='black').place(x=500,y=100)
        
        
        Label(window6,text="TO(DD/MM/YY)",bg="white",fg="black").place(x=500,y=150)
        ad8=StringVar()
        Entry(window6,textvar=ad8,width=30).place(x=680,y=150)
        Label(window6,text = "From(DD/MM/YY)",bg='white',fg='black').place(x=50,y=150)
        Label(window6,text = "Total Number Of Days",bg='white',fg='black').place(x=50,y=200)
        Label(window6,text = "Type",bg='white',fg='black').place(x=50,y=250)
        Label(window6,text = "Number Of Days Present",fg="black",bg="white").place(x=50,y=300)
        Label(window6,text = "Number Of Days Absent",fg="black",bg="white").place(x=50,y=350)
        ad1 = StringVar()
        ad2 = StringVar()
        ad3 = StringVar()
        ad7 = StringVar()
        ad5 = StringVar()
        ad6 = StringVar()
        ad9 = StringVar()
        Entry(window6,textvar=ad1,width= 30).place(x=230,y=100)
        
        Entry(window6,textvar=ad2,width= 30).place(x=680,y=100)
        Entry(window6,textvar=ad3,width= 30).place(x=230,y=150)
        #Entry(window5,textvar=fd4,width= 30).place(x=230,y=200)
        
        Entry(window6,textvar=ad7,width=30).place(x=230,y=300)
        Entry(window6,textvar=ad9,width=30).place(x=230,y=200)
        

        Entry(window6,textvar=ad5,width= 30).place(x=230,y=250)
        ad5.set("Student")
        Entry(window6,textvar=ad6,width = 30).place(x=230,y=350)
        Button(window6,text="Search").place(x=430,y=100)
        Button(window6,text="Save").place(x=230,y=400)
        Button(window6,text="Delete").place(x=300,y=400)
        Button(window6,text = "Update").place(x=370,y=400)
        student_table=ttk.Treeview(window6,columns=("Sr No","Student Name","Phone No","Course"))
        Scroll = Scrollbar(student_table)
        Scroll.pack(side=RIGHT,  fill=Y)
        Scroll.config(command=student_table.yview)
        student_table.config(yscrollcommand=Scroll.set)
        #scroll_y.config(command=student_table.yview)
        #student_table.config(yscroll=window20.set)
        student_table.heading("Sr No",text = "Sr No")
        student_table.heading("Student Name",text="Student Name")
        student_table.heading("Phone No",text="Phone No")
        student_table.heading("Course",text="Course")
        student_table['show']='headings'
        student_table.pack(side = BOTTOM,fill = X)

        
    def staff():
        for widget in window6.winfo_children():
            widget.destroy()
        Button(window6,text = "Student",command = lambda: student()).place(x=10,y=5)
        Button(window6,text = "Staff",command = lambda: staff()).place(x=90,y=5)
        Button(window6,text="Data",command=lambda: data()).place(x=170,y=5)
        Label(window6,text="Staff Attendance",font = ("times new roman",20,"bold"),relief = "solid",bg="white",width = 30).pack()
        Label(window6,text = "Search By Name",bg='white',fg='black').place(x=50,y=100)
        
        Label(window6,text = "Admission Number",bg='white',fg='black').place(x=500,y=100)
        
        
        Label(window6,text="TO(DD/MM/YY)",bg="white",fg="black").place(x=500,y=150)
        ad8=StringVar()
        Entry(window6,textvar=ad8,width=30).place(x=680,y=150)
        Label(window6,text = "From(DD/MM/YY)",bg='white',fg='black').place(x=50,y=150)
        Label(window6,text = "Total Number Of Days",bg='white',fg='black').place(x=50,y=200)
        Label(window6,text = "Type",bg='white',fg='black').place(x=50,y=250)
        Label(window6,text = "Number Of Days Present",fg="black",bg="white").place(x=50,y=300)
        Label(window6,text = "Number Of Days Absent",fg="black",bg="white").place(x=50,y=350)
        ad1 = StringVar()
        ad2 = StringVar()
        ad3 = StringVar()
        ad7 = StringVar()
        ad5 = StringVar()
        ad6 = StringVar()
        ad9 = StringVar()
        Entry(window6,textvar=ad1,width= 30).place(x=230,y=100)
        
        Entry(window6,textvar=ad2,width= 30).place(x=680,y=100)
        Entry(window6,textvar=ad3,width= 30).place(x=230,y=150)
        #Entry(window5,textvar=fd4,width= 30).place(x=230,y=200)
        
        Entry(window6,textvar=ad7,width=30).place(x=230,y=300)
        Entry(window6,textvar=ad9,width=30).place(x=230,y=200)
        

        Entry(window6,textvar=ad5,width= 30).place(x=230,y=250)
        ad5.set("Staff")
        Entry(window6,textvar=ad6,width = 30).place(x=230,y=350)
        Button(window6,text="Search").place(x=430,y=100)
        Button(window6,text="Save").place(x=230,y=400)
        Button(window6,text="Delete").place(x=300,y=400)
        Button(window6,text = "Update").place(x=370,y=400)
        student_table=ttk.Treeview(window6,columns=("Sr No","Student Name","Phone No","Course"))
        Scroll = Scrollbar(student_table)
        Scroll.pack(side=RIGHT,  fill=Y)
        Scroll.config(command=student_table.yview)
        student_table.config(yscrollcommand=Scroll.set)
        #scroll_y.config(command=student_table.yview)
        #student_table.config(yscroll=window20.set)
        student_table.heading("Sr No",text = "Sr No")
        student_table.heading("Student Name",text="Student Name")
        student_table.heading("Phone No",text="Phone No")
        student_table.heading("Course",text="Course")
        student_table['show']='headings'
        student_table.pack(side = BOTTOM,fill = X)
    def data():
        for widget in window6.winfo_children():
            widget.destroy()
        Button(window6,text = "Student",command = lambda: student()).place(x=10,y=5)
        Button(window6,text = "Staff",command = lambda: staff()).place(x=90,y=5)
        Button(window6,text="Data",command=lambda: data()).place(x=170,y=5)
        list88=["Student","Staff"]
        reason88=StringVar()               
        reason88=ttk.Combobox(window6,value=list88,width=30)
        reason88.set("Choose Type")
        reason88.place(x=100,y=50)
        Button(window6,text="Search").place(x=350,y=50)

        student_table=ttk.Treeview(window6,columns=("NAME","Attendance From","Attendance To","Present Days","Absent Days"))
        Scroll = Scrollbar(student_table)
        Scroll.pack(side=RIGHT,  fill=Y)
        Scroll.config(command=student_table.yview)
        student_table.config(yscrollcommand=Scroll.set)
        #scroll_y.config(command=student_table.yview)
        #student_table.config(yscroll=window20.set)
        student_table.heading("NAME",text="NAME")
        student_table.heading("Attendance From",text="Attendance From")
        student_table.heading("Attendance To",text="Attendance To")
        student_table.heading("Present Days",text="Present Days")
        student_table.heading("Absent Days",text="Absent Days")
        student_table['show']='headings'
        student_table.pack(fill = BOTH,pady=100,expand = 1)
        

    Button(window6,text = "Student",command = lambda: student()).place(x=10,y=5)
    Button(window6,text = "Staff",command = lambda: staff()).place(x=90,y=5)
    Button(window6,text="Data",command=lambda: data()).place(x=170,y=5)
    Label(window6,text="Student Attendance",font = ("times new roman",20,"bold"),relief = "solid",bg="white",width = 30).pack()
    Label(window6,text = "Search By Name",bg='white',fg='black').place(x=50,y=100)
    
    Label(window6,text = "Admission Number",bg='white',fg='black').place(x=500,y=100)
    
    
    Label(window6,text="TO(DD/MM/YY)",bg="white",fg="black").place(x=500,y=150)
    ad8=StringVar()
    Entry(window6,textvar=ad8,width=30).place(x=680,y=150)
    Label(window6,text = "From(DD/MM/YY)",bg='white',fg='black').place(x=50,y=150)
    Label(window6,text = "Total Number Of Days",bg='white',fg='black').place(x=50,y=200)
    Label(window6,text = "Type",bg='white',fg='black').place(x=50,y=250)
    Label(window6,text = "Number Of Days Present",fg="black",bg="white").place(x=50,y=300)
    Label(window6,text = "Number Of Days Absent",fg="black",bg="white").place(x=50,y=350)
    ad1 = StringVar()
    ad2 = StringVar()
    ad3 = StringVar()
    ad7 = StringVar()
    ad5 = StringVar()
    ad6 = StringVar()
    ad9 = StringVar()
    Entry(window6,textvar=ad1,width= 30).place(x=230,y=100)
    
    Entry(window6,textvar=ad2,width= 30).place(x=680,y=100)
    Entry(window6,textvar=ad3,width= 30).place(x=230,y=150)
    #Entry(window5,textvar=fd4,width= 30).place(x=230,y=200)
    
    Entry(window6,textvar=ad7,width=30).place(x=230,y=300)
    Entry(window6,textvar=ad9,width=30).place(x=230,y=200)
    

    Entry(window6,textvar=ad5,width= 30).place(x=230,y=250)
    ad5.set("Student")
    Entry(window6,textvar=ad6,width = 30).place(x=230,y=350)
    Button(window6,text="Search").place(x=430,y=100)
    Button(window6,text="Save").place(x=230,y=400)
    Button(window6,text="Delete").place(x=300,y=400)
    Button(window6,text = "Update").place(x=370,y=400)
    student_table=ttk.Treeview(window6,columns=("Sr No","Student Name","Phone No","Course"))
    Scroll = Scrollbar(student_table)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=student_table.yview)
    student_table.config(yscrollcommand=Scroll.set)
    #scroll_y.config(command=student_table.yview)
    #student_table.config(yscroll=window20.set)
    student_table.heading("Sr No",text = "Sr No")
    student_table.heading("Student Name",text="Student Name")
    student_table.heading("Phone No",text="Phone No")
    student_table.heading("Course",text="Course")
    student_table['show']='headings'
    student_table.pack(side = BOTTOM,fill = X)
    window6.mainloop()

def search_for_student():
    if misc1.get() == "all":

        conn = sqlite3.connect("student")
        corr = conn.cursor()
        

        #corr.execute("SELECT * FROM data_base WHERE STUDENT_NAME = ? OR ADMISSION_NUMBER = ?", (name,admnum))
        #corr.execute("SELECT * FROM data_base WHERE ADMISSION_NUMBER = ?", admnum)
        try:
            corr.execute("SELECT * FROM data_base")
        except:
            messagebox.showerror("Error in Searching","Error in Searching")
        rows = corr.fetchall()
        for i in student_table_misc1.get_children():
            student_table_misc1.delete(i)
        if len(rows)!=0:
            for row in rows:
                student_table_misc1.insert('',END,values=(row[0],row[2],row[7],row[10],row[12]))
        
        conn.close()
    elif misc1.get()=="" or misc1.get()==" ":
        if misc111.get()=="all":
            conn = sqlite3.connect("student")
            corr = conn.cursor()
            

            #corr.execute("SELECT * FROM data_base WHERE STUDENT_NAME = ? OR ADMISSION_NUMBER = ?", (name,admnum))
            #corr.execute("SELECT * FROM data_base WHERE ADMISSION_NUMBER = ?", admnum)
            try:
                corr.execute("SELECT * FROM data_base WHERE COURSE = ?", (misc11.get(),))
            except:
                messagebox.showerror("Error in Searching","The given admission number is wrong")
            rows = corr.fetchall()
            
            for i in student_table_misc1.get_children():
                student_table_misc1.delete(i)
            for row in rows:

                student_table_misc1.insert('',END,values=(row[0],row[2],row[7],row[10],row[12]))
            
            
            conn.close()
        else:
            conn = sqlite3.connect("student")
            corr = conn.cursor()
            

            #corr.execute("SELECT * FROM data_base WHERE STUDENT_NAME = ? OR ADMISSION_NUMBER = ?", (name,admnum))
            #corr.execute("SELECT * FROM data_base WHERE ADMISSION_NUMBER = ?", admnum)
            try:
                corr.execute("SELECT * FROM data_base WHERE COURSE = ? AND SECTION = ?", (misc11.get(),misc111.get(),))
            except:
                messagebox.showerror("Error in Searching","The given admission number is wrong")
            rows = corr.fetchall()
            
            for i in student_table_misc1.get_children():
                student_table_misc1.delete(i)
            for row in rows:

                student_table_misc1.insert('',END,values=(row[0],row[2],row[7],row[10],row[12]))
            
            
            conn.close()

    else:
        conn = sqlite3.connect("student")
        corr = conn.cursor()
        

        #corr.execute("SELECT * FROM data_base WHERE STUDENT_NAME = ? OR ADMISSION_NUMBER = ?", (name,admnum))
        #corr.execute("SELECT * FROM data_base WHERE ADMISSION_NUMBER = ?", admnum)
        try:
            corr.execute("SELECT * FROM data_base WHERE STUDENT_NAME = ?", (misc1.get(),))
        except:
            messagebox.showerror("Error in Searching","The given admission number is wrong")
        rows = corr.fetchall()
        
        for i in student_table_misc1.get_children():
            student_table_misc1.delete(i)
        for row in rows:

            student_table_misc1.insert('',END,values=(row[0],row[2],row[7],row[10],row[12]))
        
        
        conn.close()

def search_for_staff():
    if misc2.get() == "all":
        conn = sqlite3.connect("staff")
        corr = conn.cursor()
        

        #corr.execute("SELECT * FROM data_base WHERE STUDENT_NAME = ? OR ADMISSION_NUMBER = ?", (name,admnum))
        #corr.execute("SELECT * FROM data_base WHERE ADMISSION_NUMBER = ?", admnum)
        try:
            corr.execute("SELECT * FROM data_base")
        except:
            messagebox.showerror("Error in Searching","Error in Searching")
        rows = corr.fetchall()
        for i in student_table_misc2.get_children():
            student_table_misc2.delete(i)
        if len(rows)!=0:
            for row in rows:
                student_table_misc2.insert('',END,values=(row[0],row[1],row[7],row[6],row[2]))
        
        conn.close()
    else:
        conn = sqlite3.connect("staff")
        corr = conn.cursor()
        

        #corr.execute("SELECT * FROM data_base WHERE STUDENT_NAME = ? OR ADMISSION_NUMBER = ?", (name,admnum))
        #corr.execute("SELECT * FROM data_base WHERE ADMISSION_NUMBER = ?", admnum)
        try:
            corr.execute("SELECT * FROM data_base WHERE FULL_NAME = ?", (misc2.get(),))
        except:
            messagebox.showerror("Error in Searching","The given admission number is wrong")
        rows = corr.fetchall()
        
        for i in student_table_misc2.get_children():
            student_table_misc2.delete(i)
        for row in rows:

            student_table_misc2.insert('',END,values=(row[0],row[1],row[7],row[6],row[2]))
        
        
        conn.close()



    




def miscellaneous(window1):
    window7 = Toplevel(window1)
    window7.geometry("1216x660+306+124")
    window7.title("Miscellaneous")
    def student_data():
        for widget in window7.winfo_children():
            widget.destroy()
        global misc1,student_table_misc1,misc11,misc111
        menu = Menu(window7)
        window7.config(menu = menu)
        submenu1=Menu(window7)
        menu.add_cascade(label = "Student Data",menu=submenu1)
        submenu1.add_command(label = "Student Data",command = lambda: student_data())
        submenu2=Menu(window7)
        menu.add_cascade(label = "Staff Data",menu=submenu2)
        submenu2.add_command(label = "Staff Data",command = lambda: staff_data())
        submenu3=Menu(window7)
        menu.add_cascade(label = "Add Course",menu=submenu3)
        submenu3.add_command(label = "Add Course",command = lambda: add_course())
        submenu4=Menu(window7)
        menu.add_cascade(label = "Add Section",menu=submenu4)
        submenu4.add_command(label = "Add Section",command = lambda: add_section())
        submenu5=Menu(window7)
        menu.add_cascade(label = "Add Subject",menu=submenu5)
        submenu5.add_command(label = "Add Subject",command = lambda: add_subject())

        misc1 = StringVar()
        Label(window7,text = "Student Data",font = ("times new roman",15,"bold"),bg="white").pack()
        Label(window7,text = "Search By name:").place(x=10,y=80)
        Entry(window7,textvar = misc1,width = 30).place(x=120,y=80)
        Label(window7,text = "Search By Course:").place(x=310,y=80)#420
        misc11=StringVar()
        file2 = open("Course.txt","r")
        file2_data = file2.read()
        list11=file2_data.split('\n')
        #list11=["Inter 1st Year","Inter 2nd Year"]
        file2.close()
                    
        misc11=ttk.Combobox(window7,value=list11,width=30)
        misc11.set("Choose Course")
        misc11.place(x=420,y=80)


        misc111=StringVar()
        file1 = open("Section.txt","r")
        file1_data = file1.read()
        list12 = file1_data.split('\n')
        list12.append("all")
        #list12=['A','B','C']
        file1.close()
                    #droplist11=OptionMenu(window11,reason,*list11)
                    #reason.set("Select Reason")
                    #droplist11.config(width=15)
                    #droplist11.place(x=500,y=196)
        misc111=ttk.Combobox(window7,value=list12,width=30)
        misc111.set("Choose Section")
        misc111.place(x=720,y=80)

        Button(window7,text ='search',command = lambda: search_for_student()).place(x=950,y=76)
        
        student_table_misc1=ttk.Treeview(window7,columns=("SERIAL NO","STUDENT NAME","PHONE","COURSE","D.O.B"))
        Scroll = Scrollbar(student_table_misc1)
        Scroll.pack(side=RIGHT,  fill=Y)
        Scroll.config(command=student_table_misc1.yview)
        student_table_misc1.config(yscrollcommand=Scroll.set)
        #scroll_y.config(command=student_table.yview)
        #student_table.config(yscroll=window20.set)
        student_table_misc1.heading("SERIAL NO",text="SERIAL NO")
        student_table_misc1.heading("STUDENT NAME",text="STUDENT NAME")
        student_table_misc1.heading("PHONE",text="PHONE")
        student_table_misc1.heading("COURSE",text="COURSE")
        student_table_misc1.heading("D.O.B",text="D.O.B")
        student_table_misc1['show']='headings'
        student_table_misc1.pack(fill = BOTH,pady=100,expand = 1)
       
        #dbase=sqlite3.connect(my_data)
        #cursor=dbase.cursor()
        #data=cursor.execute(''' SELECT DATE,PARTICULARS,WITHDRAWLS,DEPOSITS,BALANCE FROM data_base''')
        #x=data.fetchall()
        #if len(x)!=0:
        #    for row in x:
        #        student_table.insert('',END,values=row)
        #    dbase.commit()
        #dbase.close()


        
                

    def staff_data():
        for widget in window7.winfo_children():
            widget.destroy()
        global misc2,student_table_misc2
        menu = Menu(window7)
        window7.config(menu = menu)
        submenu1=Menu(window7)
        menu.add_cascade(label = "Student Data",menu=submenu1)
        submenu1.add_command(label = "Student Data",command = lambda: student_data())
        submenu2=Menu(window7)
        menu.add_cascade(label = "Staff Data",menu=submenu2)
        submenu2.add_command(label = "Staff Data",command = lambda: staff_data())
        submenu3=Menu(window7)
        menu.add_cascade(label = "Add Course",menu=submenu3)
        submenu3.add_command(label = "Add Course",command = lambda: add_course())
        submenu4=Menu(window7)
        menu.add_cascade(label = "Add Section",menu=submenu4)
        submenu4.add_command(label = "Add Section",command = lambda: add_section())
        submenu5=Menu(window7)
        menu.add_cascade(label = "Add Subject",menu=submenu5)
        submenu5.add_command(label = "Add Subject",command = lambda: add_subject())

       
        misc2 = StringVar()
        Label(window7,text = "Staff Data",font = ("times new roman",15,"bold"),bg="white").pack()
        Label(window7,text = "Search By name:").place(x=40,y=80)
        Entry(window7,textvar = misc2,width = 60).place(x=200,y=80)
        Button(window7,text ='search',command = lambda: search_for_staff()).place(x=620,y=76)
        
        student_table_misc2=ttk.Treeview(window7,columns=("NAME","QUALIFICATION","SUBJECT","PHONE NUMBER","EMAIL ADDRESS"))
        Scroll = Scrollbar(student_table_misc2)
        Scroll.pack(side=RIGHT,  fill=Y)
        Scroll.config(command=student_table_misc2.yview)
        student_table_misc2.config(yscrollcommand=Scroll.set)
        #scroll_y.config(command=student_table.yview)
        #student_table.config(yscroll=window20.set)
        student_table_misc2.heading("NAME",text="NAME")
        student_table_misc2.heading("QUALIFICATION",text="QUALIFICATION")
        student_table_misc2.heading("SUBJECT",text="SUBJECT")
        student_table_misc2.heading("PHONE NUMBER",text="PHONE NUMBER")
        student_table_misc2.heading("EMAIL ADDRESS",text="EMAIL ADDRESS")
        student_table_misc2['show']='headings'
        student_table_misc2.pack(fill = BOTH,pady=100,expand = 1)

    def save_the_course():
        file5=open("Course.txt","a")
        file5.write( str(course1.get())+'\n')
        file5.close()
        messagebox.showinfo("Course","Course Added Succesfully")
    def delete_the_course():
        file6 = open("Course.txt","r+")
        file6_data = file6.read()
        courses = file6_data.split('\n')
        if str(course1.get()) in courses:
            i = courses.index(str(course1.get()))
            del courses[i]
            file6.close()
            file7 = open("Course.txt","w+")
            for value in courses:
                file7.write(value+'\n')
            file7.close()
            messagebox.showinfo("Courses","Course deleted successfully")
        else:
            messagebox.showerror("Courses","Course not found")

    def add_course():
        for widget in window7.winfo_children():
            widget.destroy()
        global course1
        menu = Menu(window7)
        window7.config(menu = menu)
        submenu1=Menu(window7)
        menu.add_cascade(label = "Student Data",menu=submenu1)
        submenu1.add_command(label = "Student Data",command = lambda: student_data())
        submenu2=Menu(window7)
        menu.add_cascade(label = "Staff Data",menu=submenu2)
        submenu2.add_command(label = "Staff Data",command = lambda: staff_data())
        submenu3=Menu(window7)
        menu.add_cascade(label = "Add Course",menu=submenu3)
        submenu3.add_command(label = "Add Course",command = lambda: add_course())
        submenu4=Menu(window7)
        menu.add_cascade(label = "Add Section",menu=submenu4)
        submenu4.add_command(label = "Add Section",command = lambda: add_section())
        submenu5=Menu(window7)
        menu.add_cascade(label = "Add Subject",menu=submenu5)
        submenu5.add_command(label = "Add Subject",command = lambda: add_subject())

        

        course1 = StringVar()
        Label(window7,text = "Add Course",font = ("times new roman",15,"bold"),bg="white").pack()
        Label(window7,text = "Course:").place(x=50,y=100)
        Entry(window7,textvar = course1,width = 30).place(x=200,y=100)
        Button(window7,text = "Save",width = 10,command = lambda: save_the_course()).place(x=200,y=150)
        Button(window7,text = 'Delete',width = 10,command = lambda: delete_the_course()).place(x=305,y=150)
    def save_section():
        file5=open("Section.txt","a")
        file5.write( str(sec1.get())+'\n')
        file5.close()
        messagebox.showinfo("Section","Section Added Succesfully")
    def delete_section():
        file6 = open("Section.txt","r+")
        file6_data = file6.read()
        courses = file6_data.split('\n')
        if str(sec1.get()) in courses:
            i = courses.index(str(sec1.get()))
            del courses[i]
            file6.close()
            file7 = open("Section.txt","w+")
            for value in courses:
                file7.write(value+'\n')
            file7.close()
            messagebox.showinfo("Section","Section deleted successfully")
        else:
            messagebox.showerror("Section","Section not found")


        

    def add_section():
        for widget in window7.winfo_children():
            widget.destroy()
        global sec1
        menu = Menu(window7)
        window7.config(menu = menu)
        submenu1=Menu(window7)
        menu.add_cascade(label = "Student Data",menu=submenu1)
        submenu1.add_command(label = "Student Data",command = lambda: student_data())
        submenu2=Menu(window7)
        menu.add_cascade(label = "Staff Data",menu=submenu2)
        submenu2.add_command(label = "Staff Data",command = lambda: staff_data())
        submenu3=Menu(window7)
        menu.add_cascade(label = "Add Course",menu=submenu3)
        submenu3.add_command(label = "Add Course",command = lambda: add_course())
        submenu4=Menu(window7)
        menu.add_cascade(label = "Add Section",menu=submenu4)
        submenu4.add_command(label = "Add Section",command = lambda: add_section())
        submenu5=Menu(window7)
        menu.add_cascade(label = "Add Subject",menu=submenu5)
        submenu5.add_command(label = "Add Subject",command = lambda: add_subject())

        sec1 = StringVar()
        Label(window7,text = "Add Section",font = ("times new roman",15,"bold"),bg="white").pack()
        Label(window7,text = "Section:").place(x=50,y=100)
        Entry(window7,textvar = sec1,width = 30).place(x=200,y=100)
        Button(window7,text = "Save",width = 10,command = lambda: save_section()).place(x=200,y=150)
        Button(window7,text = 'Delete',width = 10,command = lambda: delete_section()).place(x=305,y=150)
    def save_subject():
        file5=open("Subject.txt","a")
        file5.write( str(sub1.get())+'\n')
        file5.close()
        messagebox.showinfo("Subject","Subject Added Succesfully")
    def delete_subject():
        file6 = open("Subject.txt","r+")
        file6_data = file6.read()
        courses = file6_data.split('\n')
        if str(sub1.get()) in courses:
            i = courses.index(str(sub1.get()))
            del courses[i]
            file6.close()
            file7 = open("Subject.txt","w+")
            for value in courses:
                file7.write(value+'\n')
            file7.close()
            messagebox.showinfo("Subject","Subject deleted successfully")
        else:
            messagebox.showerror("Subject","Subject not found")
    def save_desc11():
        file5=open("Description.txt","a")
        file5.write( str(desc11.get())+'\n')
        file5.close()
        messagebox.showinfo("Description","Description Added Succesfully")
    def delete_desc11():
        file6 = open("Description.txt","r+")
        file6_data = file6.read()
        courses = file6_data.split('\n')
        if str(desc11.get()) in courses:
            i = courses.index(str(desc11.get()))
            del courses[i]
            file6.close()
            file7 = open("Description.txt","w+")
            for value in courses:
                file7.write(value+'\n')
            file7.close()
            messagebox.showinfo("Description","Description deleted successfully")
        else:
            messagebox.showerror("Description","Description not found")


    def add_subject():
        for widget in window7.winfo_children():
            widget.destroy()
        global sub1,desc11
        menu = Menu(window7)
        window7.config(menu = menu)
        submenu1=Menu(window7)
        menu.add_cascade(label = "Student Data",menu=submenu1)
        submenu1.add_command(label = "Student Data",command = lambda: student_data())
        submenu2=Menu(window7)
        menu.add_cascade(label = "Staff Data",menu=submenu2)
        submenu2.add_command(label = "Staff Data",command = lambda: staff_data())
        submenu3=Menu(window7)
        menu.add_cascade(label = "Add Course",menu=submenu3)
        submenu3.add_command(label = "Add Course",command = lambda: add_course())
        submenu4=Menu(window7)
        menu.add_cascade(label = "Add Section",menu=submenu4)
        submenu4.add_command(label = "Add Section",command = lambda: add_section())
        submenu5=Menu(window7)
        menu.add_cascade(label = "Add Subject",menu=submenu5)
        submenu5.add_command(label = "Add Subject",command = lambda: add_subject())
        sub1 = StringVar()
        Label(window7,text = "Add Subject and Description",font = ("times new roman",15,"bold"),bg="white").pack()
        Label(window7,text = "Subject:").place(x=50,y=100)
        Entry(window7,textvar = sub1,width = 30).place(x=200,y=100)
        Button(window7,text = "Save subject",width = 15,command = lambda: save_subject()).place(x=200,y=150)
        Button(window7,text = 'Delete subject',width = 15,command = lambda: delete_subject()).place(x=320,y=150)
        Label(window7,text = "Add Description:").place(x = 50, y = 250)
        desc11 = StringVar()
        Entry(window7,textvar = desc11,width = 30).place(x = 200,y = 250)
        Button(window7,text = "Save description",width = 15,command = lambda: save_desc11()).place(x=200,y=300)
        Button(window7,text = 'Delete description',width = 15,command = lambda: delete_desc11()).place(x=320,y=300)





    menu = Menu(window7)
    window7.config(menu = menu)
    submenu1=Menu(window7)
    menu.add_cascade(label = "Student Data",menu=submenu1)
    submenu1.add_command(label = "Student Data",command = lambda: student_data())
    submenu2=Menu(window7)
    menu.add_cascade(label = "Staff Data",menu=submenu2)
    submenu2.add_command(label = "Staff Data",command = lambda: staff_data())
    submenu3=Menu(window7)
    menu.add_cascade(label = "Add Course",menu=submenu3)
    submenu3.add_command(label = "Add Course",command = lambda: add_course())
    submenu4=Menu(window7)
    menu.add_cascade(label = "Add Section",menu=submenu4)
    submenu4.add_command(label = "Add Section",command = lambda: add_section())
    submenu5=Menu(window7)
    menu.add_cascade(label = "Add Subject",menu=submenu5)
    submenu5.add_command(label = "Add Subject",command = lambda: add_subject())

    window7.mainloop()

def login_session(window):
    window.destroy()
    window1 = Tk()
    #window1.geometry("1500x800")
    window1.state('zoomed')
    window1.title("College Management System")
    table_frame=Frame(window1,bd=4,relief=RIDGE).place(x=0,y=0,width=310,height=800)
    table_frame1 = Frame(window1,bd=4,relief = RIDGE,width=1220,height=100).place(x=311,y=0)
    image2=Image.open('image1.jpg')
    photo2=ImageTk.PhotoImage(image2)
    lab1=Label(table_frame,image=photo2)
    lab1.config(height=165)
    lab1.place(x=25,y=20)
    Button(table_frame,text="Student Management",width=20,relief="ridge",font = ("arial",16),bd=3,command = lambda: student(window1)).place(x=30,y=250)
    Button(table_frame,text="Staff Management",width=20,relief="ridge",font = ("arial",16),bd=3,command = lambda: staff(window1)).place(x=30,y=320)
    Button(table_frame,text="Exam Management",width=20,relief="ridge",font = ("arial",16),bd=3,command = lambda: exam(window1)).place(x=30,y=390)
    Button(table_frame,text="Fees Management",width=20,relief="ridge",font = ("arial",16),bd=3,command = lambda: fees(window1)).place(x=30,y=460)
    Button(table_frame,text="Attendance",width=20,relief="ridge",font = ("arial",16),bd=3,command = lambda:attendance(window1)).place(x=30,y=530)
    Button(table_frame,text="Miscellaneous",width=20,relief="ridge",font = ("arial",16),bd=3,command = lambda:miscellaneous(window1)).place(x=30,y=600)
    Label(table_frame1,text="COLLEGE  MANAGEMENT  SYSTEM",font=("times new roman",25,"bold"),relief = "ridge",width = 35).place(x=345,y=28)

    window1.mainloop()
def main_window():
    window=Tk()
    ac1=StringVar()
    ac2 = StringVar()
    window.geometry("580x360")
    window.title("Administrator Login Page")
    Label(window,text="Vignana Bharathi College",font=("arial",20,"bold"),width = 40,relief = SOLID).pack()
    Label(window,text="Administrator Name:",font=("arial",16,"bold"),width = 18,relief = SOLID).place(x=40,y=100)
    Label(window,text="Enter Password:",font=("arial",16,"bold"),width = 18,relief = SOLID).place(x=40,y= 150)
    entry11=Entry(window,textvar=ac1,width= 30,relief = "solid").place(x=350,y=105)
    entry11=Entry(window,textvar=ac2,show = "*",width = 30, relief = "solid").place(x=350,y=155)
    login_button=Button(window,text="login",width=10,relief="ridge",bg="grey",fg="white", command=lambda: login_session(window)).place(x=250,y=250)
    
    

    
    
    window.mainloop()
main_window()