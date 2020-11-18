from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkm
import time
import csv

class LoginPage(object):
    def __init__(self,master=None):
        self.root=master
        self.id=StringVar()
        self.password=StringVar()
        self.createPage()
    def createPage(self):
        #文字
        login_frame=ttk.Frame(self.root,padding=(10,10,10,10),relief='sunken',width=400,height=550)
        login_frame.grid()
        #frame1=ttk.Frame(login_frame)

        title=ttk.Label(login_frame,text='学生成绩查询系统',font=('华文行楷',20))
        id_label=ttk.Label(login_frame,text='学号')
        pass_lable=ttk.Label(login_frame,text='密码')

        image_file=PhotoImage(file='hust.gif')
        hust_lable=ttk.Label(login_frame,image=image_file)

        user_entry=ttk.Entry(login_frame,textvariable=self.id,show=None,font=('Arial',14))
        pass_entry=ttk.Entry(login_frame,textvariable=self.password,show='*',font=('Arial',14))

        button1=ttk.Button(login_frame,text='注册',command=self.register)
        button2=ttk.Button(login_frame,text='登陆',command=None)
        button3=ttk.Button(login_frame,text='退出',command=None)

        title.grid(row=1,column=3,rowspan=2,columnspan=3)
        hust_lable.grid(row=4,column=3,rowspan=2,columnspan=3,sticky=N)
        id_label.grid(row=8,column=3,rowspan=2)
        pass_lable.grid(row=10,column=3,rowspan=2)
        user_entry.grid(row=8,column=4,rowspan=2,columnspan=2,pady=5)
        pass_entry.grid(row=10,column=4,rowspan=2,columnspan=2,pady=5)
        button1.grid(row=12,column=3,rowspan=2,pady=3)
        button2.grid(row=12,column=4,rowspan=2,pady=3)
        button3.grid(row=12,column=5,rowspan=2,pady=3)
        login_frame.columnconfigure(0,weight=1)
        login_frame.rowconfigure(0,weight=1)
        login_frame.mainloop()
    #用户名检测是否合法
    def isLegal(self,string):
        if len(string)!=10:
            return False
        if string[0] not in ['U','M','D','I']:
            return False
        if int(string[1:5])>time.localtime(time.time()).tm_year:
            return False
        return True
    def loginCheck(self):
        id=self.id.get()
        password=self.password.get()
        
    def isLegalUser(self,id,password):
        file=open('user.csv','r',encoding='utf-8')

    def register(self):
        id=self.id.get()
        password=self.password.get()
        #检测是否有输入
        if len(id)==0 or len(password)==0:
            tkm.showerror(title='错误提示',message='学号密码不能为空')
            return 
        #检测非法字符
        for char in password:
            if not str(char).isalnum() and not str(char)=='_':
                tkm.showerror(title='错误提示',message='密码存在非法字符')
                return 
        if not self.isLegal(id):
            tkm.showerror(title='错误提示',message='该学号不存在')
            return
        #检测是否已经=注册
        with open('user.csv','r',encoding='utf-8') as f:
            reader=csv.reader(f)
            for row in reader:
                if id==str(row[0]):
                    tkm.showerror(title='错误提示',message='该用户已注册')
                    return
        #写入文件
        with open('user.csv','a',encoding='utf-8',newline='') as file:
            csv_writer=csv.writer(file)
            csv_writer.writerow([id,password])
        tkm.showinfo(title='系统提示',message='注册成功')
        return True
        
    
        


