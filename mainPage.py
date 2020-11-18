from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkm
import csv

class mainPage(object):
    def __init__(self,master=None,id=None,user=None):
        self.root=master
        self.id=id
        self.user=user
        if self.user=='student':
            self.creatStudentPage()
        else:
            self.creatTeacherPage()
    def creatStudentPage(self):
        frame=ttk.Frame(self.root)
        frame.grid()
        inquire_button=ttk.Button(frame,text='成绩查询',command=None)
        inquire_button.grid()
        frame.mainloop()
    def creatTeacherPage(self):
        frame=ttk.Frame(self.root)
        frame.grid()
        inquire_button=ttk.Button(frame,text='学生成绩查询',command=None)
        class_button=ttk.Button(frame,text='班级成绩查询',command=None)
        input_button=ttk.Button(frame,text='成绩录入',command=None)
        inquire_button.grid(row=1,column=1)
        class_button.grid(row=2,column=1)
        input_button.grid(row=2,column=1)
        frame.mainloop()

class studentPage(mainPage):
    def __init__(self):
        pass
        
class teacherPage(mainPage):
    def __init__(self):
        pass
    def inputGrade(self):
        pass