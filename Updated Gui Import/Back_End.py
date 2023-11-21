import customtkinter
import datetime
import mysql.connector
from Data_Holding import time

db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'cliniclick_db')
mycur = db.cursor()

# with open("Updated Gui Import/Front_End.py") as f:
#     exec(f.read())

def patient_code():
    x = 'y'
    
    
def time_validation():

    global timeObject,formatted_time, time

    # new_time = str(time.get())
    formatted_time = time.upper()
    time_format = '%I:%M %p'
    
    try:
        timeObject = datetime.datetime.strptime(formatted_time, time_format)
        print(formatted_time)

    except ValueError:
        
        print('Error')
        

     
# def validation_fail():
#     failed_main = tk.Toplevel(main)
#     failed_main.title('Invalid Entry')
#     failed_main.geometry()
    
#     error_label = tk.Label(failed_main, text = 'Incorrect Time', fg = 'red', font = 'bold', width = 20)
#     ok_button = tk.Button(failed_main, text = 'Ok', bg = 'grey', command = fail_destroy)
    
#     error_label.pack()
#     ok_button.pack()

