import mysql.connector
import os

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
    mycur.execute("SELECT p.patient_lastname FROM appointmentrequeststbl a INNER JOIN patienttbl p ON a.patient_code = p.patient_code WHERE apt_req_code = "+ "\'" + choice + "\'")
