from tkinter import *
from tkinter import ttk

import login

root=Tk()
#添加标题
root.title('Student Achievement Enquiry System')

root.geometry('550x400')
login.LoginPage(root)
root.mainloop()