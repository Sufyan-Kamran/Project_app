import tkinter as tk 
from tkinter import *
from ttkwidgets.autocomplete import AutocompleteEntryListbox
from tkinter import ttk
from tkinter import font
import mysql.connector
import pymysql
from tkcalendar import Calendar, DateEntry


root = Tk()
root.geometry("1500x800+0+0")
lab = Label(root, text="ADMINSTRATION PANEL",fg="red", font=("times new roman", 24,"bold"))
lab.place(x=300,y=20)


def serachs():
    con = pymysql.connect(host="localhost", user="root", password="", database="sufyan" )
    cur = con.cursor()
    cur.execute("select * from userinformations where id=%s",(search.get()))
    row = cur.fetchone()
    print(row)
    
    ent1.insert(0,row[0])
    ent2.insert(0,row[1])
    ent3.insert(0,row[2])
    ent4.insert(0,row[3])
    ent5.insert(0,row[4])
    ent6.insert(0,row[5])
    
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)

def new():
    con = pymysql.connect(host="localhost", user="root", password="", database="sufyan" )
    cur = con.cursor()
    cur.execute("insert into userinformations where first_name = %s, last_name = %s, occupation=%s,dob=%s,country=%s",(fname.get(),lname.get(),occup.get(),dob.get(),country.get()))

    row = cur.fetchall()
    

def selected():
    #delete previous loaded data from entry boxes
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)

    #grab record NUmber 
    selects = treeview.focus()

    #grab record values
    value = treeview.item(selects,'values')
    ent1.insert(0,value[0])
    ent2.insert(0,value[1])
    ent3.insert(0,value[2])
    ent4.insert(0,value[3])
    ent5.insert(0,value[4])
    ent6.insert(0,value[5])
    
def update():
    
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)
    #grab record NUmber 
    selects = treeview.focus()

    #grab record values
    value = treeview.item(selects,'values')
    ent1.insert(0,value[0])
    ent2.insert(0,value[1])
    ent3.insert(0,value[2])
    ent4.insert(0,value[3])
    ent5.insert(0,value[4])
    ent6.insert(0,value[5])
    con = pymysql.connect(host="localhost", user="root", password="", database="sufyan" )
    cur = con.cursor()
    sql = "update userinformations set first_name=%s,last_name=%s,occupation=%s,dob=%s,country=%s where id=%s"
    inputs =(ent2.get(),ent3.get(),ent4.get(),ent5.get(),ent6.get(),search.get())
    cur.execute(sql,inputs)

    con.commit()
    con.close()    


search = Entry(root)
search.place(x=700,y=20)

searchbtn = Button(root,text="SERACH",command=serachs)
searchbtn.place(x=800,y=20)
btn = Button(root, text="SELECTED", command=selected)
btn.place(x=500,y=670,width=70)
ubtn = Button(root, text="Update",bg="blue",fg="white", command=update)
ubtn.place(x=500,y=720,width=70)
Dbtn = Button(root, text="Delete",bg="red",fg="white", command=update)
Dbtn.place(x=500,y=770,width=70)


con = pymysql.connect(host="localhost", user="root", password="", database="sufyan" )
cur = con.cursor()
cur.execute("select * from userinformations ")
row = cur.fetchall()

#connect = mysql.connector.connect(host="localhost", user="root",password="",database="sufyan")
#conn= connect.cursor()
#conn.execute("select * from user")
#print(conn)

treeview =ttk.Treeview(root,height=700)
treeview["columns"]= ("Id","Name","Lastname","Occupation","date of Birth","Country")
treeview["show"]="headings"
s = ttk.Style(root)
s.theme_use("vista")
s.configure(".", font=('times new roman', 11))
s.configure("Treeview.Heading", foreground="BLUE", font=("times new roman", 14, "bold"))

#adding columns

treeview.column('Id', width=5, minwidth=5,anchor=tk.CENTER)
treeview.column('Name', width=30, minwidth=20,anchor=tk.CENTER)
treeview.column('Lastname', width=30, minwidth=20,anchor=tk.CENTER)
treeview.column('Occupation', width=30, minwidth=30,anchor=tk.CENTER)
treeview.column('date of Birth', width=30, minwidth=30,anchor=tk.CENTER)
treeview.column('Country', width=30, minwidth=30,anchor=tk.CENTER)

#adding heading
treeview.heading('Id', text='Id', anchor=CENTER)
treeview.heading('Name', text='Name', anchor=CENTER)
treeview.heading('Lastname', text='Lastname', anchor=CENTER)
treeview.heading('Occupation', text='Occupation' ,anchor=CENTER)
treeview.heading('date of Birth', text='Date of Birth' ,anchor=CENTER)
treeview.heading('Country', text='Country' ,anchor=CENTER)
#treeview.pack(side=TOP, fill=BOTH)

treeview.place(x=0,y=100,width=1000,height=500)

    
i = 0
for ro in row:
    treeview.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
    i = i+1
hsb = ttk.Scrollbar(treeview, orient="vertical")
hsb.configure(command=treeview.yview)
treeview.configure(yscrollcommand=hsb.set)
hsb.pack(fill=Y,side=RIGHT)
global ent1
global ent2
global ent3
global ent4
global ent5
global ent6

#Delete And Update records
UaD = Label(root, text="Update/Delete records",fg="red", font=("times new roman",22))
UaD.place(x=30,y=620)

ent1 = Entry(root,width=30)
ent1.place(x=10,y=670,height=30)
ent2 = Entry(root,width=30)
ent2.place(x=230,y=670,height=30)
ent3 = Entry(root,width=30)
ent3.place(x=10,y=710,height=30)
ent4 = Entry(root,width=30)
ent4.place(x=230,y=710,height=30)
ent5 = Entry(root,width=30)
ent5.place(x=10,y=750,height=30)
ent6 = Entry(root,width=30)
ent6.place(x=230,y=750,height=30)

#Create New User
cframe = Frame(root,width=420,height=590)
cframe.place(x=1030,y=0)

Nlabel =Label(cframe, text="Create New User", font=("times new roman",24,"bold"),fg="green")
Nlabel.place(x=100,y=20)

#New user
firstname = Label(cframe, text="First Name : ", font=("times new roman",15),fg="blue")
firstname.place(x=10,y=150)
lastname = Label(cframe, text="Last Name : ", font=("times new roman",15),fg="blue")
lastname.place(x=10,y=200)
occupation = Label(cframe, text="Occupation : ", font=("times new roman",15),fg="blue")
occupation.place(x=10,y=250)
dobirth = Label(cframe, text="D.O.B : ", font=("times new roman",15),fg="blue")
dobirth.place(x=10,y=300)
Country = Label(cframe, text="Country : ", font=("times new roman",15),fg="blue")
Country.place(x=10,y=350)

#new user entry
global fname
fname = Entry(cframe, font=("times new roman",15),fg="Gray")
fname.place(x=150,y=150)
global lname
lname = Entry(cframe, font=("times new roman",15),fg="gray")
lname.place(x=150,y=200)
global occup
occup = Entry(cframe, font=("times new roman",15),fg="gray")
occup.place(x=150,y=250)
global dob
dob = DateEntry(cframe, font=("times new roman",15),fg="gray")
dob.place(x=150,y=300)
global country
country = Entry(cframe, font=("times new roman",15),fg="gray")
country.place(x=150,y=350)

#Create user button
Cbtn = Button(cframe, text="ADD USER",fg="WHITE", bg="blue",width=20, height=2, command=new)
Cbtn.place(x=10,y=400)








root.mainloop()