import customtkinter as tk
from tkinter import ttk
import Patient_Login_BE as pbe
from PIL import ImageTk,Image

tk.set_appearance_mode('System')
tk.set_default_color_theme('blue')

def base_screen():
    global main_screen 
    main_screen = tk.CTk()
    main_screen.title('Cliniclick')
    
    patient_main_screen()

def patient_main_screen():
    for child in main_screen.winfo_children():
        child.destroy()
    
    main_screen.geometry('1280x720')
    img1 = ImageTk.PhotoImage(Image.open("assets/pattern.jpg"))
    l1 = tk.CTkLabel(main_screen, image=img1)
    l1.pack()

    frame = tk.CTkFrame(master=l1, width=320, height=360)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    l2 = tk.CTkLabel(master=frame, text="Hello!", font=('Century Gothic', 30))
    l2.place(x=122, y=150)

    l3 = tk.CTkLabel(master=frame, text="Welcome to the\n Cliniclick Log-In Portal", font=('Century Gothic', 10))
    l3.place(x=110, y=190)

    logo_image = Image.open("assets/logo.png")
    logo_image = logo_image.convert("RGBA")

    logo_image = logo_image.resize((350, 145))

    logo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.CTkLabel(master=frame, image=logo, text="")
    logo_label.image = logo
    logo_label.place(x=23, y=23)

    login_button = tk.CTkButton(master=frame, text='Log-In', command=patient_login)
    login_button.place(x=95, y=300)
    register_button = tk.CTkButton(master=frame, text='Register', command=patient_registration)
    register_button.place(x=95, y=265)
    
    # Create a transparent label by using a Label  widget and setting its background to be transparent
    # main_screen.wm_attributes('-transparentcolor', '#ab23ff')
    # footer_label = tk.CTkLabel(master=main_screen, text='Developed By Cliniclick™', font=('Century Gothic', 8), fg_color="#ab23ff")
    # footer_label.place(x=115, y=325)

    main_screen.mainloop()

