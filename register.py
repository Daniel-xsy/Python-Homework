import tkinter as tk
import register

window=tk.Tk()
window.title=('学生成绩录入系统')
window.geometry('450x300')

var=tk.StringVar()

tk.Label(window,text='学生成绩查询系统',font=('华文行楷',20),width=30,height=2).place(x=40,y=10)
tk.Label(window,text='用户名',width=30,height=2).place(x=15,y=120)
tk.Label(window,text='密码',width=30,height=2).place(x=15,y=165)

#用户名输入
user_id=tk.Entry(window,show=None,font=('Arial',14))
user_id.place(x=145,y=130)

#密码输入
user_password=tk.Entry(window,show='*',font=('Arial',14))
user_password.place(x=145,y=170)

#按钮
tk.Button(window,text='注册',width=10,height=1,command=None).place(x=100,y=230)
tk.Button(window,text='登陆',width=10,height=1,command=None).place(x=190,y=230)
tk.Button(window,text='退出',width=10,height=1,command=None).place(x=250,y=230)

canvas=tk.Canvas(window,height=100,width=94)
image_file=tk.PhotoImage(file='hust.gif')
image=canvas.create_image(250,0,anchor='n',image=image_file)
canvas.pack()

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

