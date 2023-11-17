from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time

os.system('cls')
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="cliniclick_db")
mycur = db.cursor()

def staff_login_screen():
    global root3
    root3= Toplevel(root3)
    global username_varify
    global password_varify
    root3 = Tk()
    root3.title("Staff Log-in Portal")
    root3.geometry("300x300")
    Label(root3, text = "Welcome to Cliniclick Staff Log-In Portal", bg="grey", fg="black", font="bold", width=300).pack()
    username_varify  = StringVar()
    password_varify = StringVar()
    Label(root3, text="").pack
    Label(root3, text="Username :", font="bold").pack()
    Entry(root3, textvariable= username_varify).pack()
    Label(root3, text="").pack()
    Label(root3, text="Password :").pack()
    Entry(root3, textvariable=password_varify, show="*").pack()
    Label(root3, text="").pack()
    Button(root3, text="Log-In", bg="red",command=staff_login_varify).pack()
    Label(root3, text="")

def staff_login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from staffttbl where staff_username = %s and staff_password = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            staff_logged()
            break
    else:
        failed()

def staff_logged():
    new_user = str(username_varify.get())
    mycur.execute("select staff_lastname from stafftbl where staff_username = " + "\'" + new_user + "\'")
    result = mycur.fetchall()
    
    for row  in result :
        staff_lastname = "".join(row)
    
    global logg
    logg = Toplevel(root3)
    logg.title("Welcome")
    logg.geometry("300x100")
    Label(logg, text="Welcome {} ".format(staff_lastname + "!"), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Log-Out", bg="grey", width=8, height=1, command=logg_destroy).pack()

def failed():
    global fail
    fail = Toplevel(root3)
    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()

def logg_destroy():
    logg.destroy()
    root3.destroy()

def fail_destroy():
    fail.destroy()