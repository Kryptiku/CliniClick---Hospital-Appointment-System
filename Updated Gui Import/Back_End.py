import datetime
import mysql.connector

db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'cliniclick_db')
mycur = db.cursor()
        
def time_validation(time):

    global timeObject,formatted_time, new_time
    new_time = str(time)
    formatted_time = new_time.upper()
    time_format = '%I:%M %p'
    
    try:
        timeObject = datetime.datetime.strptime(formatted_time, time_format)
        print(formatted_time)

    except ValueError:
        print(new_time)
        print('Error')
        

     













# def validation_fail():
#     failed_main = tk.Toplevel(main)
#     failed_main.title('Invalid Entry')
#     failed_main.geometry()
    
#     error_label = tk.Label(failed_main, text = 'Incorrect Time', fg = 'red', font = 'bold', width = 20)
#     ok_button = tk.Button(failed_main, text = 'Ok', bg = 'grey', command = fail_destroy)
    
#     error_label.pack()
#     ok_button.pack()