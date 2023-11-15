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

mycur.execute("select patient_code from patienttbl")
mycur.fetchall()
value = "00000000" 
conv_rowcount = str(mycur.rowcount)
temp = len(conv_rowcount)
modified_value = value[:-temp]
print('PA' + modified_value + conv_rowcount)