def patient_login():
    for child in main_screen.winfo_children():
        child.destroy()
    
    global username, password
    username = tk.StringVar()
    password = tk.StringVar()
    
    img1 = ImageTk.PhotoImage(Image.open("assets/pattern.jpg"))
    l1 = tk.CTkLabel(main_screen, image=img1, text="")
    l1.pack()

    main_screen.title('Log-In Portal')
    main_screen.geometry('1280x720')

    frame = tk.CTkFrame(master=l1, width=320, height=360)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    l2 = tk.CTkLabel(master=frame, text="Log-In Interface", font=('Century Gothic', 30))
    l2.place(x=45, y=50)

    l3 = tk.CTkLabel(master=frame, text="Log-in the required credentials below:", font=('Century Gothic', 10))
    l3.place(x=72, y=90)

    username_label = tk.CTkLabel(master=frame,text = 'Username: ',font=('Century Gothic', 10))
    username_label.place(x=95, y=130)
    username_entry = tk.CTkEntry(master=frame, textvariable = username)
    username_entry.place(x=95, y=155)
    
    password_label = tk.CTkLabel(master=frame, text = 'Password: ',font=('Century Gothic', 10))
    password_label.place(x=95, y=190)
    password_entry = tk.CTkEntry(master=frame, textvariable = password, show = '*')
    password_entry.place(x=95, y=215)

    login_button = tk.CTkButton(master=frame, text = 'Log-In',command = patient_login_verify)
    login_button.place(x=95, y=265)
    back_button = tk.CTkButton(master=frame, text = 'Back', command = patient_main_screen)
    back_button.place(x=95, y=300)

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
    registration_main.attributes('-topmost', True)
    registration_main.title('Registration Portal')
    window_width = 500
    window_height = 720
    
    screen_width = registration_main.winfo_screenwidth()
    screen_height = registration_main.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    registration_main.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    img = Image.open("assets/pattern2.jpg")
    background_image = ImageTk.PhotoImage(img)

    background_label = tk.CTkLabel(registration_main, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0)

    lastname = tk.StringVar()
    firstname = tk.StringVar()
    middlename = tk.StringVar()
    birthdate = tk.StringVar()
    sex = tk.StringVar()
    contact = tk.StringVar()
    address = tk.StringVar()
    username = tk.StringVar()
    password = tk.StringVar()   
    
    title_label = tk.CTkLabel(registration_main, text = 'Register your account', width = 25, font=('Century Gothic', 35), corner_radius=15)
    title_label.grid(row = 0, columnspan = 2, pady = 10, padx = 30, sticky = 'ewns')

    label_lastname = tk.CTkLabel(registration_main, text = 'Last Name:', font=('Century Gothic',20))
    entry_lastname = tk.CTkEntry(registration_main, textvariable = lastname)
    label_lastname.grid(row = 1, column = 0, sticky = 'ewns', pady = 5, padx = 30)
    entry_lastname.grid(row = 1, column = 1, pady  =5, padx = 5)

    label_firstname = tk.CTkLabel(registration_main, text = 'First Name:',font=('Century Gothic',20))
    entry_firstname = tk.CTkEntry(registration_main, textvariable = firstname)
    label_firstname.grid(row = 2, column = 0, sticky = 'ewns', pady = 5, padx = 30)
    entry_firstname.grid(row = 2, column = 1, pady = 5, padx = 5)
    
    label_middlename = tk.CTkLabel(registration_main, text = 'Middle Name: ',font=('Century Gothic',20))
    entry_middlename = tk.CTkEntry(registration_main, textvariable = middlename)
    label_middlename.grid(row = 3, column = 0, sticky = 'ewns', pady = 5, padx = 30)
    entry_middlename.grid(row = 3, column = 1, pady = 5, padx = 5)

    label_birthdate = tk.CTkLabel(registration_main, text = 'Birth Date:',font=('Century Gothic',20))
    entry_birthdate = tk.CTkEntry(registration_main, textvariable = birthdate)
    label_birthdate.grid(row = 4, column = 0, sticky = 'ewns', pady = 5, padx = 30)
    entry_birthdate.grid(row = 4, column = 1, pady = 5, padx = 5)

    label_sex = tk.CTkLabel(registration_main, text = 'Sex:',font=('Century Gothic',20))
    entry_sex = tk.CTkEntry(registration_main, textvariable = sex)
    label_sex.grid(row = 5, column = 0, sticky = 'ewns', pady = 5, padx = 30)
    entry_sex.grid(row = 5, column = 1, pady = 5, padx = 5)

    label_contact = tk.CTkLabel(registration_main, text = 'Contact Number:',font=('Century Gothic',20))
    entry_contact = tk.CTkEntry(registration_main, textvariable = contact)
    label_contact.grid(row = 6, column = 0, sticky = 'ewns', pady = 5, padx = 30)
    entry_contact.grid(row = 6, column = 1, pady = 5, padx = 5)

    label_address = tk.CTkLabel(registration_main, text='Address:',font=('Century Gothic',20))
    entry_address = tk.CTkEntry(registration_main, textvariable = address)
    label_address.grid(row = 7, column = 0, sticky = 'ewns', pady = 5, padx = 30)
    entry_address.grid(row = 7, column = 1, pady = 5, padx = 5)

    label_username = tk.CTkLabel(registration_main, text = 'Username:',font=('Century Gothic',20))
    entry_username = tk.CTkEntry(registration_main, textvariable = username)
    label_username.grid(row = 8, column = 0, sticky ='ewns', pady = 5, padx = 30)
    entry_username.grid(row = 8, column = 1, pady = 5, padx = 5)

    label_password = tk.CTkLabel(registration_main, text = 'Password:',font=('Century Gothic',20))
    entry_password = tk.CTkEntry(registration_main, textvariable = password, show = '*')
    label_password.grid(row = 9, column = 0, sticky = 'ewns', pady = 5, padx = 30)
    entry_password.grid(row = 9, column = 1, pady = 5, padx = 5)
 
    register_button = tk.CTkButton(registration_main, text = 'Register', command = register_verify, font=('Century Gothic',20),fg_color='#458B74')
    register_button.grid(row = 10, column = 0, sticky = 's', pady = 10, padx = 10)
    
    back_button = tk.CTkButton(registration_main, text = 'Back', command = register_destroy, font=('Century Gothic',20),fg_color='#458B74')
    back_button.grid(row = 10, column = 1, sticky = 's', pady = 10, padx = 10)

    for i in range(12):
        registration_main.grid_rowconfigure(i, weight=1)
    for i in range(2):
        registration_main.grid_columnconfigure(i, weight=1)

