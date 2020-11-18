from tkinter import *
from tkinter import ttk
import login

if __name__=="__main__":  
    root=Tk()
    #添加标题
    root.title('Student Grade Enquiry System')
    root.geometry('550x400')
    login.LoginPage(root)
    root.mainloop()