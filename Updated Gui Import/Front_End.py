import customtkinter
import Back_End as be

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')
main = customtkinter.CTk()

def appointment():
        
    main.title('Appointment')
    main.geometry('525x200')
    my_font = customtkinter.CTkFont(family = 'bold')
    global time
    time = customtkinter.StringVar()
    
    register_label = customtkinter.CTkLabel(main, text = 'Appointment Registration', font = my_font)
    register_label.pack()
    
    patient_label = customtkinter.CTkLabel(main, text = 'Patient', font = my_font)
    patient_label.pack()
      
    label_time = customtkinter.CTkLabel(main, text='Time: ')
    entry_time = customtkinter.CTkEntry(main, textvariable = time)
    
    appointment_button = customtkinter.CTkButton(main, text = 'Enter', command = lambda:be.time_validation(time.get()))
   
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