def register_verify():
    pbe.register_main = registration_main
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
    window_width = 1280
    window_height = 720
    main_screen.geometry(f"{window_width}x{window_height}")

    img = Image.open("assets/pattern.jpg")
    background_image = ImageTk.PhotoImage(img)

    # Set window background image
    background_label = tk.CTkLabel(main_screen, image=background_image, text="")
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    canvas_width = window_width // 3  # Half of the window width
    canvas_height = window_height

    # Create a frame for the buttons on the left side
    frame = tk.CTkFrame(main_screen, width=canvas_width, height=canvas_height, fg_color="#F0F8FF")
    frame.place(x=0, y=0)

    welcome_label = tk.CTkLabel(frame, text='Welcome {}'.format(pbe.patient_lastname + '!'), font=('Century Gothic',40))
    welcome_label.place(relx=0.1, rely=0.1)

    # Buttons on the left side
    appointment_button = tk.CTkButton(frame, text='Register Appointment', command=register_appointment, font=('Century Gothic',18), fg_color='#458B74')
    appointment_button.place(relx=0.1, rely=0.3)

    history_button = tk.CTkButton(frame, text='View History and Prescriptions', command=alt_main, font=('Century Gothic',18), fg_color='#458B74')
    history_button.place(relx=0.1, rely=0.5)

    pending_appointments_button = tk.CTkButton(frame, text='Pending Appoinments', command=pending_appointments, font=('Century Gothic',18), fg_color='#458B74')
    pending_appointments_button.place(relx=0.1, rely=0.7)

    log_out_button = tk.CTkButton(frame, text='Log-Out', command=patient_main_screen, font=('Century Gothic',18), fg_color='#458B74')
    log_out_button.place(relx=0.1, rely=0.9)

    logo_image = Image.open("assets/logo.png")
    logo_image = logo_image.convert("RGBA")

    logo_image = logo_image.resize((850, 350))

    logo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.CTkLabel(master=main_screen, image=logo, text="")
    logo_label.image = logo
    logo_label.place(x=510, y=245)

    main_screen.mainloop()

