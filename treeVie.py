import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter import font
import pymysql
from tkinter import messagebox
#from tkcalendar import Calendar, DateEntry


root = Tk()
root.geometry("1500x800+0+0")
lab = Label(root, text="ADMINSTRATION PANEL",fg="red", font=("times new roman", 24,"bold"))
lab.place(x=600,y=10)

id_var = StringVar()
fname_var = StringVar()
lname_var = StringVar()
email_var =StringVar()
passw_var = StringVar()
occup_var = StringVar()



def searchs():
    con = pymysql.connect(host="localhost", user="root", password="", database="sufyan" )
    cur = con.cursor()
    cur.execute("select * from userinformations where id=%s",(searching.get()))
    
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
    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur = con.cursor()
    cur.execute("select * from employees where email=%s",email.get())
    row = cur.fetchone()
    if fname.get() == "" or lname.get() == "" or email.get()== "" or passrd.get() == "" or occup.get() == "":
        messagebox.showerror("Field Error"," All fields are required")
    else:
        if len(passrd.get()) < 8:
            messagebox.showerror("Password Error","Password must be contain 8 character ")
        else:
            if row == None:
                cur.execute("insert into employees(fname,lname,email,passwrd,occupation) values(%s,%s,%s,%s,%s)",(fname.get(),lname.get(),email.get(),passrd.get(),occup.get()))
                con.commit()
                con.close
                fname.delete(0,END)
                lname.delete(0,END)
                email.delete(0,END)
                passrd.delete(0,END)
                occup.delete(0,END)
                messagebox.showinfo("New User", "New user added successfully")
            else:
                messagebox.showerror("error","Already exist")
                email.config(fg="red")
                print(email.get(),"already exist")

            
    

def selected():
    
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
    
    
    
    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur = con.cursor()
    
    cur.execute("update employees set fname=%s,lname=%s,email=%s,passwrd=%s,occupation=%s where id=%s",(fname_var.get(),lname_var.get(),email_var.get(),passw_var.get(),occup_var.get(),id_var.get()))
    con.commit()
    con.close()    
    messagebox.showinfo("Record Updated", "Record updated successfully")
    
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)

def delt():
        
    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur = con.cursor()
    
    cur.execute("delete from employees where id=%s",(id_var.get()))
    
    con.commit()
    con.close()    
    messagebox.showinfo("Record Deleted", "Record deleted successfully")
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)




def TAB():
    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur = con.cursor()
    cur.execute("select * from employees")
    row = cur.fetchall()

    #connect = mysql.connector.connect(host="localhost", user="root",password="",database="sufyan")
    #conn= connect.cursor()
    #conn.execute("select * from user")
    #print(conn)

    treeview =ttk.Treeview(root,height=700)
    treeview["columns"]= ("Id","Name","Lastname","email","Password","Occupation")
    treeview["show"]="headings"
    s = ttk.Style(root)
    s.theme_use("vista")
    s.configure(".", font=('times new roman', 11))
    s.configure("Treeview.Heading", foreground="BLUE", font=("times new roman", 14, "bold"))

    #adding columns

    treeview.column('Id', width=5, minwidth=5,anchor=tk.CENTER)
    treeview.column('Name', width=30, minwidth=20,anchor=tk.CENTER)
    treeview.column('Lastname', width=30, minwidth=20,anchor=tk.CENTER)
    treeview.column('email', width=30, minwidth=30,anchor=tk.CENTER)
    treeview.column('Password', width=30, minwidth=30,anchor=tk.CENTER)
    treeview.column('Occupation', width=30, minwidth=30,anchor=tk.CENTER)

    #adding heading
    treeview.heading('Id', text='Id', anchor=CENTER)
    treeview.heading('Name', text='Name', anchor=CENTER)
    treeview.heading('Lastname', text='Lastname', anchor=CENTER)
    treeview.heading('email', text='Email' ,anchor=CENTER)
    treeview.heading('Password', text='Password' ,anchor=CENTER)
    treeview.heading('Occupation', text='Occupation' ,anchor=CENTER)
    #treeview.pack(side=TOP, fill=BOTH)

    treeview.place(x=0,y=100,width=900,height=500)

        
    i = 0
    for ro in row:
        treeview.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i = i+1
    hsb = ttk.Scrollbar(treeview, orient="vertical")
    hsb.configure(command=treeview.yview)
    treeview.configure(yscrollcommand=hsb.set)
    hsb.pack(fill=Y,side=RIGHT)



    ## order 
    treeview2 =ttk.Treeview(root,height=700)
    treeview2["columns"]= ("Id","Name","email","order","date")
    treeview2["show"]="headings"
    s = ttk.Style(root)
    s.theme_use("vista")
    s.configure(".", font=('times new roman', 11))
    s.configure("treeview2.Heading", foreground="BLUE", font=("times new roman", 14, "bold"))

    #adding columns

    treeview2.column('Id', width=5, minwidth=5,anchor=tk.CENTER)
    treeview2.column('Name', width=30, minwidth=20,anchor=tk.CENTER)
    treeview2.column('email', width=30, minwidth=30,anchor=tk.CENTER)
    treeview2.column('order', width=30, minwidth=30,anchor=tk.CENTER)
    treeview2.column('date', width=30, minwidth=30,anchor=tk.CENTER)

    #adding heading
    treeview2.heading('Id', text='Id', anchor=CENTER)
    treeview2.heading('Name', text='Name', anchor=CENTER)
    treeview2.heading('email', text='Email' ,anchor=CENTER)
    treeview2.heading('order', text='Order' ,anchor=CENTER)
    treeview2.heading('date', text='Date' ,anchor=CENTER)
    #treeview2.pack(side=TOP, fill=BOTH)

    treeview2.place(x=920,y=100,width=570,height=500)

        
    i = 0
    for ro in row:
        treeview2.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i = i+1
    hsb = ttk.Scrollbar(treeview2, orient="vertical")
    hsb.configure(command=treeview2.yview)
    treeview2.configure(yscrollcommand=hsb.set)
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

