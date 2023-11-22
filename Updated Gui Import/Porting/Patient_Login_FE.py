import customtkinter as tk
import Patient_Login_BE as pbe

tk.set_appearance_mode('System')
tk.set_default_color_theme('blue')

def patient_main_screen():
    global main_screen 
    main_screen = tk.CTk()
    main_screen.title('Cliniclick')
    main_screen.geometry('525x200')
    # main_screen.attributes('-topmost', True)
    
    welcome_label = tk.CTkLabel(main_screen, text = 'Welcom to the Cliniclick Log-In Portal')
    login_button = tk.CTkButton(main_screen, text = 'Log-In', command = patient_login)
    register_button = tk.CTkButton(main_screen, text = 'Register', command = patient_registration)
    footer_label = tk.CTkLabel(main_screen, text = 'Developed By Cliniclick™')
    
    welcome_label.pack()
    login_button.pack(pady = 15)
    register_button.pack()
    footer_label.pack(side = 'bottom', pady = 5)
    
    main_screen.mainloop()

def patient_login():
    for child in main_screen.winfo_children():
        child.destroy()
    
    global username, password
    username = tk.StringVar()
    password = tk.StringVar()
    
    main_screen.title('Log-In Portal')
    main_screen.geometry('525x225')
    login_label = tk.CTkLabel(main_screen, text = 'Log-In Portal')
    username_label = tk.CTkLabel(main_screen, text = 'Username: ')
    username_entry = tk.CTkEntry(main_screen, textvariable = username)
    
    password_label = tk.CTkLabel(main_screen, text = 'Password: ')
    password_entry = tk.CTkEntry(main_screen, textvariable = password, show = '*')
    
    login_button = tk.CTkButton(main_screen, text = 'Log-In',command = patient_login_verify)
    
    login_label.pack(pady = 10)
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    login_button.pack(pady = 10)
    