def register_appointment():
    global doctors_dropdown
    for child in main_screen.winfo_children():
        child.destroy()

    main_screen.title('Welcome')
    window_width = 1280
    window_height = 720
    main_screen.geometry(f"{window_width}x{window_height}")

    img = Image.open("assets/pattern.jpg")
    background_image = ImageTk.PhotoImage(img)

    # Set window background image
    background_label = tk.CTkLabel(main_screen, image=background_image, text="")
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    canvas_width = window_width // 3  # One-third of the window width
    canvas_height = window_height

    # Create a frame for the buttons on the left side
    frame = tk.CTkFrame(main_screen, width=canvas_width, height=canvas_height, fg_color="#F0F8FF")
    frame.place(x=0, y=0)

    welcome_label = tk.CTkLabel(frame, text='Welcome {}'.format(pbe.patient_lastname + '!'), font=('Century Gothic',40), pady=10)
    welcome_label.place(relx=0.1, rely=0.1)

    # Buttons on the left side
    appointment_button = tk.CTkButton(frame, text='Register Appointment', command=register_appointment, font=('Century Gothic',18), fg_color='#458B74')
    appointment_button.place(relx=0.1, rely=0.3)

    history_button = tk.CTkButton(frame, text='View History and Prescriptions', command=alt_main, font=('Century Gothic',18), fg_color='#458B74')
    history_button.place(relx=0.1, rely=0.5)

    pending_appointments_button = tk.CTkButton(frame, text='Pending Appoinments', command=pending_appointments, font=('Century Gothic',18), fg_color='#458B74')
    pending_appointments_button.place(relx=0.1, rely=0.7)

    log_out_button = tk.CTkButton(frame, text='Log-Out', command=patient_main_screen, font=('Century Gothic',18), fg_color='#458B74')
    log_out_button.place(relx=0.1, rely=0.9)
    
    pbe.dropdownobj()
    
    # Create a frame for the appointment system on the right side
    frame2 = tk.CTkFrame(main_screen, width=canvas_width * 2, height=canvas_height, fg_color="#F0F8FF")
    frame2.place(x=590, rely=0.35)

    specialists_label = tk.CTkLabel(frame2, text='Specialists:', font=('Century Gothic',25))
    specialists_dropdown = tk.CTkComboBox(frame2, values=pbe.specialist_options, variable='', command=drop_down_config, font=('Century Gothic',25))

    doctors_label = tk.CTkLabel(frame2, text='Doctors:', font=('Century Gothic',25), width=500)
    doctors_dropdown = tk.CTkComboBox(frame2, values=pbe.doctor_options, variable='', font=('Century Gothic',25))

    apply_button = tk.CTkButton(frame2, text='Apply', command=appointment_registration, font=('Century Gothic',25), fg_color='#458B74')
    back_button = tk.CTkButton(frame2, text='Back', command=login_main, font=('Century Gothic',25), fg_color='#458B74')

    specialists_label.pack()
    specialists_dropdown.pack()
    doctors_label.pack()
    doctors_dropdown.pack()
    apply_button.pack(pady=10)
    back_button.pack()

    main_screen.mainloop()
    
def drop_down_config(choice):
    placeholder_choice = choice
    pbe.drop_down_update(placeholder_choice)
    doctors_dropdown.configure(values = pbe.config_doctor_options)
    
def appointment_registration():
    pbe.appointment_registration(doctors_dropdown.get())

def register_destroy():
    registration_main.destroy()\
        
def alt_main():
    for child in main_screen.winfo_children():
        child.destroy()
        
    main_screen.title('Welcome')
    window_width = 1280
    window_height = 720
    main_screen.geometry(f"{window_width}x{window_height}")

    img = Image.open("assets/pattern.jpg")
    background_image = ImageTk.PhotoImage(img)

    # Set window background image
    background_label = tk.CTkLabel(main_screen, image=background_image, text="")
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    canvas_width = window_width // 3  # One-third of the window width
    canvas_height = window_height

    # Create a frame for the buttons on the left side
    frame = tk.CTkFrame(main_screen, width=canvas_width, height=canvas_height, fg_color="#F0F8FF")
    frame.place(x=0, y=0)

    welcome_label = tk.CTkLabel(frame, text='Welcome {}'.format(pbe.patient_lastname + '!'), font=('Century Gothic',40))
    welcome_label.place(relx=0.1, rely=0.1)

    # Buttons on the left side
    appointment_button = tk.CTkButton(frame, text='Register Appointment', command=register_appointment, font=('Century Gothic',18), fg_color='#458B74')
    appointment_button.place(relx=0.1, rely=0.3)

    history_button = tk.CTkButton(frame, text='View History and Prescriptions', command=alt_main, font=('Century Gothic',18), fg_color='#458B74')
    history_button.place(relx=0.1, rely=0.5)

    pending_appointments_button = tk.CTkButton(frame, text='Pending Appoinments', command= pending_appointments, font=('Century Gothic',18), fg_color='#458B74')
    pending_appointments_button.place(relx=0.1, rely=0.7)

    log_out_button = tk.CTkButton(frame, text='Log-Out', command=patient_main_screen, font=('Century Gothic',18), fg_color='#458B74')
    log_out_button.place(relx=0.1, rely=0.9)

    pbe.patient_history()
    
    # Create a frame for the database table on the right side
    frame2 = tk.CTkFrame(main_screen, width=canvas_width * 2, height=canvas_height, fg_color="#F0F8FF")
    frame2.place(x=500, y=250)

    # Create a Treeview to display the database table
    tree = ttk.Treeview(frame2, show='headings')
    tree['columns'] = ('dctrln', 'dctrfn', 'diag', 'date', 'med', 'dsg', 'freq')
    # ... (rest of your Treeview code remains the same)

    bg_color = main_screen._apply_appearance_mode(tk.ThemeManager.theme['CTkFrame']['fg_color'])
    text_color = main_screen._apply_appearance_mode(tk.ThemeManager.theme['CTkLabel']['text_color'])

    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview', background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)

    tree.heading('dctrln', text='Doctor Last Name')
    tree.heading('dctrfn', text='Doctor First Name')
    tree.heading('diag', text='Diagnosis')
    tree.heading('date', text = 'Date')
    tree.heading('med', text='Medication')
    tree.heading('dsg', text='Dosage')
    tree.heading('freq', text='Frequency')

    for column in tree['columns']:
        tree.column(column, anchor='s', width=125)

    for row in pbe.pa_his_data:
        tree.insert('', 'end', values=row)

    tree.pack()

    back_button = tk.CTkButton(frame2, text='Back', command=login_main, font=('Century Gothic',18), fg_color='#458B74')
    back_button.pack(pady=10)

    main_screen.mainloop()

