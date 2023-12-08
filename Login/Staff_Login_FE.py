import customtkinter as tk
from tkinter import ttk
import os
import Staff_Login_BE as sbe

os.system('cls')

# class LoginFrontEnd:
#     def __init__ (self):
#         self.staff = tk.CTk()
#         self.staff.title('CliniClick Staff Log-in')
#         self.staff.geometry('525x300')
#         self.my_font = ('bold', 18)

#     def staff_login(self):                                                                                                                                   # LOGIN WINDOW   
#         global staff, username_verify, password_verify, username_entry, password_entry, loginfail_label
        
#         username_verify = tk.StringVar()
#         password_verify = tk.StringVar()

#         stlogin_label = tk.CTkLabel(self.staff, text='Staff Log-in Portal', fg_color='black', width=525)
#         mt_label = tk.CTkLabel(self.staff, text='')
#         loginfail_label = tk.CTkLabel(self.staff, text='', font = self.my_font)
#         username_label = tk.CTkLabel(self.staff, text='Username: ')
#         username_entry = tk.CTkEntry(self.staff, textvariable=username_verify)
#         password_label = tk.CTkLabel(self.staff, text='Password: ')
#         password_entry = tk.CTkEntry(self.staff, textvariable=password_verify, show='*')
#         login_btn = tk.CTkButton(self.staff, text='Log in', command=self.stlogin_verify)

#         sbe.username_verify = username_verify
#         sbe.password_verify = password_verify
        
#         stlogin_label.pack()
#         mt_label.pack()
#         loginfail_label.pack(side='top')
#         username_label.pack()
#         username_entry.pack()
#         password_label.pack()
#         password_entry.pack()
#         login_btn.pack(pady=20)

#         self.staff.mainloop()

# class LoginFunctionManager(LoginFrontEnd): #self
#     def __init__ (self, LoginFrontEnd):
#         super().__init__()
#         self.loginfail_label = LoginFrontEnd.loginfail_label
#         self.username_entry = LoginFrontEnd.username_entry

#     def stlogin_verify(self):
#         sbe.stlogin_verify_test()
#         if sbe.results:
#             for i in sbe.results:
#                 st_menu()
#                 break
#         else:
#             stlogin_failed()
        
#     def stlogin_failed(self):
#         self.loginfail_label.configure(text='Invalid Credentials. Please try again.')
#         username_entry.delete(0, 'end'), password_entry.delete(0, 'end')


#     def stlogin_failed(self):
#         loginfail_label.configure(text='Invalid Credentials. Please try again.')
#         username_entry.delete(0, 'end'), password_entry.delete(0, 'end')

class LoginFrontEnd:
    def __init__(self):
        self.staff = tk.CTk()
        self.staff.title('CliniClick Staff Log-in')
        self.staff.geometry('525x300')
        self.my_font = ('bold', 18)

    def staff_login(self):  # LOGIN WINDOW
        global username_verify, password_verify, username_entry, password_entry, loginfail_label
        username_verify = tk.StringVar()
        password_verify = tk.StringVar()

        stlogin_label = tk.CTkLabel(self.staff, text='Staff Log-in Portal', fg_color='black', width=525)
        mt_label = tk.CTkLabel(self.staff, text='')
        loginfail_label = tk.CTkLabel(self.staff, text='', font=self.my_font)
        username_label = tk.CTkLabel(self.staff, text='Username: ')
        username_entry = tk.CTkEntry(self.staff, textvariable=username_verify)
        password_label = tk.CTkLabel(self.staff, text='Password: ')
        password_entry = tk.CTkEntry(self.staff, textvariable=password_verify, show='*')
        login_btn = tk.CTkButton(self.staff, text='Log in', command=self.stlogin_verify)

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

        self.staff.mainloop()

    def stlogin_verify(self):
        sbe.stlogin_verify_test()
        if sbe.results:
            for i in sbe.results:
                st_menu()
                break
        else:
            self.stlogin_failed()

    def stlogin_failed(self):
        self.loginfail_label.configure(text='Invalid Credentials. Please try again.')
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')


