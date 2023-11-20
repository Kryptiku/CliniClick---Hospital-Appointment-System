import datetime
import os

os.system('cls')

time = input('input time: ').upper()


def validations():
    try:
        global timeObject
        time_format = '%I:%M %p'
        timeObject = datetime.datetime.strptime(time, time_format)
        print(time)
        
    except ValueError:
        print('Invalid DataType')

validations()