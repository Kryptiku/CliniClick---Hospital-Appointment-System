import datetime
import os

os.system('cls')

time = input('input time: ').upper()
# time_formatted = time.upper
time_format = '%I:%M %p'

try:
    timeObject = datetime.datetime.strptime(time, time_format)
    print(time)
    
except ValueError:
    print('Invalid DataType')
