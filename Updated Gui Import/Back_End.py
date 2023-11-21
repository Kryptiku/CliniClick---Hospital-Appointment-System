# from tkinter import *
import customtkinter

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')
root = customtkinter.CTk()

root.title('Tkinter Test')
root.geometry('600x350')

my_button = customtkinter.CTkButton(root, text = 'Enter')
my_button.pack()

root.mainloop()
