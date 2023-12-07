import customtkinter as tk
import datetime
import mysql.connector

db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'cliniclick_db')
mycur = db.cursor()

def palogin_verify_test(username_verify, password_verify):
    global results, results2, patient_lastname, paun_verify
    paun_verify = username_verify
    papw_verify = password_verify
    sql = 'select * from patienttbl where binary patient_username = %s and patient_password = %s'
    mycur.execute(sql,[(paun_verify),(papw_verify)])
    results = mycur.fetchall()
    
    mycur.execute('select patient_lastname from patienttbl where patient_username = ' + '\'' + paun_verify + '\'')
    results2 = mycur.fetchall()
    
    for row  in results2 :
        patient_lastname = ''.join(row)

def login_failed():
    global failed_main
    failed_main = tk.CTkToplevel()
    failed_main.attributes('-topmost', True)
    failed_main.title('Invalid')
    failed_main.geometry('200x100')
    
    error_label = tk.CTkLabel(failed_main, text = 'Invalid credentials')
    ok_button = tk.CTkButton(failed_main, text = 'Ok', command = fail_destroy)
    
    error_label.pack()
    ok_button.pack()
    
def fail_destroy():
    failed_main.destroy()
    
def register_user(lastname, firstname, middlename, birthdate, sex, contact, address, username, password):
    global lastname_info, firstname_info, middlename_info, birthdate_info, sex_info, contact_info, address_info, username_info, password_info, dateObject, new_date
    
    lastname_info = lastname
    firstname_info = firstname
    middlename_info = middlename
    birthdate_info = birthdate
    sex_info = sex
    contact_info = contact
    address_info = address
    username_info = username
    password_info = password
     
    new_date = str(birthdate_info)
    date_format = '%Y-%m-%d'
       
    try:
        dateObject = datetime.datetime.strptime(new_date, date_format)
        registration_validation()
        
    except ValueError:  
        login_failed()
    
def registration_validation():
    if lastname_info == '' or firstname_info == '' or middlename_info == '' or birthdate_info == '' or sex_info == '' or contact_info == '' or username_info == '' or password_info == '':
        login_failed()
        
    elif len(lastname_info) > 20 or len(firstname_info) > 20 or len(middlename_info) > 20 or len(address_info) > 50 or len(username_info) > 15 or len(password_info) > 15:
        login_failed()

    else:
        mycur.execute('select patient_code from patienttbl')
        mycur.fetchall()
        
        conv_rowcount = str(mycur.rowcount + 1)
        value = '00000000' 
        conv_rowcount = str(conv_rowcount)
        temp = len(conv_rowcount)
        modified_value = value[:-temp]
        db.commit()
        sql = 'insert into patienttbl values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        t = ('PA' + modified_value + conv_rowcount, lastname_info, firstname_info, middlename_info, birthdate_info, sex_info, contact_info, address_info, username_info, password_info)
        mycur.execute(sql, t)
        db.commit()
        print("Register Success")  
        registration_success()
    
def dropdownobj():
    global specialist_options, specialist_size, doctor_options, doctor_size, choice
    
    mycur.execute('select distinct doctor_specialty from doctortbl order by doctor_specialty')
    specialist_size = mycur.fetchall()
    
    specialist_options = [row[0] for row in specialist_size]
    
    mycur.execute('select doctor_lastname, doctor_firstname from doctortbl order by doctor_lastname asc')
    doctor_size = mycur.fetchall()
    
    doctor_options = []
   
    for row in doctor_size :
        last_name = row[0].strip()
        first_name = row[1].strip()
        full_name = last_name + ', ' + first_name
        
        doctor_options.append(full_name)

def drop_down_update(choice):
    global config_doctor_options
    config_doctor_options = []
        
    mycur.execute('select doctor_lastname, doctor_firstname from doctortbl where doctor_specialty = ' + '\'' + choice + '\'' +  ' order by doctor_lastname asc')
    doctor_size = mycur.fetchall()
    
    for row in doctor_size :
        last_name = row[0].strip()
        first_name = row[1].strip()
        full_name = last_name + ', ' + first_name
        
        config_doctor_options.append(full_name)
        
