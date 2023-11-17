from tkinter import *
import mysql.connector
import os
import time

os.system('cls')
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="cliniclick_db")
mycur = db.cursor()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err,text="All fields are required..",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x200")
    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()

def register_user():
    lastname_info = lastname.get()
    firstname_info = firstname.get()
    middlename_info = middlename.get()
    birthdate_info = birthdate.get()
    sex_info = sex.get()
    contact_info = contact.get()
    address_info = address.get()
    username_info = username.get()
    password_info = password.get()
    
    if lastname_info == "":
        error()
    elif firstname_info == "":
        error()
    elif middlename_info == "":
        error()
    elif birthdate_info == "":
        error()
    elif sex_info == "":
        error()
    elif contact_info == "":
        error()
    elif address_info == "":
        error()
    elif username_info == "":
        error()
    elif password_info == "":
        error()    
    else:
        mycur.execute("select patient_code from patienttbl")
        mycur.fetchall()
        conv_rowcount = str(mycur.rowcount + 1)
        value = "00000000" 
        conv_rowcount = str(conv_rowcount)
        temp = len(conv_rowcount)
        modified_value = value[:-temp]
        db.commit()
        sql = "insert into patienttbl values (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
        t = ("PA" + modified_value + conv_rowcount, lastname_info, firstname_info, middlename_info, birthdate_info, sex_info, contact_info, address_info, username_info, password_info)
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        time.sleep(0.50)
        success()

def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration Portal")
    root1.geometry('300x300')
    global lastname
    global firstname
    global middlename
    global birthdate
    global sex 
    global contact
    global address
    global username
    global password
    Label(root1,text="Register your account",bg="sky blue",fg="black",font="bold",width=300).pack()
    lastname = StringVar()
    firstname = StringVar()
    middlename = StringVar()
    birthdate = StringVar()
    sex = StringVar()
    contact = StringVar()
    address = StringVar()
    username = StringVar()
    password = StringVar()
    
    Label(root1,text="").pack()
    label = Label(root1, text = "Last Name: ")
    entry = Entry(root1, textvariable = lastname)
    label.pack()
    entry.pack()
    
    Label(root1, text="").pack()
    Label(root1,text="First Name :").pack()
    Entry(root1,textvariable=firstname).pack()
    
    Label(root1, text="").pack()
    Label(root1,text="Middle Name :").pack()
    Entry(root1,textvariable=middlename).pack()
    
    Label(root1, text="").pack()
    Label(root1,text="Birth Date :").pack()
    Entry(root1,textvariable=birthdate).pack()
    
    Label(root1, text="").pack()
    Label(root1,text="Sex :").pack()
    Entry(root1,textvariable=sex).pack()
    
    Label(root1, text="").pack()
    Label(root1,text="Contact Number :").pack()
    Entry(root1,textvariable=contact).pack()
    
    Label(root1, text="").pack()
    Label(root1,text="Address :").pack()
    Entry(root1,textvariable=address).pack()
    
    Label(root1, text="").pack()
    Label(root1,text="Username :").pack()
    Entry(root1,textvariable=username).pack()
    
    Label(root1, text="").pack()
    Label(root1, text="Password :").pack()
    Entry(root1, textvariable=password,show="*").pack()
    
    Label(root1, text="").pack()
    Button(root1,text="Register",bg="sky blue",command=register_user).pack()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Log-In Portal")
    root2.geometry("300x300")
    global username_verify
    global password_verify
    Label(root2, text="Log-In Portal", bg="grey", fg="black", font="bold",width=300).pack()
    username_verify = StringVar()
    password_verify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", font="bold").pack()
    Entry(root2, textvariable=username_verify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :").pack()
    Entry(root2, textvariable=password_verify, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Log-In", bg="sky blue",command=login_verify).pack()
    Label(root2, text="")

def logg_destroy():
    logg.destroy()
    root2.destroy()

def fail_destroy():
    fail.destroy()

def logged():
    new_user = str(username_verify.get())
    mycur.execute("select patient_lastname from patienttbl where patient_username = " + "\'" + new_user + "\'")
    result = mycur.fetchall()
    
    for row  in result :
        patient_lastname = "".join(row)
    
    global logg
    logg = Toplevel(root2)
    logg.title("Welcome")
    logg.geometry("300x100")
    Label(logg, text="Welcome {} ".format(patient_lastname + "!"), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Log-Out", bg="grey", width=8, height=1, command=logg_destroy).pack()
    
def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()

def login_verify():
    user_verify = username_verify.get()
    pas_verify = password_verify.get()
    sql = "select * from patienttbl where patient_username = %s and patient_password = %s"
    mycur.execute(sql,[(user_verify),(pas_verify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()


def main_screen():
    global root
    root = Tk()
    root.title("Cliniclick")
    root.geometry("500x300")
    Label(root,text="Welcome to Cliniclick Log-In Portal",font="calibri 24",bg="grey",fg="black",width=300).pack()
    Label(root,text="").pack()
    Button(root,text="Log-In",width="8",height="1",bg="sky blue",font="bold",command=login).pack()
    Label(root,text="").pack()
    Button(root, text="Registration",height="1",width="15",bg="sky blue",font="bold",command=registration).pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    Label(root,text="Developed By Cliniclick").pack()

main_screen()
root.mainloop()