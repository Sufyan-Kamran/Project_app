import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import font
from tkinter.font import BOLD
from tkinter import messagebox
import re
import pymysql
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
    frame = Frame(root2,width=1400, height=800,bg="gray")
    frame.place(x=0,y=0)
def login():    
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
        cur = con.cursor()
        cur.execute("select * from employees where fname=%s and passwrd=%s",(usernameEntry.get(),passwordEntry.get()))
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