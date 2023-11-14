import mysql.connector


connection = mysql.connector.connect(host="localhost", user="root", password = "", database = "cliniclick_db")

if connection.is_connected():
    print("Connected Successfully")
    
else:
        print("Failed to connect")