def appointment_registration(doctor_name):
    global fromatted_doctor_name
    delimiter = ','
    fromatted_doctor_name = doctor_name.split(delimiter)[0]
    
    if fromatted_doctor_name == '':
        login_failed()
    
    else:
        mycur.execute('select apt_req_code from appointmentrequeststbl')
        mycur.fetchall()
        
        conv_rowcount = str(mycur.rowcount + 1)
        value = '00000000' 
        conv_rowcount = str(conv_rowcount)
        temp = len(conv_rowcount)
        modified_value = value[:-temp]
        db.commit()
        
        mycur.execute('select patient_code from patienttbl where patient_username = ' + '\'' + paun_verify + '\'')
        patient_code = mycur.fetchall()
        
        for row  in patient_code:
            new_patient_code = ''.join(row)
            
        db.commit()
        
        mycur.execute('select doctor_code from doctortbl where doctor_lastname = ' + '\'' + fromatted_doctor_name + '\'')
        doctor_code = mycur.fetchall()
        
        for row  in doctor_code:
            new_doctor_code = ''.join(row)
        
        db.commit()
        
        sql = 'insert into appointmentrequeststbl values (%s, %s, %s)'
        t = ('AR' + modified_value + conv_rowcount, new_patient_code, new_doctor_code)
        mycur.execute(sql, t)
        db.commit()
        print("Register Success")
        appointment_registration_success()
        
def patient_history():
    global pa_his_data
    mycur.execute('select patient_code from patienttbl where patient_username = ' + '\'' + paun_verify + '\'')
    patient_code = mycur.fetchall()
    
    for row  in patient_code:
            new_patient_code = ''.join(row)
    
    mycur.execute('select d.doctor_lastname, d.doctor_firstname, h.diagnosis, h.diagnosis_date, m.meds_name, p.dosage, p.frequency from patienthistorytbl h inner join doctortbl d on h.doctor_code = d.doctor_code inner join medstbl m on h.meds_code = m.meds_code inner join prescriptiontbl p on h.meds_code = p.meds_code where h.patient_code = ' + '\'' + new_patient_code + '\'')        
    pa_his_data = mycur.fetchall()
    
def registration_success():
    global success_main
    success_main = tk.CTkToplevel()
    success_main.attributes('-topmost', True)
    success_main.title('Success')
    success_main.geometry('200x100')
    
    error_label = tk.CTkLabel(success_main, text = 'Registration Success')
    ok_button = tk.CTkButton(success_main, text = 'Ok', command = success_destroy)
    
    error_label.pack()
    ok_button.pack()
    
def success_destroy():
    global register_main
    success_main.destroy()
    register_main.destroy()
    
def appointment_registration_success():
    global success_main
    success_main = tk.CTkToplevel()
    success_main.attributes('-topmost', True)
    success_main.title('Success')
    success_main.geometry('200x100')
    
    error_label = tk.CTkLabel(success_main, text = 'Registration Success')
    ok_button = tk.CTkButton(success_main, text = 'Ok', command = registration_success_destroy)
    
    error_label.pack()
    ok_button.pack()\
        
def registration_success_destroy():
    success_main.destroy()

def pending_appointments():
    global acceptedapts
    mycur.execute('SELECT a.apt_req_code, p.patient_lastname, p.patient_firstname, d.doctor_lastname, d.doctor_firstname, a.apt_date, a.apt_time FROM appointmentstbl a INNER JOIN patienttbl p ON a.patient_code = p.patient_code INNER JOIN doctortbl d ON a.doctor_code = d.doctor_code where patient_username = ' + '\'' + paun_verify + '\'')
    acceptedapts = mycur.fetchall()