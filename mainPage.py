from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkm
import csv

class mainPage(object):
    def __init__(self,master=None,id=None,user=None):
        self.root=master
        self.id=id
        self.user=user
        if user=='student':
            studentPage(self.root)
        else:
            teacherPage(self.root)



class studentPage(mainPage):
    def __init__(self,master=None):
        self.root=master
        self.creatStudentPage()
    def creatStudentPage(self):
        frame=ttk.Frame(self.root)
        frame.grid()
        inquire_button=ttk.Button(frame,text='成绩查询',command=None)
        inquire_button.grid()
        frame.mainloop()

        
class teacherPage(mainPage):
    def __init__(self,master=None):
        self.root=master
        self.creatTeacherPage()
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
    def studentInforSearch(self):
        search_input=StringVar()
        search_lable=ttk.Label(self.root,text='请输入学生姓名或姓名')
        search_entry=ttk.Entry(self.root,textvariable=search_input)
        search_button=ttk.Button(self.root,text='确认')
        name_label=ttk.Label(self.root,text='姓名')
        id_label=ttk.Label(self.root,text='学号')

        search_lable.grid(row=1,column=1,columnspan=2,pady=5)
        search_entry.grid(row=2,column=1,columnspan=2,padx=5)
        search_button.grid(row=2,column=3)
        name_label.grid(row=3,column=1,padx=2,pady=3)
        id_label.grid(row=3,column=2,padx=2)
        infor=self.searchGrade(search_input.get())
        if infor:
            infor_label=ttk.Label(self.root,text=str(infor))
            infor_label.grid(row=4,rowspan=4)
        else:
            tkm.showwarning(title='系统提示',message='未查找到任何信息')
    def searchGrade(self,string):
        with open('students.csv','r',encoding='utf-8') as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0]==string or row[1]==string:
                    return row
            return None