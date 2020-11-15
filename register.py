import tkinter as tk
import tkinter.messagebox as tkm

window=tk.Tk()
window.title=('学生成绩录入系统')
window.geometry('450x300')

#文字
tk.Label(window,text='学生成绩查询系统',font=('华文行楷',20),width=30,height=2).place(x=40,y=0)
tk.Label(window,text='用户名',width=30,height=2).place(x=-5,y=130)
tk.Label(window,text='密码',width=30,height=2).place(x=-5,y=175)

#用户名输入 密码输入
user_id=tk.Entry(window,show=None,font=('Arial',14))
user_id.place(x=130,y=140)
user_password=tk.Entry(window,show='*',font=('Arial',14))
user_password.place(x=130,y=180)

#按钮
tk.Button(window,text='注册',width=10,height=1,command=None).place(x=70,y=230)
tk.Button(window,text='登陆',width=10,height=1,command=None).place(x=190,y=230)
tk.Button(window,text='退出',width=10,height=1,command=None).place(x=310,y=230)

#图片
canvas=tk.Canvas(window,height=75,width=98)
image_file=tk.PhotoImage(file='hust.gif')
image=canvas.create_image(50,-10,anchor='n',image=image_file)
canvas.place(x=170,y=50)

window.mainloop()

