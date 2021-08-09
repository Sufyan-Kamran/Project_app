from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import mysql.connector
import io
import tkinter as tk
from tkinter import ttk
master= tk.Tk()
tree=ttk.Treeview(master)

tree["columns"]=("one","two","three")
tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree.column("one", width=150, minwidth=150, stretch=tk.NO)
tree.column("two", width=400, minwidth=200)
tree.column("three", width=80, minwidth=50, stretch=tk.NO)
tree.heading("#0",text="Name",anchor=tk.W)
tree.heading("one", text="Date modified",anchor=tk.W)
tree.heading("two", text="Type",anchor=tk.W)
tree.heading("three", text="Size",anchor=tk.W)
tree.pack(side=tk.TOP,fill=tk.X)


master.mainloop()