from datetime import datetime
import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import font
from tkinter.font import BOLD
from tkinter import messagebox
import re
import pymysql
from tkinter import ttk
from PIL import Image, ImageTk

######################################### Section1 #######################################################

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
def admin():
    if usernameEntry.get() == "ADMIN" or passwordEntry.get() == "Admin@001":
        root2.destroy()
        import treeVie
def reset():
     usernameEntry.delete(0,'end')
     passwordEntry.delete(0, 'end')   	
def passchk():
    passwd = passwordEntry.get()
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg)   
    mat = re.search(pat, passwd)
    if mat:
        print("Password is valid.")
    else:
        messagebox.showerror("ERROR", "Password must contain Special character, numbers or capital letters")
def empty():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror("ERROR", "All fields are required")
def loginPage():
    frame = Frame(root2,width=1400, height=800,)
    frame.place(x=0,y=0)
    con4 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur4 = con4.cursor()
    cur4.execute("select * from products")
    row4 = cur4.fetchall()
    treeview3 =ttk.Treeview(frame,height=700)
    treeview3["columns"]= ("PId","P_Name","Price","Category")
    treeview3["show"]="headings"
    s = ttk.Style(root)
    s.theme_use("vista")
    s.configure(".", font=('times new roman', 11))
    s.configure("treeview3.Heading", foreground="BLUE", font=("times new roman", 14, "bold"))
    treeview3.column('PId', width=5, minwidth=5,anchor=tk.CENTER)
    treeview3.column('P_Name', width=30, minwidth=20,anchor=tk.CENTER)
    treeview3.column('Price', width=30, minwidth=30,anchor=tk.CENTER)
    treeview3.column('Category', width=30, minwidth=30,anchor=tk.CENTER)

################################## Adding heading #####################################################

    treeview3.heading('PId', text='PId', anchor=CENTER)
    treeview3.heading('P_Name', text='P_Name', anchor=CENTER)
    treeview3.heading('Price', text='Price' ,anchor=CENTER)
    treeview3.heading('Category', text='Category' ,anchor=CENTER)    
    treeview3.place(x=10,y=100,width=650,height=600)
    i = 0
    for ro in row4:
        treeview3.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i = i+1
    hsb = ttk.Scrollbar(treeview3, orient="vertical")
    hsb.configure(command=treeview3.yview)
    treeview3.configure(yscrollcommand=hsb.set)
    hsb.pack(fill=Y,side=RIGHT)

###########################################################################################################
###########################################################################################################
###########################################################################################################
    
    con5 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur5 = con5.cursor()
    cur5.execute("select * from orders where name=%s and email=%s",(row[1],row[3]))
    row5 = cur5.fetchall()
    treeview4 =ttk.Treeview(frame,height=700)
    treeview4["columns"]= ("Id","Name","Product","Qty","Bill","Date")
    treeview4["show"]="headings"
    s = ttk.Style(root)
    s.theme_use("vista")
    s.configure(".", font=('times new roman', 11))
    s.configure("treeview4.Heading", foreground="BLUE", font=("times new roman", 14, "bold"))
    #adding columns
    treeview4.column('Id', width=1, minwidth=1,anchor=tk.CENTER)
    treeview4.column('Name', width=10, minwidth=10,anchor=tk.CENTER)
    treeview4.column('Product', width=10, minwidth=10,anchor=tk.CENTER)
    treeview4.column('Qty', width=10, minwidth=10,anchor=tk.CENTER)
    treeview4.column('Bill', width=10, minwidth=10,anchor=tk.CENTER)
    treeview4.column('Date', width=10, minwidth=10,anchor=tk.CENTER) 
    #adding heading
    treeview4.heading('Id', text='Id', anchor=CENTER)
    treeview4.heading('Name', text='Name', anchor=CENTER)
    treeview4.heading('Product', text='Product' ,anchor=CENTER)
    treeview4.heading('Qty', text='Qty' ,anchor=CENTER)
    treeview4.heading('Bill', text='Bill' ,anchor=CENTER)
    treeview4.heading('Date', text='Date' ,anchor=CENTER)    
    treeview4.place(x=670,y=100,width=650,height=600)        
    i = 0
    for ro in row5:
        treeview4.insert('',i, text="", values=(ro[0],ro[1],ro[4],ro[5],ro[6],ro[7]))
        i = i+1
    hsb = ttk.Scrollbar(treeview4, orient="vertical")
    hsb.configure(command=treeview4.yview)
    treeview4.configure(yscrollcommand=hsb.set)
    hsb.pack(fill=Y,side=RIGHT)