def pending_appointments():
    for child in main_screen.winfo_children():
        child.destroy()

    main_screen.title('Welcome')
    window_width = 1280
    window_height = 720
    main_screen.geometry(f"{window_width}x{window_height}")

    img = Image.open("assets/pattern.jpg")
    background_image = ImageTk.PhotoImage(img)

    # Set window background image
    background_label = tk.CTkLabel(main_screen, image=background_image, text="")
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    canvas_width = window_width // 3  # Half of the window width
    canvas_height = window_height

    # Create a frame for the buttons on the left side
    frame = tk.CTkFrame(main_screen, width=canvas_width, height=canvas_height, fg_color="#F0F8FF")
    frame.place(x=0, y=0)

    welcome_label = tk.CTkLabel(frame, text='Welcome {}'.format(pbe.patient_lastname + '!'), font=('Century Gothic',40))
    welcome_label.place(relx=0.1, rely=0.1)

    # Buttons on the left side
    appointment_button = tk.CTkButton(frame, text='Register Appointment', command=register_appointment, font=('Century Gothic',18), fg_color='#458B74')
    appointment_button.place(relx=0.1, rely=0.3)

    history_button = tk.CTkButton(frame, text='View History and Prescriptions', command=alt_main, font=('Century Gothic',18), fg_color='#458B74')
    history_button.place(relx=0.1, rely=0.5)

    pending_appointments_button = tk.CTkButton(frame, text='Pending Appoinments', command=pending_appointments, font=('Century Gothic',18), fg_color='#458B74')
    pending_appointments_button.place(relx=0.1, rely=0.7)

    log_out_button = tk.CTkButton(frame, text='Log-Out', command=patient_main_screen, font=('Century Gothic',18), fg_color='#458B74')
    log_out_button.place(relx=0.1, rely=0.9)

    pbe.pending_appointments()

    frame2 = tk.CTkFrame(main_screen, width=canvas_width * 2, height=canvas_height, fg_color="#F0F8FF")
    frame2.place(x=500, y=250)

    global acctree
    tree_frame = tk.CTkFrame(frame2)
    tree_frame.pack()
    acctree = ttk.Treeview(tree_frame, show="headings")
    acctree["columns"] = ("req_id", "ptntln", "ptntfn", "dctrln", "dctrfn", "aptdate", "apttime")
    
    bg_color = main_screen._apply_appearance_mode(tk.ThemeManager.theme["CTkFrame"]["fg_color"])
    text_color = main_screen._apply_appearance_mode(tk.ThemeManager.theme["CTkLabel"]["text_color"])

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
    
    back_button = tk.CTkButton(frame2, text='Back', command=login_main, font=('Century Gothic',18), fg_color='#458B74')
    back_button.pack()

def acceptedapt_current_treeview():
    pbe.pending_appointments()
    acctree.delete(*acctree.get_children())
    for row in pbe.acceptedapts:
        acctree.insert("", "end", values=row)

base_screen()