from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkm
import csv
import pandas as pd

class mainPage(object):
    def __init__(self,master=None,id=None,user=None):
        self.root=master
        self.infor_frame=None
        self.id=id
        self.user=user
        self.search_input=StringVar()
        if user=='student':
            studentPage(self.root,self.id)
        else:
            teacherPage(self.root,self.id)
    def searchPage(self):
        self.infor_frame=ttk.Frame(self.root)
        self.infor_frame.grid()
        search_lable=ttk.Label(self.infor_frame,text='请输入学生姓名或学号')
        search_entry=ttk.Entry(self.infor_frame,textvariable=self.search_input)
        search_button=ttk.Button(self.infor_frame,text='确认',command=self.searchGrade)
        name_label=ttk.Label(self.infor_frame,text='姓名')
        id_label=ttk.Label(self.infor_frame,text='学号')

        search_lable.grid(row=1,column=1,columnspan=2,pady=5)
        search_entry.grid(row=2,column=1,columnspan=2,padx=5)
        search_button.grid(row=2,column=3)
        name_label.grid(row=3,column=1,padx=2,pady=3)
        id_label.grid(row=3,column=2,padx=2)
    def searchGrade(self):
        string=self.search_input.get()
        with open('students.csv','r',encoding='utf-8') as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0]==string or row[1]==string:
                    name=str(row[1])
                    id=str(row[0])
                    grade=[None]*(len(row)-4)
                    grade_lable=[None]*(len(row)-4)
                    for i in range(len(row)-4):
                        grade[i]=str(row[4+i])
                        grade_lable[i]=ttk.Label(self.infor_frame,text=grade[i])
                    name_label=ttk.Label(self.infor_frame,text=name)
                    id_lable=ttk.Label(self.infor_frame,text=id)
                    #grade_lable=ttk.Label(self.infor_frame,text=grade)
                    name_label.grid(row=4,column=1,padx=3)
                    id_lable.grid(row=4,column=2,padx=3)
                    for i in range(len(row)-4):
                        grade_lable[i].grid(row=5+i,column=1,columnspan=3)
                    return
            tkm.showwarning(title='系统提示',message='未查找到任何信息')
            return
    def classGrade(self):
        data=pd.read_csv('students.csv')
        course=data.keys()
        course_number=len(course)
        
        with open('students.csv','r',encoding='utf-8') as file:
            reader=csv.reader(file)
            grade=list(reader)
            for k in range(course_number)
    def getAverage(self,subject):
        pass
    def getLimit(self,subject):
        pass
    def getRank(self)
        pass
    def getPlot(self)
        pass
            





class studentPage(mainPage):
    def __init__(self,master=None,id=None):
        self.root=master
        self.id=id
        self.creatStudentPage()
    def creatStudentPage(self):
        frame=ttk.Frame(self.root)
        frame.grid()
        inquire_button=ttk.Button(frame,text='成绩查询',command=self.getGrade)
        inquire_button.grid()
        frame.mainloop()
    def getGrade(self):
        frame=ttk.Frame(self.root)
        frame.grid()
        with open('students.csv','r',encoding='utf-8') as file:
            reader=csv.reader(file)
            for row in reader:
                if self.id==row[0]:
                    grade=row[4:]
                    grade_lable=[None]*len(grade)
                    for i in range(len(grade)):
                        grade_lable[i]=ttk.Label(frame,text=str(grade[i]))
                        grade_lable[i].grid(row=i+1,column=1,pady=2)
                    return grade
            tkm.showwarning(title='系统提示',message='成绩还未录入')
            return

        
class teacherPage(mainPage):
    def __init__(self,master=None,id=None):
        self.root=master
        self.id=id
        self.search_input=StringVar()
        self.creatTeacherPage()
    def creatTeacherPage(self):
        frame=ttk.Frame(self.root)
        frame.grid()
        inquire_button=ttk.Button(frame,text='学生成绩查询',command=self.searchPage)
        class_button=ttk.Button(frame,text='班级成绩查询',command=None)
        input_button=ttk.Button(frame,text='成绩录入',command=None)
        inquire_button.grid(row=1,column=1)
        class_button.grid(row=2,column=1)
        input_button.grid(row=2,column=1)
        frame.mainloop()
    def inputGradePage(self):
        pass

