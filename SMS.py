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
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
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
    #adding columns
    treeview3.column('PId', width=5, minwidth=5,anchor=tk.CENTER)
    treeview3.column('P_Name', width=30, minwidth=20,anchor=tk.CENTER)
    treeview3.column('Price', width=30, minwidth=30,anchor=tk.CENTER)
    treeview3.column('Category', width=30, minwidth=30,anchor=tk.CENTER)
    

    #adding heading
    treeview3.heading('PId', text='PId', anchor=CENTER)
    treeview3.heading('P_Name', text='P_Name', anchor=CENTER)
    treeview3.heading('Price', text='Price' ,anchor=CENTER)
    treeview3.heading('Category', text='Category' ,anchor=CENTER)
    #treeview3.pack(side=TOP, fill=BOTH)

    treeview3.place(x=100,y=100,width=600,height=600)

        
    i = 0
    for ro in row4:
        treeview3.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i = i+1
    hsb = ttk.Scrollbar(treeview3, orient="vertical")
    hsb.configure(command=treeview3.yview)
    treeview3.configure(yscrollcommand=hsb.set)
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
    Pricelabe = Label(frame, text="Total Bill : ",fg="red",font=("times new roman", 15))
    Pricelabe.place(x=750,y=400)
###############################################################################################################

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
    en1.place(x=850,y=600)
    
    def hello():
        #print(row[0],row[1],row[3],row4[0],row4[1],row4[2])
        #grab record NUmber 
        selects = treeview3.focus()
        #grab record values
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
        labe5.place(x=900,y=400)
        pi = int(value[0])
        a= int(value[2])
        b = int(en1.get())#int(row[0])
        qt = int(value[4])
        
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
    
        c = a*b
        labe5["text"] = c



    btn = Button(frame,text="hello", command=hello)
    btn.place(x=950,y=700)




def login():    
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
        cur = con.cursor()
        cur.execute("select * from employees where fname=%s and passwrd=%s",(usernameEntry.get(),passwordEntry.get()))
        global row
        row = cur.fetchone()
        print(row)
        if row==None:
            SellButton["state"]="disable"
            StockButton["state"]="disable"
            messagebox.showerror("ERROR", "Enter Valid Username or Password")    
        else:
            messagebox.showinfo("Success", "Login Successfully")
            #SellButton["state"]="normal"
            #StockButton["state"]="normal"
            loginPage()	
    except:
        pass
################################################ Section Change #####################################################
root2 = Tk()  
root2.geometry('1400x800+0+0')  
root2.title('Stationary Management System | Login')
root2.resizable("false","false")


############################################### Background Image ##3333################################################

#canvas = Canvas(root2, width=1500, height=800)
#canvas.place(x=-10,y=0)
#imge = ImageTk.PhotoImage(Image.open("background3.jpg"))
#imge = img.resize((50, 50), Image.ANTIALIAS)
#canvas.create_image(-10, 0, anchor=NW, image=imge)

image1 = Image.open("background3.jpg")
image1 = image1.resize((1400,800), Image.ANTIALIAS) 
test = ImageTk.PhotoImage(image1)
canvas = tk.Label(root2,image=test)
canvas.image = test
canvas.place(x=0,y=0)



root = Frame(canvas, width=600,height=600, bg="white")
root.place(x=430,y=120)
root3 = Frame(canvas, width=1400,height=50, bg="gray4")
root3.place(x=0,y=0)


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
loginButton = Button(root, text="Login", font=("arial", 12, BOLD), command=lambda:[passchk(), empty(),login()])#validateLogin
loginButton.place(x=250, y=370 , width=130)
resetButton = Button(root, text="Reset", font=("arial", 12, BOLD), foreground="blue" , command=reset)
resetButton.place(x=250, y=420 , width=130)
exitButton = Button(root, text="Exit", font=("arial", 12, BOLD),foreground="red", command=root.destroy) 
exitButton.place(x=250, y=470 , width=130)
#StockButton = Button(root, text="Stock",state="disable" ,font=("arial", 12, BOLD),foreground="red")  
#StockButton.place(x=590, y=600 , width=130)
#SellButton = Button(root, text="Sell", state="disable", font=("arial", 12, BOLD),foreground="red")  
#SellButton.place(x=780, y=600 , width=130)








root2.mainloop()     