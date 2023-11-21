import customtkinter

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')
main = customtkinter.CTk()

# root.title('Tkinter Test')
# root.geometry('600x350')

# my_button = customtkinter.CTkButton(root, text = 'Enter')
# my_button.pack()

# root.mainloop()

def appointment():
    patient_code = customtkinter.StringVar()
    time_validation = customtkinter.StringVar()
    # for child in main.winfo_children():
    #     child.destroy()
    
    # user = str(username_verify.get())
    # mycur.execute('select patient_code from patienttbl where patient_username = ' + '\'' + user + '\'')
    # result = mycur.fetchall()
    
    # for row  in result :
    #     patient_code = ''.join(row)
        
    main.title('Appointment')
    main.geometry()
    my_font = customtkinter.CTkFont(family = 'bold')
    
    register_label = customtkinter.CTkLabel(main, text = 'Appointment Registration', bg_color = 'sky blue', fg_color = 'black', font = my_font, width = 50)
    register_label.pack()
    
    patient_label = customtkinter.CTkLabel(main, text = patient_code, bg_color = 'sky blue', fg_color = 'black', font = customtkinter.CTkFont(family = 'bold'), width = 50)
    patient_label.pack()
    
    appointment_button = customtkinter.CTkButton(main, text = 'Enter', bg_color = 'sky blue', fg_color = 'black', command = time_validation)
    appointment_button.pack()
    
    global time, date
    time = customtkinter.StringVar()
    
    label_time = customtkinter.CTkLabel(main, text='Time: ')
    entry_time = customtkinter.CTkEntry(main, textvariable = time)
    
    label_time.pack()
    entry_time.pack()
    
    
    date = customtkinter.StringVar()
    label_date = customtkinter.CTkLabel(main, text='Date: ')
    entry_date = customtkinter.CTkEntry(main, textvariable = date)
    
    label_date.pack()
    entry_date.pack()
    
    main.mainloop()
    
appointment()
    