class LoginFunctionManager(LoginFrontEnd):
    def __init__(self, login_frontend):
        super().__init__()
        self.loginfail_label = login_frontend.loginfail_label
        self.username_entry = login_frontend.username_entry

    def stlogin_failed(self):
        super().stlogin_failed()
        # Additional functionality for login failure, if needed


def st_menu():                                                                                                                                    # MAIN MENU WINDOW
    lfe.staff.geometry('525x300')
    for child in lfe.staff.winfo_children():
        child.destroy()

    lfe.staff.title('Welcome!')

    sbe.loggedin_user = str(username_verify.get())
    sbe.getname()
    welcome_label = tk.CTkLabel(lfe.staff, text="Welcome {} ".format(sbe.staff_lastname + ", " + sbe.staff_firstname + "!"), fg_color="green")
    mema_label = tk.CTkLabel(lfe.staff, text="")
    aptreq_btn = tk.CTkButton(lfe.staff, text='Appointment Requests', command=stappreq_main)
    aptacpt_btn = tk.CTkButton(lfe.staff, text='Accepted Appointments', command = staccepted_apts_main)
    logout_btn = tk.CTkButton(lfe.staff, text='Log-Out', bg_color='grey', width=8, height=1, command=logout)
    

    welcome_label.pack()
    mema_label.pack()
    aptreq_btn.pack(pady=10)
    aptacpt_btn.pack(pady=10)
    logout_btn.pack()

def stappreq_main():                                                                                                            # APPOINTMENT REQUESTS WINDOW
    for child in lfe.staff.winfo_children():
        child.destroy()
    
    sbe.getaptreq()
    lfe.staff.title('Appointment Requests')
    lfe.staff.geometry('700x650')
    mema_label = tk.CTkLabel(lfe.staff, text="")
    mema_label.pack()

    global tree
    tree_frame = tk.CTkFrame(lfe.staff)
    tree_frame.pack()
    tree = ttk.Treeview(tree_frame, show="headings")
    tree["columns"] = ("req_id", "ptntln", "ptntfn", "dctrln", "dctrfn")
    
    bg_color = lfe.staff._apply_appearance_mode(tk.ThemeManager.theme["CTkFrame"]["fg_color"])
    text_color = lfe.staff._apply_appearance_mode(tk.ThemeManager.theme["CTkLabel"]["text_color"])

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

    accept_label = tk.CTkLabel(lfe.staff, text = 'Accept appointment: ')
    accept_label.pack(pady = 5)
    
    sbe.ardropdownobj()
    global options
    options = tk.CTkComboBox(lfe.staff, values = sbe.ar_options, variable = "", command=changear_entries)
    options.place(relx=0.5, rely=0.5, anchor = 'center')
    options.pack()

    global choice_label
    choice_label = tk.CTkLabel(lfe.staff, text = "")
    choice_label.pack()

    global time, date, entry_time, entry_date
    time = tk.StringVar()
    label_time = tk.CTkLabel(lfe.staff, text='Time (HH:MM AM/PM): ')
    entry_time = tk.CTkEntry(lfe.staff, textvariable = time)

    date = tk.StringVar()
    label_date = tk.CTkLabel(lfe.staff, text='Date (YYYY-MM-DD): ')
    entry_date = tk.CTkEntry(lfe.staff, textvariable = date)
    
    label_time.pack()
    entry_time.pack()
    label_date.pack()
    entry_date.pack()

    global aptaccepted_label
    aptaccepted_label = tk.CTkLabel(lfe.staff, text = "")
    aptaccepted_label.pack(pady = 10)
    
    acceptapt_btn = tk.CTkButton(lfe.staff, text = "Accept Appointment", command = verify_appointment)
    acceptapt_btn.pack(pady = 10)

    back_btn = tk.CTkButton(lfe.staff, text='Back', bg_color='grey', width=8, height=1, command=st_menu)
    back_btn.pack(pady = 20)

