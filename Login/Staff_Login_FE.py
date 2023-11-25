import customtkinter as tk
from tkinter import ttk
import tkinter
import os
import Staff_Login_BE as sbe

os.system('cls')

def staff_login():                                           # LOGIN WINDOW   
    global staff, username_verify, password_verify, username_entry, password_entry, loginfail_label
    staff = tk.CTk()
    staff.title('CliniClick Staff Log-in')
    staff.geometry('525x300')
    my_font = ('bold', 18)
    
    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    stlogin_label = tk.CTkLabel(staff, text='Staff Log-in Portal', fg_color='black', width=525)
    mt_label = tk.CTkLabel(staff, text='')
    loginfail_label = tk.CTkLabel(staff, text='', font = my_font)
    username_label = tk.CTkLabel(staff, text='Username: ')
    username_entry = tk.CTkEntry(staff, textvariable=username_verify)
    password_label = tk.CTkLabel(staff, text='Password: ')
    password_entry = tk.CTkEntry(staff, textvariable=password_verify, show='*')
    login_btn = tk.CTkButton(staff, text='Log in', command=stlogin_verify)

    sbe.username_verify = username_verify
    sbe.password_verify = password_verify
    
    stlogin_label.pack()
    mt_label.pack()
    loginfail_label.pack(side='top')
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
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
    loginfail_label.configure(text='Invalid Credentials. Please try again.')
    username_entry.delete(0, 'end'), password_entry.delete(0, 'end')

def st_menu():                                          # MAIN MENU WINDOW
    staff.geometry('525x300')
    for child in staff.winfo_children():
        child.destroy()

    staff.title('Welcome!')

    sbe.loggedin_user = str(username_verify.get())
    sbe.getname()
    welcome_label = tk.CTkLabel(staff, text="Welcome {} ".format(sbe.staff_lastname + ", " + sbe.staff_firstname + "!"), fg_color="green")
    mema_label = tk.CTkLabel(staff, text="")
    aptreq_btn = tk.CTkButton(staff, text='Appointment Requests', command=stappreq_main)
    aptacpt_btn = tk.CTkButton(staff, text='Accepted Appointments', command = accepted_appointments)
    logout_btn = tk.CTkButton(staff, text='Log-Out', bg_color='grey', width=8, height=1, command=logout)
    

    welcome_label.pack()
    mema_label.pack()
    aptreq_btn.pack(pady=10)
    aptacpt_btn.pack(pady=10)
    logout_btn.pack()

def stappreq_main():                                    # APPOINTMENT REQUESTS WINDOW
    for child in staff.winfo_children():
        child.destroy()
    
    sbe.getaptreq()
    staff.title('Appointment Requests')
    staff.geometry('700x650')
    mema_label = tk.CTkLabel(staff, text="")
    mema_label.pack()

    global tree
    tree_frame = tk.CTkFrame(staff)
    tree_frame.pack()
    tree = ttk.Treeview(tree_frame, show="headings")
    tree["columns"] = ("req_id", "ptntln", "ptntfn", "dctrln", "dctrfn")
    
    bg_color = staff._apply_appearance_mode(tk.ThemeManager.theme["CTkFrame"]["fg_color"])
    text_color = staff._apply_appearance_mode(tk.ThemeManager.theme["CTkLabel"]["text_color"])

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)

    # Define column headings
    tree.heading("req_id", text="Request ID")
    tree.heading("ptntln", text="Patient Last Name")
    tree.heading("ptntfn", text="Patient First Name")
    tree.heading("dctrln", text="Doctor Last Name")
    tree.heading("dctrfn", text="Doctor First Name")

    for column in tree["columns"]:
        tree.column(column, anchor="w", width=125)
    
    aptreq_current_treeview()
    tree.pack(side = "left", fill="both", expand=True)

    accept_label = tk.CTkLabel(staff, text = 'Accept appointment: ')
    accept_label.pack(pady = 5)
    
    sbe.dropdownobj()
    options = tk.CTkComboBox(master = staff, values = sbe.ar_options, variable = "", command=changear_entries)
    options.place(relx=0.5, rely=0.5, anchor = 'center')
    options.pack()

    global choice_label
    choice_label = tk.CTkLabel(staff, text = "")
    choice_label.pack()

    global time, date
    time = tk.StringVar()
    label_time = tk.CTkLabel(staff, text='Time (HH:MM AM/PM): ')
    entry_time = tk.CTkEntry(staff, textvariable = time)

    date = tk.StringVar()
    label_date = tk.CTkLabel(staff, text='Date (YYYY-MM-DD): ')
    entry_date = tk.CTkEntry(staff, textvariable = date)
    
    label_time.pack()
    entry_time.pack()
    label_date.pack()
    entry_date.pack()

    global aptaccepted_label
    aptaccepted_label = tk.CTkLabel(staff, text = "")
    aptaccepted_label.pack(pady = 10)
    
    acceptapt_btn = tk.CTkButton(staff, text = "Accept Appointment", command = verify_appointment)
    acceptapt_btn.pack(pady = 10)

    back_btn = tk.CTkButton(staff, text='Back', bg_color='grey', width=8, height=1, command=st_menu)
    back_btn.pack(pady = 20)