ent1 = Entry(root,textvariable=id_var,width=30)
ent1.place(x=10,y=670,height=30)
ent2 = Entry(root,width=30,textvariable=fname_var)
ent2.place(x=230,y=670,height=30)
ent3 = Entry(root,width=30,textvariable=lname_var)
ent3.place(x=10,y=710,height=30)
ent4 = Entry(root,width=30,textvariable=email_var)
ent4.place(x=230,y=710,height=30)
ent5 = Entry(root,width=30,textvariable=passw_var)
ent5.place(x=10,y=750,height=30)
ent6 = Entry(root,width=30,textvariable=occup_var)
ent6.place(x=230,y=750,height=30)

#Create New User
#cframe = Frame(root,width=420,height=590)
#cframe.place(x=1030,y=0)

Nlabel =Label(root, text="Create New User", font=("times new roman",24,"bold"),fg="green")
Nlabel.place(x=970,y=600)

#New user
firstname = Label(root, text="First Name : ", font=("times new roman",15),fg="blue")
firstname.place(x=700,y=670)
lastname = Label(root, text="Last Name : ", font=("times new roman",15),fg="blue")
lastname.place(x=700,y=710)
Eemail = Label(root, text="Email : ", font=("times new roman",15),fg="blue")
Eemail.place(x=700,y=750)
Epassword = Label(root, text="Password : ", font=("times new roman",15),fg="blue")
Epassword.place(x=1050,y=670)
Occupation = Label(root, text="Occupation : ", font=("times new roman",15),fg="blue")
Occupation.place(x=1050,y=710)

#new user entry
global fname
fname = Entry(root, font=("times new roman",15),fg="Gray")
fname.place(x=820,y=670)
global lname
lname = Entry(root, font=("times new roman",15),fg="gray")
lname.place(x=820,y=710)
global email
email = Entry(root, font=("times new roman",15),fg="gray")
email.place(x=820,y=750)
global passrd
passrd = Entry(root, font=("times new roman",15),fg="gray")
passrd.place(x=1180,y=670)
global occup
occup = Entry(root, font=("times new roman",15),fg="gray")
occup.place(x=1180,y=710)

#Create user button
rbtn = Button(root, text="REFRESH",fg="WHITE", bg="Green", command=TAB)
rbtn.place(x=500,y=620,width=70)
btn = Button(root, text="SELECTED", command=selected)
btn.place(x=500,y=670,width=70)
ubtn = Button(root, text="Update",bg="blue",fg="white", command=update)
ubtn.place(x=500,y=720,width=70)
Dbtn = Button(root, text="Delete",bg="red",fg="white", command=delt)
Dbtn.place(x=500,y=770,width=70)
Cbtn = Button(root, text="ADD USER",fg="WHITE", bg="blue",width=20, height=2, command=new)
Cbtn.place(x=1180,y=750)


TAB()






root.mainloop()