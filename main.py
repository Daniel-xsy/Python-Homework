import tkinter as tk
from tkinter import ttk
import login

if __name__=="__main__":
    root=tk.Tk()
    #添加标题
    root.title('Student Grade Enquiry System')
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    width=360
    height=300
    #将窗口放置于屏幕中间
    root.geometry('%dx%d+%d+%d'%(width, height,\
         (screenwidth-width)/2, (screenheight-height)/2))
    #进入登陆注册界面
    login.LoginPage(root)
    root.mainloop()
