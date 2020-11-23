import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm
import pandas as pd
import time
import csv
import mainPage

class LoginPage(object):
    def __init__(self,master=None):
        self.root=master
        self.frame=ttk.Frame(self.root,padding=(10,10,10,10),relief='sunken',width=400,height=550)
        self.choice_frame=None
        self.id=tk.StringVar()
        self.password=tk.StringVar()
        self.name=tk.StringVar()
        self.name.set('仅在注册时输入')
        self.user=None
        self.choicePage()
    def choicePage(self):
        #清除上一次页面
        self.frame.destroy()
        self.choice_frame=ttk.Frame(self.root,padding=(10,10,10,10),\
            relief='sunken',width=400,height=550)
        self.choice_frame.pack(expand='YES',anchor='center')
        text_label=ttk.Label(self.choice_frame,text='请选择您的身份')
        student_button=ttk.Button(self.choice_frame,text='我是学生',command=self.student)
        teacher_button=ttk.Button(self.choice_frame,text='我是老师',command=self.teacher)
        text_label.grid(row=1,column=1,columnspan=3,pady=10)
        student_button.grid(row=2,column=1,columnspan=3,pady=5)
        teacher_button.grid(row=3,column=1,columnspan=3,pady=5)
    def student(self):
        self.user='student'
        self.choice_frame.destroy()
        self.createPage()
    def teacher(self):
        self.user='teacher'
        self.choice_frame.destroy()
        self.createPage()
    def createPage(self):
        self.frame=ttk.Frame(self.root,padding=(10,10,10,10),relief='sunken',width=400,height=550)
        self.frame.pack(expand='YES',anchor='center')
        title=ttk.Label(self.frame,text='学生成绩管理系统',font=('华文行楷',20))
        name_label=ttk.Label(self.frame,text='姓名')
        if self.user=='student':
            id_label=ttk.Label(self.frame,text='学号')
        else:
            id_label=ttk.Label(self.frame,text='编号')
        pass_lable=ttk.Label(self.frame,text='密码')

        image_file=tk.PhotoImage(file='hust.gif')
        hust_lable=ttk.Label(self.frame,image=image_file)

        user_entry=ttk.Entry(self.frame,textvariable=self.id,font=('Arial',14))
        pass_entry=ttk.Entry(self.frame,textvariable=self.password,show='*',font=('Arial',14))
        name_entry=ttk.Entry(self.frame,textvariable=self.name,font=('Arial',14))

        button1=ttk.Button(self.frame,text='注册',command=self.register)
        button2=ttk.Button(self.frame,text='登陆',command=self.loginCheck)
        button3=ttk.Button(self.frame,text='返回',command=self.choicePage)

        title.grid(row=1,column=3,rowspan=2,columnspan=3)
        hust_lable.grid(row=4,column=3,rowspan=2,columnspan=3,sticky='N')
        name_label.grid(row=8,column=3,rowspan=2)
        id_label.grid(row=10,column=3,rowspan=2)
        pass_lable.grid(row=12,column=3,rowspan=2)
        name_entry.grid(row=8,column=4,rowspan=2,columnspan=2,pady=5)
        user_entry.grid(row=10,column=4,rowspan=2,columnspan=2,pady=5)
        pass_entry.grid(row=12,column=4,rowspan=2,columnspan=2,pady=5)
        button1.grid(row=14,column=3,rowspan=2,pady=3)
        button2.grid(row=14,column=4,rowspan=2,pady=3)
        button3.grid(row=14,column=5,rowspan=2,pady=3)
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(0,weight=1)
        self.frame.mainloop()
    #用户名检测是否合法
    def isLegal(self,string):
        #学生
        if self.user=='student':
            if len(string)!=10:
                return False
            if string[0] not in ['U','M','D','I']:
                return False
            if int(string[1:5])>time.localtime(time.time()).tm_year:
                return False
            return True
        #老师
        else:
            return True

    def loginCheck(self):
        id=self.id.get()
        password=self.password.get()
        user=self.user
        if self.isLegalUser(id,password):
            tkm.showinfo(title='系统提示',message='登陆成功')
            self.frame.destroy()
            #进入主功能界面
            mainPage.mainPage(self.root,id,user)
            pass
        else:
            tkm.showerror(title='错误提示',message='账号或密码错误')
            return
    #检测登陆信息
    def isLegalUser(self,id,password):
        with open(self.user+'s.csv','r',encoding='utf-8') as file:
            reader=csv.reader(file)
            for row in reader:
                if id==row[0] and password==row[2]:
                    return True
            return False
    #注册
    def register(self):
        id=self.id.get()
        password=self.password.get()
        name=self.name.get()
        #检测是否有输入
        if len(id)==0 or len(password)==0 \
            or len(name)==0:
            tkm.showerror(title='错误提示',message='账号密码或名字不能为空')
            return 
        if len(password)<6:
            tkm.showerror(title='错误提示,',message='密码必须大于6位')
            return 
        #检测非法字符
        for char in password:
            if not str(char).isalnum() and not str(char)=='_':
                tkm.showerror(title='错误提示',message='密码存在非法字符')
                return 
        if not self.isLegal(id):
            tkm.showerror(title='错误提示',message='该学号不存在')
            return
        #检测是否已经注册
        with open(self.user+'s.csv','r',encoding='utf-8') as f:
            reader=csv.reader(f)
            for row in reader:
                if id==str(row[0]):
                    tkm.showerror(title='错误提示',message='该用户已注册')
                    return
        #写入文件
        with open(self.user+'s.csv','a',encoding='utf-8',newline='') as file:
            csv_writer=csv.writer(file)
            csv_writer.writerow([id,name,password,0,0,0,0])
        tkm.showinfo(title='系统提示',message='注册成功')
        return True
    
        


