import tkinter as tk 
from tkinter import *
from tkinter import ttk
import mysql.connector
import pymysql


root = Tk()
root.geometry("1000x800+0+0")


con = pymysql.connect(host="localhost", user="root", password="", database="sufyan" )
cur = con.cursor()
cur.execute("select * from userinformation where 500")
row = cur.fetchall()
print(row)
#connect = mysql.connector.connect(host="localhost", user="root",password="",database="sufyan")
#conn= connect.cursor()
#conn.execute("select * from user")
#print(conn)

treeview =ttk.Treeview(root)
treeview["columns"]= ("Name","Lastname","Occupation","date of Birth","Country")
treeview["show"]="headings"
s = ttk.Style(root)
s.theme_use("vista")
s.configure(".", font=('times new roman', 11))
s.configure("Treeview.Heading", foreground="red", font=("times new roman", 11, "bold"))

#adding columns


treeview.column('Name', width=50, minwidth=50,anchor=tk.CENTER)
treeview.column('Lastname', width=50, minwidth=50,anchor=tk.CENTER)
treeview.column('Occupation', width=50, minwidth=50,anchor=tk.CENTER)
treeview.column('date of Birth', width=50, minwidth=50,anchor=tk.CENTER)
treeview.column('Country', width=50, minwidth=50,anchor=tk.CENTER)

#adding heading
treeview.heading('Name', text='Name', anchor=CENTER)
treeview.heading('Lastname', text='Lastname', anchor=CENTER)
treeview.heading('Occupation', text='Occupation' ,anchor=CENTER)
treeview.heading('date of Birth', text='Date of Birth' ,anchor=CENTER)
treeview.heading('Country', text='Country' ,anchor=CENTER)
treeview.pack(side=TOP, fill=BOTH)
    
i = 0
for ro in row:
    treeview.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
    i = i+1
hsb = ttk.Scrollbar(root, orient="vertical")
hsb.configure(command=treeview.yview)
treeview.configure(yscrollcommand=hsb.set)
hsb.pack(fill=Y,side=RIGHT)

root.mainloop()