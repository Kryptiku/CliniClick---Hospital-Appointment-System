import customtkinter
import Back_End as be

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')


def appointment():
    global time, date, main
    main = customtkinter.CTk()

    main.title('Appointment')
    main.geometry('525x200')
    
    my_font = customtkinter.CTkFont(family = 'bold')
    time = customtkinter.StringVar()
    
    register_label = customtkinter.CTkLabel(main, text = 'Appointment Registration', font = my_font)
    register_label.pack()
    
    patient_label = customtkinter.CTkLabel(main, text = 'Patient', font = my_font)
    patient_label.pack()
      
    label_time = customtkinter.CTkLabel(main, text='Time: ')
    entry_time = customtkinter.CTkEntry(main, textvariable = time)
    
    label_time.pack()
    entry_time.pack()
    
    date = customtkinter.StringVar()
    label_date = customtkinter.CTkLabel(main, text='Date: ')
    entry_date = customtkinter.CTkEntry(main, textvariable = date)
    appointment_button = customtkinter.CTkButton(main, text = 'Enter', command = appointment_validation)
    
    label_date.pack()
    entry_date.pack()
    appointment_button.pack()
    main.mainloop()
    
def appointment_validation():
    be.appointment_validation(time.get(), date.get())
           
appointment()