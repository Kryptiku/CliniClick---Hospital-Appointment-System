import tkinter as tk
from tkinter import ttk
import mysql.connector
import os
import Staff_Login_BE as sbe

os.system('cls')
db = mysql.connector.connect(host="localhost", user="root", passwd="", database="cliniclick_db")
mycur = db.cursor()

def staff_login():
    global staff, username_verify, password_verify, username_entry, password_entry, loginfail_label
    staff = tk.Tk()
    staff.title('CliniClick Staff Log-in')
    staff.geometry('525x300')
    
    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    stlogin_label = tk.Label(staff, text='Staff Log-in Portal', bg='sky blue', fg='black', font=('bold', 18),width=525)
    stlogin_label.pack()

    mt_label = tk.Label(staff, text='')
    mt_label.pack()

    loginfail_label = tk.Label(staff, text='', fg='red', font=('bold'))
    loginfail_label.pack(side='top')

    username_label = tk.Label(staff, text='Username: ', font='bold')
    username_entry = tk.Entry(staff, textvariable=username_verify)
    username_label.pack()
    username_entry.pack()

    password_label = tk.Label(staff, text='Password: ', font='bold')
    password_entry = tk.Entry(staff, textvariable=password_verify, show='*')
    password_label.pack()
    password_entry.pack()

    sbe.username_verify = username_verify
    sbe.password_verify = password_verify

    login_btn = tk.Button(staff, text='Log in', command=stlogin_verify, font=('bold', 18), bg='sky blue')
    login_btn.pack(pady=20)

    staff.mainloop()

def stlogin_verify():
    sbe.stlogin_verify_test()
    if sbe.results:
        for i in sbe.results:
            st_menu()
            break
    else:
        stlogin_failed()

def stlogin_failed():
    loginfail_label.config(text='Invalid Credentials. Please try again.')
    username_entry.delete(0, 'end'), password_entry.delete(0, 'end')

def st_menu():
    for child in staff.winfo_children():
        child.destroy()

    staff.title('Welcome!')

    sbe.loggedin_user = str(username_verify.get())
    sbe.getname()

    welcome_label = tk.Label(staff, text="Welcome {} ".format(sbe.staff_lastname + "!"), fg="green", font="bold")
    welcome_label.pack()

    mema_label = tk.Label(staff, text="")
    mema_label.pack()

    aptreq_btn = tk.Button(staff, text='Appointment Requests', font=('bold', 18), bg='sky blue', command=stappreq_main)
    aptreq_btn.pack(pady=10)

    aptacpt_btn = tk.Button(staff, text='Accepted Appointments', font=('bold', 18), bg='sky blue')
    aptacpt_btn.pack(pady=10)

    logout_btn = tk.Button(staff, text='Log-Out', bg='grey', width=8, height=1, command=logout)
    logout_btn.pack()

def stappreq_main():

    staff.geometry('700x500')

    for child in staff.winfo_children():
        child.destroy() 

    staff.title('Appointment Requests')
    
    mema_label = tk.Label(staff, text="")
    mema_label.pack()

    mycur.execute("SELECT a.apt_req_code, p.patient_lastname, p.patient_firstname, d.doctor_lastname, d.doctor_firstname FROM appointmentrequeststbl a INNER JOIN patienttbl p ON a.patient_code = p.patient_code INNER JOIN doctortbl d ON a.doctor_code = d.doctor_code")
    apt_req_data = mycur.fetchall()

    tree = ttk.Treeview(staff, show="headings")
    tree["columns"] = ("req_id", "ptntln", "ptntfn", "dctrln", "dctrfn")
    
    # Define column headings
    tree.heading("req_id", text="Request ID")
    tree.heading("ptntln", text="Patient Last Name")
    tree.heading("ptntfn", text="Patient First Name")
    tree.heading("dctrln", text="Doctor Last Name")
    tree.heading("dctrfn", text="Doctor First Name")

    for column in tree["columns"]:
        tree.column(column, anchor="w", width=125)
    
    for row in apt_req_data:
        tree.insert("", "end", values=row)
    tree.pack()


    # aptreq_btn = tk.Button(staff, text='Appointment Requests', font=('bold', 18), bg='sky blue')
    # aptreq_btn.pack(pady=10)

    # aptacpt_btn = tk.Button(staff, text='Accepted Appointments', font=('bold', 18), bg='sky blue')
    # aptacpt_btn.pack(pady=10)

    back_btn = tk.Button(staff, text='Back', bg='grey', width=8, height=1, command=st_menu)
    back_btn.pack(pady = 20)

def logout():
    staff.destroy()
    staff_login()

# Initialize the login window
staff_login()
