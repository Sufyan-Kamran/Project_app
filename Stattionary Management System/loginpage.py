from tkinter import *
from functools import partial
from tkinter.font import BOLD
from tkinter import messagebox
import re
import pymysql

def logout():
    root.destroy()
    import SMS.py
root = Tk()  
root.resizable("false","false")
root.geometry('1200x850')  
root.title('Stationary Management System')

def searching():
    con = pymysql.connect(host="localhost", user="root", password="", database="sufyan" )
    cur = con.cursor()
    cur.execute("select name from items where product=%s",(search.get()))
    row = cur.fetchall()
    print(row)
    

def usernasmes():
    title = Label(mainframe,foreground="purple",bg="red",font=("times new roman",28,BOLD), text="Welcome To Our Shop")
    title.place(x=250,y=20)

    title['text']=(row)
def change():
    pass
    


mainframe = StringVar()
mainframe = Frame(root, width=1200, height=800, bg="white").pack()
search = Entry(mainframe, width=25,font=("arial", 12, BOLD), highlightcolor="yellow")
search.place(x=650,y=11, height=30)

frame= Frame(mainframe, bg="gray", width=1200,height=800)
frame.place(x=0,y=100)


frame1= Frame(frame, bg="yellow", width=200,height=200)
frame1.place(x=50,y=10)

frame2= Frame(frame, bg="yellow", width=200,height=200)
frame2.place(x=270,y=10)

frame3= Frame(frame, bg="yellow", width=200,height=200)
frame3.place(x=490,y=10)

frame4= Frame(frame, bg="yellow", width=200,height=200)
frame4.place(x=710,y=10)

frame5= Frame(frame, bg="yellow", width=200,height=200)
frame5.place(x=930,y=10)


frame6= Frame(frame, bg="yellow", width=200,height=200)
frame6.place(x=50,y=250)

frame7= Frame(frame, bg="yellow", width=200,height=200)
frame7.place(x=270,y=250)

frame8= Frame(frame, bg="yellow", width=200,height=200)
frame8.place(x=490,y=250)

frame9= Frame(frame, bg="yellow", width=200,height=200)
frame9.place(x=710,y=250)

frame10= Frame(frame, bg="yellow", width=200,height=200)
frame10.place(x=930,y=250)


frame11= Frame(frame, bg="yellow", width=200,height=200)
frame11.place(x=50,y=490)

frame12= Frame(frame, bg="yellow", width=200,height=200)
frame12.place(x=270,y=490)

frame13= Frame(frame, bg="yellow", width=200,height=200)
frame13.place(x=490,y=490)

frame14= Frame(frame, bg="yellow", width=200,height=200)
frame14.place(x=710,y=490)

frame15= Frame(frame, bg="yellow", width=200,height=200)
frame15.place(x=930,y=490)

logoutButton = Button(mainframe, text="Search", font=("arial", 12, BOLD), command=lambda:[searching(),usernasmes()])
logoutButton.place(x=900, y=10 , width=130)

logoutButton = Button(mainframe, text="Logout", font=("arial", 12, BOLD), command=logout)
logoutButton.place(x=1050, y=10 , width=130)




    
root.mainloop()