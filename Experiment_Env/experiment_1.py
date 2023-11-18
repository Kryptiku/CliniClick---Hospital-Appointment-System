# from tkinter import *
# from tkcalendar import *
# root=Tk()
# root.geometry("500x500")
# def mainF():
#     global cal
#     def getDate():
#         date=cal.get_date()
#         print(date)
#     cal.pack(pady=20, padx=20)
#     butt=Button(root,text="Date Getter", bg="cyan",command=getDate).pack()
# cal=Calendar(root,selectmode="day",date_pattern="y-mm-dd")
# but=Button(root,text="Pick Date",command=mainF).pack()
# root.mainloop()

from tkinter import *

def set_text(text):
    e.delete(0,END)
    e.insert(0,text)
    return

win = Tk()

e = Entry(win,width=10)
e.pack()

b1 = Button(win,text="animal",command=lambda:set_text("animal"))
b1.pack()

b2 = Button(win,text="plant",command=lambda:set_text("plant"))
b2.pack()

win.mainloop()