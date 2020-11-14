import tkinter as tk
import register

window=tk.Tk()
window.title=('学生成绩录入系统')
window.geometry('450x300')

var=tk.StringVar()

l=tk.Label(window,text='学生成绩录入系统',bg='gray',font=('Arial',16),width=30,height=2)
l.pack()
#canvas =  tk.Canvas(window,height = 200,width = 500)

#用户名输入
user_id=tk.Entry(window,show=None,font=('Arial',14))
user_id.pack()

button1=tk.Button(window,text='确定',width=10,height=2,command=None)
button1.pack()

#密码输入
user_password=tk.Entry(window,show='*',font=('Arial',14))
user_password.pack()

botton2=tk.Button(window,text='确定',width=10,height=2,command=None)
botton2.pack()

'''
t=tk.Text(window,height=3)

def insert_id():
    var=user_id.get()
    t.insert('insert',var)
def insert_password():
    var=user_password.get()
    t.insert('end',var)
'''



window.mainloop()