def staccepted_apts_main():                                                                                                             # ACCEPTED APPOINTMENTS WINDOW
    for child in lfe.staff.winfo_children():
        child.destroy()

    sbe.getacceptedapts()
    lfe.staff.title('Accepted Appointments')
    lfe.staff.geometry('920x700')
    mema_label = tk.CTkLabel(lfe.staff, text="")
    mema_label.pack()

    global acctree
    tree_frame = tk.CTkFrame(lfe.staff)
    tree_frame.pack()
    acctree = ttk.Treeview(tree_frame, show="headings")
    acctree["columns"] = ("req_id", "ptntln", "ptntfn", "dctrln", "dctrfn", "aptdate", "apttime")
    
    bg_color = lfe.staff._apply_appearance_mode(tk.ThemeManager.theme["CTkFrame"]["fg_color"])
    text_color = lfe.staff._apply_appearance_mode(tk.ThemeManager.theme["CTkLabel"]["text_color"])

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)

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

    update_label = tk.CTkLabel(lfe.staff, text = 'Update or Delete appointment: ')
    update_label.pack(pady = 5)

    sbe.aadropdownobj()
    global update_options
    update_options = tk.CTkComboBox(lfe.staff, values = sbe.aa_options, variable = "", command=changeaa_entries)
    update_options.place(relx=0.5, rely=0.5, anchor = 'center')
    update_options.pack()

    global updchoice_label, update_time, update_date, entry_time, entry_date
    updchoice_label = tk.CTkLabel(lfe.staff, text = "")
    updchoice_label.pack()

    update_time = tk.StringVar()
    label_time = tk.CTkLabel(lfe.staff, text='Time (HH:MM AM/PM): ')
    entry_time = tk.CTkEntry(lfe.staff, textvariable = update_time)

    update_date = tk.StringVar()
    label_date = tk.CTkLabel(lfe.staff, text='Date (YYYY-MM-DD): ')
    entry_date = tk.CTkEntry(lfe.staff, textvariable = update_date)
    
    label_time.pack()
    entry_time.pack()
    label_date.pack()
    entry_date.pack()

    global updateapt_label
    updateapt_label = tk.CTkLabel(lfe.staff, text = "")
    updateapt_label.pack(pady = 5)

    update_btn = tk.CTkButton(lfe.staff, text = 'Update Appointment', command = verify_update)
    done_btn = tk.CTkButton(lfe.staff, text = 'Appointment Done', command = verify_done)
    delete_btn = tk.CTkButton(lfe.staff, text = "Delete Appointment", command = delete_appointment)
    update_btn.pack(padx = 5, pady = 5)
    done_btn.pack(padx = 5, pady = 5)
    delete_btn.pack(pady = 5)
    
    back_btn = tk.CTkButton(lfe.staff, text='Back', bg_color='grey', width=8, height=1, command=st_menu)
    back_btn.pack(pady = 20)

def verify_done():
    if update_options.get() == "":
        updchoice_label.configure(text = "Choose an appointment.")
    else:
        appointment_done()

def appointment_done():                                                                                                                   # APPOINTMENT DONE
    global aptdone, diagnosis, meds_cb, dosage, frequency, diagnosis_entry, dosage_entry, frequency_entry, error_label
    aptdone = tk.CTkToplevel(lfe.staff)
    aptdone.attributes('-top', True)
    aptdone.title("Appointment Done")
    aptdone.geometry("400x420")

    sbe.medsdropdownobj()
    diagnosis = tk.StringVar()
    dosage = tk.StringVar()
    frequency = tk.StringVar()
    
    diagnosis_label = tk.CTkLabel(aptdone, text = "Diagnosis:")
    diagnosis_entry = tk.CTkEntry(aptdone, textvariable = diagnosis)
    meds_label = tk.CTkLabel(aptdone, text = "Medicine:")
    meds_cb = tk.CTkComboBox(aptdone, values = sbe.meds_options, variable = "")
    dosage_label = tk.CTkLabel(aptdone, text = "Dosage:")
    dosage_entry = tk.CTkEntry(aptdone, textvariable = dosage)
    frequency_label = tk.CTkLabel(aptdone, text = "Frequency:")
    frequency_entry = tk.CTkEntry(aptdone, textvariable = frequency)

    diagnosis_label.pack(pady=2)
    diagnosis_entry.pack(pady=2)
    meds_label.pack(pady=2)
    meds_cb.pack(pady=2)
    dosage_label.pack(pady=2)
    dosage_entry.pack(pady=2)
    frequency_label.pack(pady=2)
    frequency_entry.pack(pady=2)

    error_label = tk.CTkLabel(aptdone, text = "")
    error_label.pack()
    
    enter_btn = tk.CTkButton(aptdone, text = "Enter", command = enter_done)
    enter_btn.pack()

    back_btn = tk.CTkButton(aptdone, text = "Back", command = aptdone.destroy)
    back_btn.pack(pady=2)