def accepted_appointments():                    # ACCEPTED APPOINTMENTS WINDOW
    for child in staff.winfo_children():
        child.destroy()
    staff.title('Accepted Appointments')
    staff.geometry('920x650')
    mema_label = tk.CTkLabel(staff, text="")
    mema_label.pack()
    sbe.getacceptedapts()

    global acctree
    tree_frame = tk.CTkFrame(staff)
    tree_frame.pack()
    acctree = ttk.Treeview(tree_frame, show="headings")
    acctree["columns"] = ("req_id", "ptntln", "ptntfn", "dctrln", "dctrfn", "aptdate", "apttime")
    
    bg_color = staff._apply_appearance_mode(tk.ThemeManager.theme["CTkFrame"]["fg_color"])
    text_color = staff._apply_appearance_mode(tk.ThemeManager.theme["CTkLabel"]["text_color"])

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)

    # Define column headings
    acctree.heading("req_id", text="Request ID")
    acctree.heading("ptntln", text="Patient Last Name")
    acctree.heading("ptntfn", text="Patient First Name")
    acctree.heading("dctrln", text="Doctor Last Name")
    acctree.heading("dctrfn", text="Doctor First Name")
    acctree.heading("aptdate", text="Date")
    acctree.heading("apttime", text="Time")

    for column in acctree["columns"]:
        acctree.column(column, anchor="w", width=125)
    
    acceptedapt_current_treeview()
    acctree.pack(side = "left", fill="both", expand=True)

    

def logout():
    staff.destroy()
    staff_login()

def changear_entries(choice):
    global show_acptdapt
    show_acptdapt = choice
    sbe.choice = str(choice)
    sbe.changear_entries()
    choice_label.configure(text = "Patient: " + sbe.ptntfn + " " + sbe.ptntln + "    ||    " + "Doctor: " + sbe.dctrfn + " " + sbe.dctrln)
    
def verify_appointment():
    sbe.acceptapt_validation(time.get(), date.get())
    if sbe.error_time==True or sbe.error_date==True:
        declineappointment()
    else:
        acceptappointment()

def declineappointment():
    global aptfail
    aptfail = tk.CTkToplevel(staff)
    aptfail.attributes('-top', True)
    aptfail.title("Error!")
    aptfail.geometry('200x200')

    fail_message = tk.CTkLabel(aptfail, text = 'Failed to accept appointment. \nPlease check the inputted values', text_color = 'pink')
    fail_message.pack(pady = 10)

    okbtn = tk.CTkButton(aptfail, text = 'Okay', command=aptfail.destroy)
    okbtn.pack(pady = 50)

def acceptappointment():
    sbe.acceptappointment()
    aptaccepted_label.configure(text = "Appointment Accepted: " + show_acptdapt)
    aptreq_current_treeview()

def aptreq_current_treeview():
    sbe.getaptreq()
    tree.delete(*tree.get_children())
    for row in sbe.apt_req_data:
        tree.insert("", "end", values=row)

def acceptedapt_current_treeview():
    sbe.getacceptedapts()
    acctree.delete(*acctree.get_children())
    for row in sbe.acceptedapts:
        acctree.insert("", "end", values=row)
    
    
# Initialize the login window
staff_login()
