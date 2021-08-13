from tkinter import filedialog
import mysql.connector
from mysql.connector import Error
import pymysql

def ctb(filename):
    with open(filename,'rb') as file:
        binarydata=file.read()
    return binarydata
def convertBTF(binarydata,filename):
    with open(filename,'wb')as file:
        file.write(binarydata)

host = "localhost"
user = "root"
password = ""
database = "example"


def openfile():
    global filepath
    filepath = filedialog.askopenfilename()
    
    file= open(filepath, 'rb').read()
openfile()
print(filepath)



try:
    convertPic = ctb(filepath)
    
    con = pymysql.connect(host="localhost", user="root", password="", database="example" )
    cur = con.cursor()
    
    cur.execute("insert into imgs (hello) value(%s)",(convertPic))
    con.commit()
    con.close()    
    
    
except Exception as e:
    print(e)