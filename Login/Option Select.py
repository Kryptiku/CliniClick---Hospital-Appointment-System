#Option Select
import tkinter as tk
# from tkinter import *
# from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import os
import time

window = tk.Tk()
window.title('Test')
window.geometry('300x150')
title_label = ttk.Label(master = window, text = 'Miles to KM', font = 'calibri 24 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = 'Convert')
entry.pack(side = 'left', padx = 10)
button.pack()
input_frame.pack(pady = 10)

output_label = ttk.Label(master = window, text = 'Output')
output_label.pack(side = 'left')


window.mainloop()