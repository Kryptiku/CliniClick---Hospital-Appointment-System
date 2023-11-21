import customtkinter
import Back_End as be
# from Back_End import time_validation

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')
main = customtkinter.CTk()

def appointment():
    patient_code = customtkinter.StringVar()
    # for child in main.winfo_children():
    #     child.destroy()
    
    # user = str(username_verify.get())
    # mycur.execute('select patient_code from patienttbl where patient_username = ' + '\'' + user + '\'')
    # result = mycur.fetchall()
    
    # for row  in result :
    #     patient_code = ''.join(row)
        
    main.title('Appointment')
    main.geometry('525x200')
    my_font = customtkinter.CTkFont(family = 'bold')
    
    time = customtkinter.StringVar()
    
    register_label = customtkinter.CTkLabel(main, text = 'Appointment Registration', font = my_font)
    register_label.pack()
    
    patient_label = customtkinter.CTkLabel(main, text = 'Patient', font = my_font)
    patient_label.pack()
    
    appointment_button = customtkinter.CTkButton(main, text = 'Enter', command = be.time_validation)
    # print_button = customtkinter.CTkButton(main, text = 'Test', command = print(time))
    
    label_time = customtkinter.CTkLabel(main, text='Time: ')
    entry_time = customtkinter.CTkEntry(main, textvariable = time)
    
    be.time = str(time.get())
    
    label_time.pack()
    entry_time.pack()
    appointment_button.pack()
    
    date = customtkinter.StringVar()
    label_date = customtkinter.CTkLabel(main, text='Date: ')
    entry_date = customtkinter.CTkEntry(main, textvariable = date)
    
    label_date.pack()
    entry_date.pack()
    
    main.mainloop()
    
appointment()
    
