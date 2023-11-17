import tkinter as tk
import mysql.connector
import os

os.system('cls')
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="cliniclick_db")
mycur = db.cursor()

def staff_login():
    global username_verify, password_verify, stlogin_main, username_entry, password_entry
    stlogin_main = tk.Tk()
    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    stlogin_main.title('CliniClick Staff Log-in')
    stlogin_main.geometry('525x300')

    stlogin_label = tk.Label(stlogin_main, text = 'Staff Log-in Portal', bg = 'sky blue', fg = 'black', font = ('bold', 18), width = 525)
    stlogin_label.pack()

    mt_label = tk.Label(stlogin_main, text = '')
    mt_label.pack()
    
    if failed_login == True:
        loginfail_label = tk.Label(stlogin_main, text = 'Invalid Credentials. Please try again.', fg = 'red', font = ('bold'))
        loginfail_label.pack(side = 'top')

    username_label = tk.Label(stlogin_main, text = 'Username: ', font = 'bold')
    username_entry = tk.Entry(stlogin_main, textvariable=username_verify)
    username_label.pack()
    username_entry.pack()

    password_label = tk.Label(stlogin_main, text='Password: ', font='bold')
    password_entry = tk.Entry(stlogin_main, textvariable=password_verify, show='*')
    password_label.pack()
    password_entry.pack()

    login_btn = tk.Button(stlogin_main, text = 'Log in', command=stlogin_verify, font = ('bold', 18), bg='sky blue')
    login_btn.pack(pady = 20)

    stlogin_main.mainloop() 

def stlogin_verify():
    stun_verify = username_verify.get()
    stpw_verify = password_verify.get()
    sql = "select * from stafftbl where staff_username = %s and staff_password = %s"
    mycur.execute(sql,[(stun_verify),(stpw_verify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            st_menu()
            break
    else:
        stlogin_failed()
    
def stlogin_failed():
    # global fail_main
    # fail_main = tk.Toplevel(stlogin_main)
    # fail_main.title("Login Failed")
    # fail_main.geometry("200x100")
    # tk.Label(fail_main, text="Invalid credentials...", fg="red", font="bold").pack()
    # loginfail_label = tk.Label(stlogin_main, text = 'Invalid Credentials. Please try again.', fg = 'red', font = ('bold'))
    # loginfail_label.pack(side = 'top')
    # tk.Label(fail_main, text="").pack()
    # tk.Button(fail_main, text="Ok", bg="grey", width=8, height=1, command=fail_main_destroy).pack()
    failed_login_true()
    staff_login_destroy()
    staff_login()



def st_menu():
    global stmenu_main
    stmenu_main = tk.Toplevel(stlogin_main)
    loggedin_user = str(username_verify.get())
    mycur.execute("select staff_lastname from stafftbl where staff_username = " + "\'" + loggedin_user + "\'")
    result = mycur.fetchall()
    
    for row  in result :
        staff_lastname = "".join(row)   

    failed_login_false()

    stmenu_main.title("Welcome")
    stmenu_main.geometry("525x300")
    welcome_label = tk.Label(stmenu_main, text="Welcome {} ".format(staff_lastname + "!"), fg="green", font="bold")
    welcome_label.pack()
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    mema_label = tk.Label(stmenu_main, text="")
    mema_label.pack()

    aptreq_btn = tk.Button(stmenu_main, text = 'Appointment Requests', font = ('bold', 18), bg='sky blue')
    aptreq_btn.pack(pady = 10)

    aptacpt_btn = tk.Button(stmenu_main, text = 'Accepted Appointments', font = ('bold', 18), bg='sky blue')
    aptacpt_btn.pack(pady = 10)

    logout_btn = tk.Button(stmenu_main, text='Log-Out', bg='grey', width=8, height=1, command=stmenu_main_destroy)
    logout_btn.pack()

# destroy mains functions
def stmenu_main_destroy():
    stmenu_main.destroy()

def staff_login_destroy():
    stlogin_main.destroy()

def failed_login_true():
    global failed_login
    failed_login = True
def failed_login_false():
    global failed_login
    failed_login = False

failed_login_false()
staff_login()



