import customtkinter
import datetime
import mysql.connector
from subprocess import call

db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'cliniclick_db')
mycur = db.cursor()
   
def appointment_validation(time, date, doctor):
    global timeObject,formatted_time, new_time, dateObject, new_date, error_time, error_date, error_doctor
    error_time = False
    error_date = False
    error_doctor = False
    
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
        
    sql = 'select doctor_code from doctortbl where doctor_lastname = ' + '\'' + doctor + '\''
    mycur.execute(sql)
    results = mycur.fetchall()  
    
    if results:
        error_doctor = False
    else:
        error_doctor = True
    
    print(error_doctor)
    if error_doctor == True or error_date == True or error_time == True:
        global failed_main
        failed_main = customtkinter.CTkToplevel()
        failed_main.attributes('-topmost', True)
        failed_main.title('Invalid Entry')
        failed_main.geometry('170x70')
        my_font = customtkinter.CTkFont(family = 'bold')
        
        error_label = customtkinter.CTkLabel(failed_main, text = 'Incorrect Input', font = my_font)
        ok_button = customtkinter.CTkButton(failed_main, text = 'Ok', command = fail_destroy)
        
        error_label.pack()
        ok_button.pack()
    
    else:
        success()
        mycur.execute('select apt_req_code from appointmentstbl')
        mycur.fetchall()
        conv_rowcount = str(mycur.rowcount + 1)
        value = '00000000' 
        conv_rowcount = str(conv_rowcount)
        temp = len(conv_rowcount)
        modified_value = value[:-temp]
        db.commit()
        sql = 'insert into appointmentstbl values (%s, %s,%s,%s,%s)'
        t = ('AR' + modified_value + conv_rowcount, 'PA00000001', 'DO00000001', new_date, formatted_time)
        mycur.execute(sql, t)
        db.commit()

def success():
    global success_popup
    success_popup = customtkinter.CTkToplevel()
    success_popup.attributes('-topmost', True)
    success_popup.title('Success Congrats Bitch')
    success_popup.geometry()
    my_font = customtkinter.CTkFont(family = 'bold')
    
    success_label = customtkinter.CTkLabel(success_popup, text = 'Congrats Fucker', font = my_font)
    ok_button = customtkinter.CTkButton(success_popup, text = 'Ok', command = success_destroy)
    
    success_label.pack()
    ok_button.pack()
        
def fail_destroy():
    failed_main.destroy()
    
def success_destroy():
    success_popup.destroy()