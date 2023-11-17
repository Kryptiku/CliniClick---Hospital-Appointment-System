from tkinter import *
import mysql.connector
import os

os.system('cls')
db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'cliniclick_db')
mycur = db.cursor()

def error_destroy():
    error.destroy()

def success_destroy():
    success.destroy()
    root1.destroy()
    
def incomplete_error():
    global error
    error = Toplevel(root1)
    error.title('Error')
    error.geometry('200x100')
    label = Label(error, text = 'All fields are required', fg = 'red', font = 'calibri')
    button = Button(error, text = 'Ok', bg = 'grey', command = error_destroy)
    label.pack()
    button.pack()
    
def success():
    global success
    success = Toplevel(root1)
    success.title('Success')
    label = Label(success, text = 'Registration Successful', fg = 'green', font = 'bold')
    button = Button(success, text = 'Ok', bg = 'grey', command = success_destroy)
    label.pack()
    button.pack()
    
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
        incomplete_error()
    elif firstname_info == "":
        incomplete_error()
    elif middlename_info == "":
        incomplete_error()
    elif birthdate_info == "":
        incomplete_error()
    elif sex_info == "":
        incomplete_error()
    elif contact_info == "":
        incomplete_error()
    elif address_info == "":
        incomplete_error()
    elif username_info == "":
        incomplete_error()
    elif password_info == "":
        incomplete_error()    
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
        label = Label(root1, text ='')
        label.pack()
        success()
        
def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Cliniclick Registration Portal")
    root1.geometry('500x600')
    root1.grid_rowconfigure(0, weight=1)
    root1.columnconfigure(0, weight = 1)
    global lastname
    global firstname
    global middlename
    global birthdate
    global sex 
    global contact
    global address
    global username
    global password
    
    label = Label(root1, text = 'Register you account', bg = 'sky blue', fg = 'black', font = 'calibri', width = '400')
    label.grid(row = 0, column = 0)
    lastname = StringVar()
    firstname = StringVar()
    middlename = StringVar()
    birthdate = StringVar()
    sex = StringVar()
    contact = StringVar()
    address = StringVar()
    username = StringVar()
    password = StringVar()
    
    label_lastname = Label(root1, text="Last Name: ")
    entry_lastname = Entry(root1)
    label_lastname.grid(row= 1, column=0)
    entry_lastname.grid(row=2, column=1)

    label_firstname = Label(root1, text="First Name: ")
    entry_firstname = Entry(root1)
    label_firstname.grid(row=1, column=2)
    entry_firstname.grid(row=2, column=2)

    label_middlename = Label(root1, text="Middle Name: ")
    entry_middlename = Entry(root1)
    label_middlename.grid(row=1, column=3)
    entry_middlename.grid(row=2, column=3)

    label_birthdate = Label(root1, text="Birth Date: ")
    entry_birthdate = Entry(root1)
    label_birthdate.grid(row = 3, column = 1)
    entry_birthdate.grid(row = 3, column = 2)

    label_sex = Label(root1, text="Sex: ")
    entry_sex = Entry(root1)
    label_sex.grid(row = 4, column = 1)
    entry_sex.grid(row = 4, column = 2)

    label_contact = Label(root1, text="Contact Number: ")
    entry_contact = Entry(root1)
    label_contact.grid(row = 5, column = 1)
    entry_contact.grid(row = 5, column = 2)

    label_address = Label(root1, text="Address: ")
    entry_address = Entry(root1)
    label_address.grid(row = 6, column = 1)
    entry_address.grid(row = 6, column = 2)

    label_username = Label(root1, text="Username: ")
    entry_username = Entry(root1)
    label_username.grid(row = 7, column = 1)
    entry_username.grid(row = 7, column = 2)

    label_password = Label(root1, text="Password: ")
    entry_password = Entry(root1, show="*")  # Show '*' for password
    label_password.grid(row = 8, column = 1)
    entry_password.grid(row = 8, column = 2)

    button = Button(root1, text='Register', bg='sky blue', command=register_user)
    button.grid(row = 9, column = 1)
    
def login():
    global root2
    global username_verify
    global password_verify
    
    root2.title('Cliniclick Log-In Portal')
    root2.geometry('300x300')
    
    label = Label(root2, text = 'Cliniclick Log-In Portal', bg = 'grey', fg = 'black', font = 'bold')
    label.pack()
    
    
def main_screen():
    global root
    root = Tk()
    root.title('Cliniclick')
    root.geometry('500x300')
    label = Label(root, text = 'Welcom to Cliniclick Log-In Portal', font = 'calibri 24', bg = 'grey', fg = 'black', width = 300)
    label.pack()
    
    button = Button(root,text="Log-In",bg="sky blue",font="bold", command = login)
    button.pack()
    
    button = Button(root, text="Registration",bg="sky blue",font="bold",command = registration)
    button.pack()
    
    label = Label(root,text="Developed By Cliniclick")
    label.pack(side = 'bottom', pady = 5)
        
main_screen()
root.mainloop()
        
    
    
    
    
    
    
