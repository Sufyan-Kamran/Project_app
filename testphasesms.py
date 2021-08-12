# In python language this we use import keyword for importing the library/module.
# Module/library is used to design and develop your  code easily.
# we use "." dot for importing specific fuctionality from the library thats why we use "."(dot).
# In this application we use several libraries.
# In python language we have a tkinter library which is compatable with OS (operating System),
# tkinter is provide as Frame, GUI and support many other functionalities  this is why we use it tkinter library.
# we use  functool library and re library for password validation.
# Last library we use pymysql library which is the second most import libray cause
# with the help of this library we can make connection with our mysql database and use insert/delete/update and many other functions.

#***************************************** IMPORTING LIBRARIES *************************************************************

from tkinter import *
from functools import partial
from tkinter import font
from tkinter.font import BOLD
from tkinter import messagebox
import re
import pymysql

#***************************************** Functions ************************************************************************
# This is a function it is use to resest all the entry fields.
# By using .delete() function we will delet every thing in the entry boxes.
def reset():
     usernameEntry.delete(0,'end')
     passwordEntry.delete(0, 'end')

#this fuction is used to check password validation

def passchk():
    
    #in this line we get password from user by using .get()function
    passwd = passwordEntry.get()
    
    # In this line we make a string for password validation  in this string we will store
    # any thing what we want to include in our password validation.
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    # in this line we compile our string by using .compile() fucntion which is from re librrary.
    pat = re.compile(reg)   
    
    # in this line we use search() function which is also from re library it will serach all every
    # single word which is in our string.
    mat = re.search(pat, passwd)
    
    # Here we use condition that if our mat is find words which is in our string that mean password is valid.
    # and then we use print funtion which is from python for printing something.
    if mat:
        print("Password is valid.")
    
    # we use else condition for if above condition is false so this condition will run.
    else:
        # we use tkinter messagebox() fuction for showerror this is show error window pop-up if else condtion will run.
        messagebox.showerror("ERROR", "Password must contain Special character, numbers or capital letters")
		
# This is a function for checking is username and password fields are empty or not.
def empty():
    # Here we use if condtion for if username and password is empty so this tome again another error window pop-up.
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror("ERROR", "All fields are required")


# Here is we make our login function which is connect with database and check username and password.
def login():
    # we use try and exepction keyword for our program more reliable if we use this keyword our program will not crash.
    try:
        # In this line we make a connection bertween database and our program.
        con = pymysql.connect(host="localhost", user="root", password="", database="sufyan" )
        cur = con.cursor()
        # in this line we type our mysql query for checking is username and password in our database or not.
        cur.execute("select * from user where name=%s and password=%s",(usernameEntry.get(),passwordEntry.get()))
        #here we use fetchone for fetch only one column data from our database table
        row = cur.fetchone()
        print(row)
        # here we use if statement for if there is no relavent data in our database so it our buttons are remain disable and error window pop-up.
        if row==None:
            SellButton["state"]="disable"
            StockButton["state"]="disable"
            messagebox.showerror("ERROR", "Enter Valid Username or Password")
        # Here if our data is exists in our database so success window pop-up and our buttons are becomes enable.
        else:
            # Here is success message line 
            messagebox.showinfo("Success", "Login Successfully")
            SellButton["state"]="normal"
            StockButton["state"]="normal"

	
    except:
        pass
        
#******************************************** WINDOW FRAMEWORK **********************************************************
# here is our main window start 
root = Tk()

#here we set our geometry 1000 is width of window and 550 is height of our window
root.geometry('1000x550')  

#here is we set title of our application
root.title('Stationary Management System')
dev = Frame(root, bg="gray4")
dev.place(x=0,y=0,width=1000,height=30)
devl = Label(dev,font=("times new roman", 15), text="Stationary Management System | Developed By Maryam",bg="gray4",fg="white")
devl.place(x=330,y=2)

# we convert our local variable into global so that we can use and access of it in many other function.
global usernameEntry

usernameEntry = StringVar()

#**********************************LABELS AND ENTRIES *******************************************************************

# this is our label which place on the top
Modelname = Label(root, font=("arial",30,BOLD), text="Stationary Management System")

# this is our label width and height remember first we define width and later we define height.
Modelname.place(x=250, y=80)

# This is our username label.
username = Label(root,  font=("arial",14,BOLD), foreground="red", text="User Name")

# this is our label width and height remember first we define width and later we define height.
username.place(x=350, y=195)
username = StringVar()


# This is our username entry field. From entry field we get data.
usernameEntry = Entry(root, textvariable=username )

# this is our entry width and height remember first we define width and later we define height.
usernameEntry.place(x=500, y=200, width=200, height=25)

# This is our password label.
passwordLabel = Label(root, font=("arial",14,BOLD), foreground="red", text="Password")

# this is our label width and height remember first we define width and later we define height.
passwordLabel.place(x=350, y=245 )
password = StringVar()

# This is our password entry field. From entry field we get data.
passwordEntry = Entry(root, textvariable=password, show='*')

# this is our entry width and height remember first we define width and later we define height.
passwordEntry.place(x=500, y=250 , width=200, height=25)

#************************************************* BUTTONS **************************************************************************
# here is our all buttons
# in buttons we provide text= "etc" which is written on our button 
# most important in button is command by using command we can run our fucntions and do anythong what we want.
# we use lambda in button command we use lambda for connect many functions in one button

# This is our login button in this button command we use our password checking, empty, and login function.
loginButton = Button(root, text="Login", font=("arial", 12, BOLD), command=lambda:[passchk(), empty(),login()])
loginButton.place(x=350, y=300 , width=130)

# this is reset button connect with rest function,
resetButton = Button(root, text="Reset", font=("arial", 12, BOLD), foreground="blue" , command=reset)
resetButton.place(x=480, y=300 , width=130)

#this is exit button which is use to shutdown the application.
exitButton = Button(root, text="Exit", font=("arial", 12, BOLD),foreground="red", command=root.destroy) 
exitButton.place(x=610, y=300 , width=130)

# this is the disable button which is not connected with any function.
StockButton = Button(root, text="Stock",state="disable" ,font=("arial", 12, BOLD),foreground="red")  
StockButton.place(x=420, y=400 , width=130)

# this is the disable button which is not connected with any function.
SellButton = Button(root, text="Sell", state="disable", font=("arial", 12, BOLD),foreground="red")  
SellButton.place(x=610, y=400 , width=130)

# here is our application exit site.
root.mainloop()