import tkinter as tk
import tkinter.messagebox as tkm

class LoginPage(object):
    def __init__(self,master=None):
        self.root=master
        self.root.geometry('450x300')
        self.id=tk.StringVar()
        self.password=tk.StringVar()
        self.createPage()
    def createPage(self):
        #文字
        self.page=tk.Frame(self.root,bg='white')
        self.page.pack(expand='YES',fill='both')
        tk.Label(self.page,text='学生成绩查询系统',font=('华文行楷',20),width=30,height=2).grid(row=1,column=1)
        tk.Label(self.page,text='用户名',width=30,height=2).place(x=-5,y=130)
        tk.Label(self.page,text='密码',width=30,height=2).place(x=-5,y=175)
        #用户名输入 密码输入
        user_id=tk.Entry(self.page,textvariable=self.id,show=None,font=('Arial',14))
        user_id.place(x=130,y=140)
        user_password=tk.Entry(self.page,textvariable=self.password,show='*',font=('Arial',14))
        user_password.place(x=130,y=180)
        #按钮
        tk.Button(self.page,text='注册',width=10,height=1,command=None).place(x=70,y=230)
        tk.Button(self.page,text='登陆',width=10,height=1,command=None).place(x=190,y=230)
        tk.Button(self.page,text='退出',width=10,height=1,command=None).place(x=310,y=230)
    def loginCheck(self):
        pass
    def register(self):
        pass
        
    
        

