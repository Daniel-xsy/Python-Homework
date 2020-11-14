import tkinter as tk
import register

window=tk.Tk()
window.title=('学生成绩录入系统')
window.geometry('450x300')

var=tk.StringVar()

tk.Label(window,text='学生成绩查询系统',font=('Arial',16),width=30,height=2).place(x=35,y=50)
tk.Label(window,text='用户名',width=30,height=2).place(x=15,y=120)
tk.Label(window,text='密码',width=30,height=2).place(x=15,y=165)
#canvas =  tk.Canvas(window,height = 200,width = 500)

#用户名输入
user_id=tk.Entry(window,show=None,font=('Arial',14))
user_id.place(x=145,y=130)
#user_id.pack()

#密码输入
user_password=tk.Entry(window,show='*',font=('Arial',14))
user_password.place(x=145,y=170)
#user_password.pack()

botton1=tk.Button(window,text='注册',width=10,height=1,command=None)
botton1.place(x=130,y=230)

botton2=tk.Button(window,text='登陆',width=10,height=1,command=None)
botton2.place(x=220,y=230)
#botton2.pack()

window.mainloop()
'''
t=tk.Text(window,height=3)

def insert_id():
    var=user_id.get()
    t.insert('insert',var)
def insert_password():
    var=user_password.get()
    t.insert('end',var)
'''

