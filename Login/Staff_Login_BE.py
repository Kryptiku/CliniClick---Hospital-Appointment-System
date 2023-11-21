import mysql.connector
import os

os.system('cls')
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
    global loggedin_user, staff_lastname
    mycur.execute("select staff_lastname from stafftbl where staff_username = " + "\'" + loggedin_user + "\'")
    result = mycur.fetchall()

    for row in result:
        staff_lastname = "".join(row)