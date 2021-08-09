import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter import font
import mysql.connector
import pymysql


root = Tk()
root.geometry("1200x800+0+0")
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
btn.place(x=100,y=700)
ubtn = Button(root, text="Update", command=update)
ubtn.place(x=200,y=700)


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

treeview.column('Id', width=50, minwidth=50,anchor=tk.CENTER)
treeview.column('Name', width=50, minwidth=50,anchor=tk.CENTER)
treeview.column('Lastname', width=50, minwidth=50,anchor=tk.CENTER)
treeview.column('Occupation', width=50, minwidth=50,anchor=tk.CENTER)
treeview.column('date of Birth', width=50, minwidth=50,anchor=tk.CENTER)
treeview.column('Country', width=50, minwidth=50,anchor=tk.CENTER)

#adding heading
treeview.heading('Id', text='Id', anchor=CENTER)
treeview.heading('Name', text='Name', anchor=CENTER)
treeview.heading('Lastname', text='Lastname', anchor=CENTER)
treeview.heading('Occupation', text='Occupation' ,anchor=CENTER)
treeview.heading('date of Birth', text='Date of Birth' ,anchor=CENTER)
treeview.heading('Country', text='Country' ,anchor=CENTER)
#treeview.pack(side=TOP, fill=BOTH)

treeview.place(x=0,y=100,width=1200,height=500)

    
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

ent1 = Entry(root,width=30)
ent1.place(x=10,y=650)
ent2 = Entry(root,width=30)
ent2.place(x=200,y=650)
ent3 = Entry(root,width=30)
ent3.place(x=390,y=650)
ent4 = Entry(root,width=30)
ent4.place(x=580,y=650)
ent5 = Entry(root,width=30)
ent5.place(x=770,y=650)
ent6 = Entry(root,width=30)
ent6.place(x=960,y=650)

root.mainloop()