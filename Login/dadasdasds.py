import tkinter as tk
import mysql.connector
import os

os.system('cls')
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="cliniclick_db")
mycur = db.cursor()

def staff_login():
    global username_verify, password_verify, stlogin_main
    stlogin_main = tk.Tk()
    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    stlogin_main.title('CliniClick Staff Log-in')
    stlogin_main.geometry('525x300')

    stlogin_label = tk.Label(stlogin_main, text = 'Staff Log-in Portal', bg = 'sky blue', fg = 'black', font = ('bold', 18), width = 525)
    stlogin_label.pack()

    mt_label = tk.Label(stlogin_main, text = '')
    mt_label.pack()

    username_label = tk.Label(stlogin_main, text = 'Username: ', font = 'bold')
    username_entry = tk.Entry(stlogin_main, textvariable=username_verify)
    username_label.pack()
    username_entry.pack()

    password_label = tk.Label(stlogin_main, text='Password: ', font='bold')
    password_entry = tk.Entry(stlogin_main, textvariable=password_verify, show='*')
    password_label.pack()
    password_entry.pack()

    login_button = tk.Button(stlogin_main, text = 'Log in', command=stlogin_verify, font = ('bold', 18), bg='sky blue')
    login_button.pack(pady = 20)

    stlogin_main.mainloop() 

def stlogin_verify():
    stun_verify = username_verify.get()
    stpw_verify = password_verify.get()
    sql = "select * from stafftbl where staff_username = %s and staff_password = %s"
    mycur.execute(sql,[(stun_verify),(stpw_verify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            stlogin_success()
            break
    else:
        stlogin_failed()
    
def stlogin_failed():
    global fail
    fail = tk.Toplevel(stlogin_main)
    fail.title("Login Failed")
    fail.geometry("200x100")
    tk.Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    tk.Label(fail, text="").pack()
    tk.Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()
    
    def fail_destroy():
        fail.destroy()



def stlogin_success():
    loggedin_user = str(username_verify.get())
    mycur.execute("select staff_lastname from stafftbl where staff_username = " + "\'" + loggedin_user + "\'")
    result = mycur.fetchall()
    
    for row  in result :
        patient_lastname = "".join(row)

    global stloggedin_main
    stloggedin_main = tk.Toplevel(stlogin_main)
    stloggedin_main.title("Welcome")
    stloggedin_main.geometry("525x300")
    welcome_label = tk.Label(stloggedin_main, text="Welcome {} ".format(patient_lastname + "!"), fg="green", font="bold")
    welcome_label.pack()
    mema_label = tk.Label(stloggedin_main, text="")
    mema_label.pack()
    logout_btn = tk.Button(stloggedin_main, text='Log-Out', bg='grey', width=8, height=1, command=stloggedin_main_destroy)
    logout_btn.pack()

    login_button = tk.Button(stlogin_main, text = 'Log in', command=stlogin_verify, font = ('bold', 18), bg='sky blue')

def stloggedin_main_destroy():
    stloggedin_main.destroy()


staff_login()



