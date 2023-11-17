import tkinter as tk
import mysql.connector
import os

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

    login_btn = tk.Button(staff, text='Log in', command=stlogin_verify, font=('bold', 18), bg='sky blue')
    login_btn.pack(pady=20)

    staff.mainloop()

def stlogin_verify():
    stun_verify = username_verify.get()
    stpw_verify = password_verify.get()
    sql = "select * from stafftbl where staff_username = %s and staff_password = %s"
    mycur.execute(sql, [(stun_verify), (stpw_verify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            st_menu()
            break
    else:
        stlogin_failed()

def stlogin_failed():
    loginfail_label.config(text='Invalid Credentials. Please try again.')
    username_entry.delete(0, 'end'), password_entry.delete(0, 'end')

def st_menu():
    for widget in staff.winfo_children():
        widget.destroy()

    loggedin_user = str(username_verify.get())
    mycur.execute("select staff_lastname from stafftbl where staff_username = " + "\'" + loggedin_user + "\'")
    result = mycur.fetchall()

    for row in result:
        staff_lastname = "".join(row)

    welcome_label = tk.Label(staff, text="Welcome {} ".format(staff_lastname + "!"), fg="green", font="bold")
    welcome_label.pack()

    mema_label = tk.Label(staff, text="")
    mema_label.pack()

    aptreq_btn = tk.Button(staff, text='Appointment Requests', font=('bold', 18), bg='sky blue', command=st_blah)
    aptreq_btn.pack(pady=10)

    aptacpt_btn = tk.Button(staff, text='Accepted Appointments', font=('bold', 18), bg='sky blue')
    aptacpt_btn.pack(pady=10)

    logout_btn = tk.Button(staff, text='Log-Out', bg='grey', width=8, height=1, command=logout)
    logout_btn.pack()

def logout():
    staff.destroy()
    staff_login()
# Initialize the login window
staff_login()
