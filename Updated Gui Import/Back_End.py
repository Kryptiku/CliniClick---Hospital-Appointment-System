import customtkinter
import datetime
import mysql.connector

db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'cliniclick_db')
mycur = db.cursor()
   
def appointment_validation(time, date):
    global timeObject,formatted_time, new_time, dateObject, new_date, error_time, error_date
    error_time = False
    error_date = False
    
    new_time = str(time)
    formatted_time = new_time.upper()
    time_format = '%I:%M %p'
    
    new_date = str(date)
    date_format = '%Y-%m-%d'
    
    try:
        timeObject = datetime.datetime.strptime(formatted_time, time_format)
        print(formatted_time)
        
    except ValueError:
        error_time = True
        
    try:
        dateObject = datetime.datetime.strptime(new_date, date_format)
        print(new_date)
        
    except ValueError:   
        error_date = True
    
    if error_date == True and error_time == False:
        global failed_main
        failed_main = customtkinter.CTkToplevel()
        failed_main.attributes('-topmost', True)
        failed_main.title('Invalid Entry')
        failed_main.geometry()
        my_font = customtkinter.CTkFont(family = 'bold')
        
        error_label = customtkinter.CTkLabel(failed_main, text = 'Incorrect Date', font = my_font)
        ok_button = customtkinter.CTkButton(failed_main, text = 'Ok', bg_color = 'grey', command = fail_destroy)
        
        error_label.pack()
        ok_button.pack()
    
    if error_date == False and error_time == True:
        failed_main = customtkinter.CTkToplevel()
        failed_main.attributes('-topmost', True)
        failed_main.title('Invalid Entry')
        failed_main.geometry()
        my_font = customtkinter.CTkFont(family = 'bold')
        
        error_label = customtkinter.CTkLabel(failed_main, text = 'Incorrect Time', font = my_font)
        ok_button = customtkinter.CTkButton(failed_main, text = 'Ok', bg_color = 'grey', command = fail_destroy)
        
        error_label.pack()
        ok_button.pack()
    
    elif error_date == True and error_time == True:
        failed_main = customtkinter.CTkToplevel()
        failed_main.attributes('-topmost', True)
        failed_main.title('Invalid Entry')
        failed_main.geometry()
        my_font = customtkinter.CTkFont(family = 'bold')
        
        error_label = customtkinter.CTkLabel(failed_main, text = 'Incorrect Date and Time', font = my_font)
        ok_button = customtkinter.CTkButton(failed_main, text = 'Ok', bg_color = 'grey', command = fail_destroy)
        
        error_label.pack()
        ok_button.pack()
    
    else:
        print(error_time)
        print(error_date)
        
def fail_destroy():
    failed_main.destroy()