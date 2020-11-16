from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkm

class LoginPage(object):
    def __init__(self,master=None):
        self.root=master
        self.id=StringVar()
        self.password=StringVar()
        self.createPage()
    def createPage(self):
        #文字
        self.login_frame=ttk.Frame(self.root,padding=(10,10,10,10),relief='sunken',width=400,height=550)
        self.login_frame.grid()

        title=ttk.Label(self.login_frame,text='学生成绩查询系统',font=('华文行楷',20))
        id_label=ttk.Label(self.login_frame,text='用户名')
        pass_lable=ttk.Label(self.login_frame,text='密码')

        image_file=PhotoImage(file='hust.gif')
        hust_lable=ttk.Label(self.login_frame,image=image_file)

        user_entry=ttk.Entry(self.login_frame,textvariable=self.id,show=None,font=('Arial',14))
        pass_entry=ttk.Entry(self.login_frame,textvariable=self.password,show='*',font=('Arial',14))

        button1=ttk.Button(self.login_frame,text='注册',command=None)
        button2=ttk.Button(self.login_frame,text='登陆',command=None)
        button3=ttk.Button(self.login_frame,text='退出',command=None)

        title.grid(row=1,column=3,rowspan=2,columnspan=3)
        hust_lable.grid(row=4,column=3,rowspan=2,columnspan=3,sticky=N)
        id_label.grid(row=8,column=3,rowspan=2)
        pass_lable.grid(row=10,column=3,rowspan=2)
        user_entry.grid(row=8,column=4,rowspan=2,columnspan=2,pady=5)
        pass_entry.grid(row=10,column=4,rowspan=2,columnspan=2,pady=5)
        button1.grid(row=12,column=3,rowspan=2,pady=3)
        button2.grid(row=12,column=4,rowspan=2,pady=3)
        button3.grid(row=12,column=5,rowspan=2,pady=3)
        self.login_frame.columnconfigure(0,weight=1)
        self.login_frame.rowconfigure(0,weight=1)
        self.login_frame.mainloop()
    def loginCheck(self):
        pass
    def register(self):
        pass
        
    
        