###################################### LABELS  ###########################################################

    idlabe = Label(frame, text="Id : ",fg = "red",font=("times new roman", 15))
    idlabe.place(x=750,y=100)
    Namelabe = Label(frame, text="Name : ",fg="red",font=("times new roman", 15))
    Namelabe.place(x=750,y=150)
    Emaillabe = Label(frame, text="Email : ",fg="red",font=("times new roman", 15))
    Emaillabe.place(x=750,y=200)
    pIDlabe = Label(frame, text="Product Id : ",fg="red",font=("times new roman", 15))
    pIDlabe.place(x=750,y=250)
    Productlabe = Label(frame, text="Produt Name : ",fg="red",font=("times new roman", 15))
    Productlabe.place(x=750,y=300)
    Pricelabe = Label(frame, text="Price : ",fg="red",font=("times new roman", 15))
    Pricelabe.place(x=750,y=350)
    Qtylabe = Label(frame, text="Qty : ",fg="red",font=("times new roman", 15))
    Qtylabe.place(x=750,y=400)
    Pricelabe = Label(frame, text="Total Bill : ",fg="red",font=("times new roman", 15))
    Pricelabe.place(x=750,y=450)

####################################### UPDATE LABELS VALUES ###################################################    

    labe = Label(frame, text="",font=("times new roman", 15))
    labe.place(x=900,y=100)
    labe["text"] = row[0]
    labe1 = Label(frame, text="",font=("times new roman", 15))
    labe1.place(x=900,y=150)
    labe1["text"] = row[1]
    labe2 = Label(frame, text="",font=("times new roman", 15))
    labe2.place(x=900,y=200)
    labe2["text"] = row[3]
    en1 = Entry(frame)
    en1.place(x=850,y=400)
    
    def hello():
        #grab record NUmber 
        selects = treeview3.focus()
        #grab record values
        global value 
        value = treeview3.item(selects,'values')        
        labe3 = Label(frame, text="",font=("times new roman", 15))
        labe3.place(x=900,y=250)
        labe3["text"] = value[0]
        labe4 = Label(frame, text="",font=("times new roman", 15))
        labe4.place(x=900,y=300)
        labe4["text"] = value[1]
        labe5 = Label(frame, text="",font=("times new roman", 15))
        labe5.place(x=900,y=350)
        labe5["text"] = value[2]
        labe5 = Label(frame, text="",font=("times new roman", 15))
        labe5.place(x=900,y=450)
        pi = int(value[0])
        a= int(value[2])
        global b
        b = int(en1.get())#int(row[0])
        qt = int(value[4])
        global pid
        pid = int(value[0])
        if b <= qt:
            fqt = qt - b
            con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
            cur = con.cursor()
            cur.execute("update products set QTY=%s where Pid=%s",(fqt,pi))
            con.commit()
            con.close()    
            messagebox.showinfo("Record Updated", "Record updated successfully")
            print(fqt)
        else:
            messagebox.showerror("error","Sorry! not enough quantity available.")
        global c
        c = a*b
        labe5["text"] = c
    def new():
        con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
        cur = con.cursor()
        b = int(en1.get())#int(row[0])
        global pnam_var
        pnam_var = StringVar()
        enk = Entry(frame,textvariable=pnam_var)
        enk.place(x=800,y=50)
        enk.insert(0,value[1])
        print(enk.get())
        if b == "":
            messagebox.showerror("Field Error"," All fields are required")
        else:
            cur.execute("insert into orders(Id,name,email,Pid,Pname,QTY,bill,date) values(%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[3],pid,enk.get(),b,c,formatted_date))
            con.commit()
            con.close
            messagebox.showinfo("New Product", "New product added successfully")
    Serac = Entry(frame)
    Serac.place(x=950,y=70)
    def Logout():
        messagebox.showinfo("Logout", "Thanks for using our app.")
        frame.destroy()
    def Search():
        treeview3.delete(*treeview3.get_children())
        try:
            con4 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
            cur4 = con4.cursor()
            cur4.execute("select * from products where PName = %s",(Serac.get()))
            row4 = cur4.fetchall()
            i = 0
            for ro in row4:
                treeview3.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
                i = i+1
            if row4 == None:
                cur4 = con4.cursor()
                cur4.execute("select * from products where Category= %s",(Serac.get()))
                row4 = cur4.fetchall()
                i = 0
                for ro in row4:
                    treeview3.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
                    i = i+1
            else:
                cur4 = con4.cursor()
                cur4.execute("select * from products where Category= %s",(Serac.get()))
                row4 = cur4.fetchall()
                i = 0
                for ro in row4:
                    treeview3.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
                    i = i+1
        except Exception as e:
            print(e)
    l = Label(frame, text="", font=("times new romans",18,"bold"), fg="green")
    l.place(x=600,y=20)
    l["text"] = "Welcome " + row[1]
    logbtn = Button(frame,text="Logout", command=Logout)
    logbtn.place(x=950,y=20)
    btn = Button(frame,text="Search", command=Search)
    btn.place(x=1050,y=20)
    btn = Button(frame,text="Select", command=hello)
    btn.place(x=950,y=700)
    btn1 = Button(frame,text="order", command=new)
    btn1.place(x=1050,y=700)
    con7 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur7 = con7.cursor()
    cur7.execute("select * from orders where date =2021-08")
    cs = cur7.fetchall()
    con7.commit()
    con7.close()    
    print(cs)
def login():    
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
        cur = con.cursor()
        cur.execute("select * from employees where fname=%s and passwrd=%s",(usernameEntry.get(),passwordEntry.get()))
        global row
        row = cur.fetchone()
        print(row)
        if row==None:
            messagebox.showerror("ERROR", "Enter Valid Username or Password")    
        else:
            messagebox.showinfo("Success", "Login Successfully")
            loginPage()	
    except:
        pass
################################################ Section Change #####################################################

root2 = Tk()  
root2.geometry('1400x800+0+0')  
root2.title('Stationary Management System | Login')
root2.resizable("false","false")

######################################## Login Page Background ###########################################

image1 = Image.open("background3.jpg")
image1 = image1.resize((1400,800), Image.ANTIALIAS) 
test = ImageTk.PhotoImage(image1)
canvas = tk.Label(root2,image=test)
canvas.image = test
canvas.place(x=0,y=0)

######################################## FRAME #######################################################
root = Frame(canvas, width=600,height=600, bg="white")
root.place(x=430,y=120)
root3 = Frame(canvas, width=1400,height=50, bg="gray4")
root3.place(x=0,y=0)

######################################## Login Page Labels and Entries ####################################

label2 = Label(root3,font=("times new roman",18,"bold"),bg="gray4",fg="White",text="Stationary Management System | Developed By Maryam.")
label2.place(x=450,y=10)
global usernameEntry
usernameEntry = StringVar()
Modelname = Label(root, font=("arial",25,BOLD),fg="red4",bg="white", text="Stationary Management System")
Modelname.place(x=50, y=20)
Modelname2 = Label(root, font=("arial",15,BOLD),fg="green",bg="white", text="Login Page")
Modelname2.place(x=220, y=80)
username = Label(root,  font=("arial",14,BOLD), foreground="red",bg="white", text="User Name")
username.place(x=120, y=170)
username = StringVar()
usernameEntry = Entry(root, textvariable=username )
usernameEntry.place(x=240, y=170, width=200, height=25)
passwordLabel = Label(root, font=("arial",14,BOLD), foreground="red",bg="white", text="Password")
passwordLabel.place(x=120, y=270 )
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*')
passwordEntry.place(x=240, y=270 , width=200, height=25)

######################################## Buttons ###########################################################

loginButton = Button(root, text="Login", font=("arial", 12, BOLD), command=lambda:[passchk(), empty(),admin(),login()])#validateLogin
loginButton.place(x=250, y=370 , width=130)
resetButton = Button(root, text="Reset", font=("arial", 12, BOLD), foreground="blue" , command=reset)
resetButton.place(x=250, y=420 , width=130)
exitButton = Button(root, text="Exit", font=("arial", 12, BOLD),foreground="red", command=root2.destroy) 
exitButton.place(x=250, y=470 , width=130)

root2.mainloop()     