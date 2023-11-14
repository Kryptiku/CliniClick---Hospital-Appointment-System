import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password = "", database = "antony_company")

if connection.is_connected():
    print("Connected Successfully")
    
else:
        print("Failed to connect")