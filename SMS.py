from tkinter import *
from functools import partial
from tkinter.font import BOLD
from tkinter import messagebox
import re
import pymysql

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
    frame = Frame(root,width=1400, height=800,bg="gray")
    frame.place(x=0,y=0)
def login():
    
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="sufyan" )
        cur = con.cursor()
        cur.execute("select * from user where name=%s and password=%s",(usernameEntry.get(),passwordEntry.get()))
        row = cur.fetchone()
        print(row)
        if row==None:
            SellButton["state"]="disable"
            StockButton["state"]="disable"
            messagebox.showerror("ERROR", "Enter Valid Username or Password")
            
        else:
            messagebox.showinfo("Success", "Login Successfully")
            SellButton["state"]="normal"
            StockButton["state"]="normal"
            loginPage()

	
    except:
        pass
        
    
#window
root = Tk()  
root.geometry('1400x800+0+0')  
root.title('Stationary Management System')
global usernameEntry

usernameEntry = StringVar()

Modelname = Label(root, font=("arial",35,BOLD), text="Stationary Management System")
Modelname.place(x=420, y=250)


username = Label(root,  font=("arial",14,BOLD), foreground="red", text="User Name")
username.place(x=550, y=360)
username = StringVar()



usernameEntry = Entry(root, textvariable=username )
usernameEntry.place(x=700, y=365, width=200, height=25)


passwordLabel = Label(root, font=("arial",14,BOLD), foreground="red", text="Password")
passwordLabel.place(x=550, y=415 )
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*')
passwordEntry.place(x=700, y=420 , width=200, height=25)


#All Buttons 

loginButton = Button(root, text="Login", font=("arial", 12, BOLD), command=lambda:[passchk(), empty(),login()])#validateLogin
loginButton.place(x=520, y=500 , width=130)

resetButton = Button(root, text="Reset", font=("arial", 12, BOLD), foreground="blue" , command=reset)
resetButton.place(x=660, y=500 , width=130)

exitButton = Button(root, text="Exit", font=("arial", 12, BOLD),foreground="red", command=root.destroy) 
exitButton.place(x=800, y=500 , width=130)

StockButton = Button(root, text="Stock",state="disable" ,font=("arial", 12, BOLD),foreground="red")  
StockButton.place(x=590, y=600 , width=130)

SellButton = Button(root, text="Sell", state="disable", font=("arial", 12, BOLD),foreground="red")  
SellButton.place(x=780, y=600 , width=130)

validateLogin = partial(validateLogin, username, password)

    
root.mainloop()     