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

def dropdownobj():
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

def acceptapt_validation(time, date):
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
    print(ptntcode)

    mycur.execute("SELECT doctor_code FROM appointmentrequeststbl WHERE apt_req_code = " + "\'" + choice + "\'")
    result2 = mycur.fetchall()
    for row  in result2 :
        dctrcode = ''.join(row)
    print(dctrcode)
    print(choice)
    date = str(new_date)
    # val = (choice, ptntcode, dctrcode, new_date, new_time)
    sql = "INSERT INTO appointmentstbl VALUES ("  + "\'" + choice + "\', " + "\'" + ptntcode + "\', " + "\'" + dctrcode + "\', " + "\'" + new_date + "\', " + "\'" + new_time + "\')"
    mycur.execute(sql)
    
    mycur.execute("SELECT * FROM appointmentstbl")
    success = mycur.fetchall()
    print(success)

    db.commit()