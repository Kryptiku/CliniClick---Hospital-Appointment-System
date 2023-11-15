# import mysql.connector


# connection = mysql.connector.connect(host="localhost", user="root", password = "", database = "cliniclick_db")

# if connection.is_connected():
#     print("Connected Successfully")
    
# else:
#         print("Failed to connect")

import mysql.connector
import os 
os.system('cls')

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="cliniclick_db")
mycur = db.cursor()
print("DB Loaded")

# db.commit
# mycur.close
# db.close

# mycur.execute("select patient_code from patienttbl")
# mycur.fetchall()
# value = "00000000" 
# conv_rowcount = str(mycur.rowcount)
# temp = len(conv_rowcount)
# modified_value = value[:-2]
# print('PA' + modified_value + conv_rowcount)

# mycur.execute("select patient_lastname from patienttbl where patient_username = \"User11\"")
# a = mycur.fetchall()

def select():
    mycur.execute("select patient_lastname from patienttbl where patient_username = \'User11\'")
    
    result = mycur.fetchall()
    return result

a = select()
db.close()
# a = "Sam"
# modified_value = a[:-1]
# print(modified_value)
for row  in a :
    b = "".join(row)

print(b)