def changear_entries(choice):
    global show_acptdapt
    show_acptdapt = choice
    sbe.choice = str(choice)
    sbe.changear_entries()
    choice_label.configure(text = "Patient: " + sbe.ptntfn + " " + sbe.ptntln + "    ||    " + "Doctor: " + sbe.dctrfn + " " + sbe.dctrln)
    
def verify_appointment():
    if options.get() == "":
        choice_label.configure(text = "Choose an appointment.")
    else:
        sbe.timeanddate_validation(time.get(), date.get())
        if sbe.error_time==True or sbe.error_date==True:
            declineappointment()
        else:
            acceptappointment()

def declineappointment():
    aptfail = tk.CTkToplevel(lfe.staff)
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
    sbe.ardropdownobj()
    options.set('')
    options.configure(values = sbe.ar_options, variable = "")
    entry_time.delete(0, 'end'), entry_date.delete(0, 'end')

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
    
def changeaa_entries(aachoice):
    global show_updtdapt
    show_updtdapt = aachoice
    sbe.aachoice = str(aachoice)
    sbe.changeaa_entries()
    updchoice_label.configure(text = "Patient: " + sbe.aaptntfn + " " + sbe.aaptntln + "    ||    " + "Doctor: " + sbe.aadctrfn + " " + sbe.aadctrln)

def verify_update():
    if update_options.get() == "":
        updateapt_label.configure(text = "Choose an appointment.")
    else:
        sbe.timeanddate_validation(update_time.get(), update_date.get())
        if sbe.error_time==True or sbe.error_date==True:
            declineupdate()
        else:
            update_appointment()

def declineupdate():
    updfail = tk.CTkToplevel(lfe.staff)
    updfail.attributes('-top', True)
    updfail.title("Error!")
    updfail.geometry('200x200')

    fail_message = tk.CTkLabel(updfail, text = 'Failed to accept appointment. \nPlease check the inputted values', text_color = 'pink')
    fail_message.pack(pady = 10)

    okbtn = tk.CTkButton(updfail, text = 'Okay', command=updfail.destroy)
    okbtn.pack()

def update_appointment():
    sbe.update_appointment()
    updateapt_label.configure(text = "Appointment Updated: " + show_updtdapt)
    acceptedapt_current_treeview()
    sbe.aadropdownobj()
    update_options.set('')
    update_options.configure(values = sbe.aa_options, variable = "")
    entry_time.delete(0, 'end'), entry_date.delete(0, 'end')

def delete_appointment():
    sbe.delete_appointment()
    updateapt_label.configure(text = "Appointment Deleted: " + show_updtdapt)
    acceptedapt_current_treeview()
    sbe.aadropdownobj()
    update_options.set('')
    update_options.configure(values = sbe.aa_options, variable = "")
    entry_time.delete(0, 'end'), entry_date.delete(0, 'end')

def enter_done():
    if meds_cb.get() == "" or diagnosis.get() == "" or dosage.get() == "" or frequency.get() == "":
        error_label.configure(text = "Error. Null values entered.")
        diagnosis_entry.delete(0, 'end'), dosage_entry.delete(0, 'end'), frequency_entry.delete(0, 'end')
        meds_cb.configure(variable = "")
    else:
        sbe.enter_done(diagnosis.get(), meds_cb.get(), dosage.get(), frequency.get())
        aptdone.destroy()
        updateapt_label.configure(text = "Appointment Done: " + show_updtdapt)

def logout():
    lfe.staff.destroy()
    lfe.staff_login()

# Initialize the login window
lfe = LoginFrontEnd()
lfe.staff_login()