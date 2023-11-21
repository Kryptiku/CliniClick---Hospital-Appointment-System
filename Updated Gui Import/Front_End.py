import customtkinter
import Back_End as be

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')


def appointment():
    global time, date, doctor, main
    main = customtkinter.CTk()

    main.title('Appointment')
    main.geometry('525x300')
    
    my_font = customtkinter.CTkFont(family = 'bold')
    time = customtkinter.StringVar()
    doctor = customtkinter.StringVar()
    
    register_label = customtkinter.CTkLabel(main, text = 'Appointment Registration', font = my_font)
    patient_label = customtkinter.CTkLabel(main, text = 'Patient', font = my_font)
    
    register_label.pack()
    patient_label.pack()
    
    doctor_label = customtkinter.CTkLabel(main, text = 'Doctor Name: ', font = my_font)
    doctor_entry = customtkinter.CTkEntry(main, textvariable = doctor)
    
    label_time = customtkinter.CTkLabel(main, text='Time: ')
    entry_time = customtkinter.CTkEntry(main, textvariable = time)
    
    date = customtkinter.StringVar()
    label_date = customtkinter.CTkLabel(main, text='Date: ')
    entry_date = customtkinter.CTkEntry(main, textvariable = date)
    enter_button = customtkinter.CTkButton(main, text = 'Enter', command = appointment_validation)
    
    doctor_label.pack()
    doctor_entry.pack()
    label_time.pack()
    entry_time.pack()
    label_date.pack()
    entry_date.pack()
    enter_button.pack(pady = 20)
    main.mainloop()
    
def appointment_validation():
    be.appointment_validation(time.get(), date.get(), doctor.get())
           
appointment()