def patient_registration():
    global lastname
    global firstname
    global middlename
    global birthdate
    global sex 
    global contact
    global address
    global username
    global password
    global registration_main
    global entry_birthdate
    global registration_main
    
    registration_main = tk.CTkToplevel(main_screen)
    # registration_main.attributes('-topmost', True)
    registration_main.title('Registration Portal')
    registration_main.geometry()
    
    lastname = tk.StringVar()
    firstname = tk.StringVar()
    middlename = tk.StringVar()
    birthdate = tk.StringVar()
    sex = tk.StringVar()
    contact = tk.StringVar()
    address = tk.StringVar()
    username = tk.StringVar()
    password = tk.StringVar()   
    
    title_label = tk.CTkLabel(registration_main, text = 'Register your account', width = 35)
    title_label.grid(row = 0, columnspan = 3, pady = 10, sticky = 'n')

    label_lastname = tk.CTkLabel(registration_main, text = 'Last Name:')
    entry_lastname = tk.CTkEntry(registration_main, textvariable = lastname)
    label_lastname.grid(row = 1, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_lastname.grid(row = 1, column = 1, pady  =5, padx = 5)

    label_firstname = tk.CTkLabel(registration_main, text = 'First Name:')
    entry_firstname = tk.CTkEntry(registration_main, textvariable = firstname)
    label_firstname.grid(row = 2, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_firstname.grid(row = 2, column = 1, pady = 5, padx = 5)
    
    label_middlename = tk.CTkLabel(registration_main, text = 'Middle Name: ')
    entry_middlename = tk.CTkEntry(registration_main, textvariable = middlename)
    label_middlename.grid(row = 3, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_middlename.grid(row = 3, column = 1, pady = 5, padx = 5)

    label_birthdate = tk.CTkLabel(registration_main, text = 'Birth Date: ')
    entry_birthdate = tk.CTkEntry(registration_main, textvariable = birthdate)
    button_birthdate = tk.CTkButton(registration_main, text = 'Select Date')
    label_birthdate.grid(row = 4, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_birthdate.grid(row = 4, column = 1, pady = 5, padx = 5)
    button_birthdate.grid(row = 4, column = 2, sticky = 'w', padx = 5)

    label_sex = tk.CTkLabel(registration_main, text = 'Sex: ')
    entry_sex = tk.CTkEntry(registration_main, textvariable = sex)
    label_sex.grid(row = 5, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_sex.grid(row = 5, column = 1, pady = 5, padx = 5)

    label_contact = tk.CTkLabel(registration_main, text = 'Contact Number: ')
    entry_contact = tk.CTkEntry(registration_main, textvariable = contact)
    label_contact.grid(row = 6, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_contact.grid(row = 6, column = 1, pady = 5, padx = 5)

    label_address = tk.CTkLabel(registration_main, text='Address: ')
    entry_address = tk.CTkEntry(registration_main, textvariable = address)
    label_address.grid(row = 7, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_address.grid(row = 7, column = 1, pady = 5, padx = 5)

    label_username = tk.CTkLabel(registration_main, text = 'Username: ')
    entry_username = tk.CTkEntry(registration_main, textvariable = username)
    label_username.grid(row = 8, column = 0, sticky ='e', pady = 5, padx = 5)
    entry_username.grid(row = 8, column = 1, pady = 5, padx = 5)

    label_password = tk.CTkLabel(registration_main, text = 'Password: ')
    entry_password = tk.CTkEntry(registration_main, textvariable = password, show = '*')
    label_password.grid(row = 9, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_password.grid(row = 9, column = 1, pady = 5, padx = 5)

    register_button = tk.CTkButton(registration_main, text = 'Register', command = register_verify)
    register_button.grid(row = 10, columnspan = 3, sticky = 's', pady = 10)

    # registration_main.mainloop()

def register_verify():
    pbe.register_user(lastname.get(), firstname.get(), middlename.get(), birthdate.get(), sex.get(), contact.get(), address.get(), username.get(), password.get())
    
def patient_login_verify():
    pbe.palogin_verify_test(username.get(), password.get())
    if pbe.results:
        for i in pbe.results:
            login_main()
            
            break
    else:
        pbe.login_failed()
        
def login_main():
    for child in main_screen.winfo_children():
        child.destroy()
        
    main_screen.title('Welcome')
    main_screen.geometry('525x300')
    welcome_label = tk.CTkLabel(main_screen, text = 'Welcome {} '.format(pbe.patient_lastname + '!'))
    appointment_button = tk.CTkButton(main_screen, text = 'Register Appointment', command = register_appointment)
    history_button = tk.CTkButton(main_screen, text = 'View History')
    prescription_button = tk.CTkButton(main_screen, text = 'View Prescrptions')
    log_out_button = tk.CTkButton(main_screen, text = 'Log-Out')
    
    welcome_label.pack(pady = 10)
    appointment_button.pack(pady = 10)
    history_button.pack(pady = 10)
    prescription_button.pack(pady = 10)
    log_out_button.pack(pady = 10)
    
    main_screen.mainloop()

def register_appointment():
    global doctors_dropdown
    for child in main_screen.winfo_children():
        child.destroy()
        
    main_screen.title('Appointment Registration')
    main_screen.geometry()
    
    pbe.dropdownobj()
    
    specialists_label = tk.CTkLabel(main_screen, text = 'Specialists:')
    specialists_dropdown = tk.CTkComboBox(main_screen, values = pbe.specialist_options, variable = '', command = drop_down_config)
    
    doctors_label = tk.CTkLabel(main_screen, text = 'Doctors:')
    doctors_dropdown = tk.CTkComboBox(main_screen, values = pbe.doctor_options, variable = '')
    
    apply_button = tk.CTkButton(main_screen, text = 'Apply', command = appointment_registration)
    
    specialists_label.pack()
    specialists_dropdown.pack()
    doctors_label.pack()
    doctors_dropdown.pack()
    apply_button.pack(pady = 10)
    
def drop_down_config(choice):
    placeholder_choice = choice
    pbe.drop_down_update(placeholder_choice)
    doctors_dropdown.configure(values = pbe.config_doctor_options)
    
def appointment_registration():
    pbe.appointment_registration(doctors_dropdown.get())
           
patient_main_screen()