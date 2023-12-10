import mysql.connector
import datetime

db = mysql.connector.connect(host="localhost", user="root", passwd="", database="cliniclick_db")
mycur = db.cursor()


def stlogin_verify_test():
    global results, username_verify, password_verify
    stun_verify = username_verify.get()
    stpw_verify = password_verify.get()
    sql = "select * from stafftbl where binary staff_username = %s and staff_password = %s"
    mycur.execute(sql, [(stun_verify), (stpw_verify)])
    results = mycur.fetchall()

def getname():
    global loggedin_user, staff_lastname, staff_firstname
    mycur.execute("select staff_lastname from stafftbl where staff_username = " + "\'" + loggedin_user + "\'")
    lnresult = mycur.fetchall()

    for row in lnresult:
        staff_lastname = "".join(row)

    mycur.execute("select staff_firstname from stafftbl where staff_username = " + "\'" + loggedin_user + "\'")
    fnresult = mycur.fetchall()
    for row in fnresult:
        staff_firstname = "".join(row)

def getaptreq():
    global apt_req_data
    mycur.execute("SELECT a.apt_req_code, p.patient_lastname, p.patient_firstname, d.doctor_lastname, d.doctor_firstname FROM appointmentrequeststbl a INNER JOIN patienttbl p ON a.patient_code = p.patient_code INNER JOIN doctortbl d ON a.doctor_code = d.doctor_code")
    apt_req_data = mycur.fetchall()

def ardropdownobj():
    global ar_options, ar_size
    mycur.execute("SELECT apt_req_code FROM appointmentrequeststbl ORDER BY apt_req_code ASC")
    ar_size = mycur.fetchall()
    ar_options = [row[0] for row in ar_size]

def changear_entries():
    global choice, ptntln, ptntfn, dctrln, dctrfn
    query = (
    "SELECT "
    "p.patient_lastname, p.patient_firstname, "
    "d.doctor_lastname, d.doctor_firstname "
    "FROM appointmentrequeststbl a "
    "INNER JOIN patienttbl p ON a.patient_code = p.patient_code "
    "INNER JOIN doctortbl d ON a.doctor_code = d.doctor_code "
    f"WHERE apt_req_code = '{choice}'")

    mycur.execute(query)    # Execute the query

    goods = mycur.fetchall() # Fetch all rows from the result set

    if goods:
        ptntln, ptntfn, dctrln, dctrfn = goods[0]
        ptntln, ptntfn, dctrln, dctrfn = str(ptntln), str(ptntfn), str(dctrln), str(dctrfn)
    else:
        ptntln, ptntfn, dctrln, dctrfn = "", "", "", ""

def timeanddate_validation(time, date):
    global timeObject,formatted_time, new_time, dateObject, new_date, error_time, error_date
    error_time = False
    error_date = False
    
    new_time = str(time)
    formatted_time = new_time.upper()
    time_format = '%I:%M %p'
    
    new_date = str(date)
    date_format = '%Y-%m-%d'
    print(new_date)
    
    try:
        timeObject = datetime.datetime.strptime(formatted_time, time_format)
        print(formatted_time)
        
    except ValueError:
        error_time = True
        print("time error")
        print(formatted_time)
        
    try:
        dateObject = datetime.datetime.strptime(new_date, date_format)
        print(new_date)
        
    except ValueError:   
        error_date = True
        print("date error")
        print(new_date)

def acceptappointment():
    global ptntcode, dctrcode
    mycur.execute("SELECT patient_code FROM appointmentrequeststbl WHERE apt_req_code = " + "\'" + choice + "\'")
    result1 = mycur.fetchall()
    for row  in result1 :
        ptntcode = ''.join(row)
    mycur.execute("SELECT doctor_code FROM appointmentrequeststbl WHERE apt_req_code = " + "\'" + choice + "\'")
    result2 = mycur.fetchall()
    for row  in result2 :
        dctrcode = ''.join(row)
    sql = "INSERT INTO appointmentstbl VALUES ("  + "\'" + choice + "\', " + "\'" + ptntcode + "\', " + "\'" + dctrcode + "\', " + "\'" + new_date + "\', " + "\'" + new_time + "\')"
    mycur.execute(sql)
    
    mycur.execute("DELETE FROM appointmentrequeststbl WHERE apt_req_code = " + "\'" + choice + "\'")

    # db.commit()

