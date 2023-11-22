import tkinter as tk
from tkinter import ttk
import mysql.connector
import os

os.system('cls')
db = mysql.connector.connect(host='localhost', user='root', password='', database='cliniclick_db')
mycur = db.cursor()

# Create a ttk.Notebook
notebook = ttk.Notebook()

# Function to create a new frame for each screen
def create_frame(title):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=title)
    return frame

# Main Screen
main_frame = create_frame('Main Screen')
welcome_label = tk.Label(main_frame, text='Welcome to the Cliniclick Log-In Portal', font='calibri 24', bg='sky blue',
                         fg='black', width=500)
welcome_label.pack()
login_button = tk.Button(main_frame, text='Log-In', bg='sky blue', font='bold', command=lambda: show_frame(login_frame))
register_button = tk.Button(main_frame, text='Register', bg='sky blue', font='bold', command=lambda: show_frame(registration_frame))
footer_label = tk.Label(main_frame, text='Developed By Cliniclick™')
login_button.pack(pady=15)
register_button.pack()
footer_label.pack(side='bottom', pady=5)

# Login Screen
login_frame = create_frame('Log-In')
def login():
    global username_verify, password_verify, login_main
    username_verify = tk.StringVar()
    password_verify = tk.StringVar()
    login_main = tk.Toplevel()
    
    login_main.title('Log-in Portal')
    login_main.geometry('300x300')
    login_label = tk.Label(login_main, text = 'Log-In Portal', bg = 'sky blue', fg = 'black', font = 'bold', width = 300)
    login_label.pack()
    
    username_label = tk.Label(login_main, text = 'Username: ')
    username_entry = tk.Entry(login_main, textvariable = username_verify)
    
    password_label = tk.Label(login_main, text = 'Password: ')
    password_entry = tk.Entry(login_main, textvariable = password_verify, show = '*')
    
    login_button = tk.Button(login_main, text = 'Log-In', bg='sky blue')
    
    username_label.pack(pady = 10)
    username_entry.pack()
    password_label.pack(pady = 10)
    password_entry.pack()
    login_button.pack(pady = 10)

# Registration Screen
registration_frame = create_frame('Registration')
# ... (your registration code)

# Other screens can be added similarly

def show_frame(frame):
    notebook.select(frame)

notebook.pack(expand=True, fill='both')
notebook.select(main_frame)  # Show the main screen initially

# Start the main loop
tk.mainloop()