def getacceptedapts():
    global acceptedapts
    mycur.execute("SELECT a.apt_req_code, p.patient_lastname, p.patient_firstname, d.doctor_lastname, d.doctor_firstname, a.apt_date, a.apt_time FROM appointmentstbl a INNER JOIN patienttbl p ON a.patient_code = p.patient_code INNER JOIN doctortbl d ON a.doctor_code = d.doctor_code")
    acceptedapts = mycur.fetchall()

def aadropdownobj():
    global aa_options, aa_size
    mycur.execute("SELECT apt_req_code FROM appointmentstbl ORDER BY apt_req_code ASC")
    aa_size = mycur.fetchall()
    aa_options = [row[0] for row in aa_size]

def changeaa_entries():
    global aachoice, aaptntln, aaptntfn, aadctrln, aadctrfn
    query = (
    "SELECT "
    "p.patient_lastname, p.patient_firstname, "
    "d.doctor_lastname, d.doctor_firstname "
    "FROM appointmentstbl a "
    "INNER JOIN patienttbl p ON a.patient_code = p.patient_code "
    "INNER JOIN doctortbl d ON a.doctor_code = d.doctor_code "
    f"WHERE apt_req_code = '{aachoice}'")

    mycur.execute(query)

    goods = mycur.fetchall()

    if goods:
        aaptntln, aaptntfn, aadctrln, aadctrfn = goods[0]
        aaptntln, aaptntfn, aadctrln, aadctrfn = str(aaptntln), str(aaptntfn), str(aadctrln), str(aadctrfn)
    else:
        aaptntln, aaptntfn, aadctrln, aadctrfn = "", "", "", ""

def update_appointment():
    mycur.execute("UPDATE appointmentstbl SET apt_date = " + "\'" + new_date + "\'" + ", apt_time = "  + "\'" + new_time + "\' WHERE apt_req_code = " + "\'" + aachoice + "\'")
    db.commit()

def delete_appointment():
    mycur.execute("DELETE FROM appointmentstbl WHERE apt_req_code = " + "\'" + aachoice + "\'")
    # db.commit()

def medsdropdownobj():
    global meds_options, meds_size
    mycur.execute("SELECT meds_name FROM medstbl ORDER BY meds_code ASC")
    meds_size = mycur.fetchall()
    meds_options = [row[0] for row in meds_size]

def enter_done(diagnosis, meds, dosage, frequency):
    mycur.execute("SELECT patient_code FROM appointmentstbl WHERE apt_req_code = " + "\'" + aachoice + "\'")
    result1 = mycur.fetchall()
    for row in result1 :
        dptntcode = ''.join(row)
    mycur.execute("SELECT doctor_code FROM appointmentstbl WHERE apt_req_code = " + "\'" + aachoice + "\'")
    result2 = mycur.fetchall()
    for row in result2 :
        ddctrcode = ''.join(row)
    
    mycur.execute("Select meds_code FROM medstbl WHERE meds_name = " + "\'" + meds + "\'")
    result3 = mycur.fetchall()
    for row in result3 :
        meds_code = ''.join(row)

    mycur.execute("SELECT apt_date FROM appointmentstbl WHERE apt_req_code = " + "\'" + aachoice + "\'")
    result4 = mycur.fetchall()
    for row in result4:
        aptdate = row[0].strftime("%Y-%m-%d")

    mycur.execute("INSERT INTO prescriptiontbl VALUES (" + "\'" + meds_code + "\', " + "\'" + dptntcode + "\', " + "\'" + dosage + "\', " + "\'" + frequency + "\')")
    
    # create new patient history code
    mycur.execute("SELECT patient_history_code FROM patienthistorytbl")
    mycur.fetchall()
    conv_rowcount = str(mycur.rowcount + 1)
    value = '00000000' 
    conv_rowcount = str(conv_rowcount)
    temp = len(conv_rowcount)
    modified_value = value[:-temp]

    sql = "INSERT INTO patienthistorytbl VALUES (%s, %s, %s, %s, %s, %s)"
    t = ('PH' + modified_value + conv_rowcount, dptntcode, ddctrcode, diagnosis, meds_code, aptdate)
    mycur.execute(sql, t)
    mycur.execute("SELECT * FROM patienthistorytbl")
    wow = mycur.fetchall()
    print(wow)