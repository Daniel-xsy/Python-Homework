import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm
import csv
import pandas as pd
import data as dt

#主界面
class mainPage(object):
    def __init__(self,master=None,id=None,user=None):
        self.root=master
        self.infor_frame=None
        self.welcome_frame=None
        self.id=id
        self.user=user
        self.search_input=tk.StringVar()
        self.welcomePage()
        if user=='student':
            studentPage(self.root,self.id)
        else:
            teacherPage(self.root,self.id)
    def welcomePage(self):
        self.welcome_frame=ttk.Frame(self.root)
        self.welcome_frame.pack(pady=10)
        name=dt.getInfor(self.id,self.user)['姓名']
        welcome_label=ttk.Label(self.welcome_frame,text='欢迎,'+name)
        welcome_label.pack()
    #班级成绩查询
    def showClassData(self):
        #销毁前一次界面
        self.infor_frame.destroy()
        self.infor_frame=ttk.Frame(self.root,padding=(10,10,10,10),relief='sunken')
        self.infor_frame.pack()
        index='科目   平均分   最高分   最低分'
        index_label=ttk.Label(self.infor_frame,text=index)
        data=dt.classGrade()
        data_label=ttk.Label(self.infor_frame,text=data)
        return_button=ttk.Button(self.infor_frame,text='返回',command=self.return_menu)

        index_label.grid(row=1,column=1)
        data_label.grid(row=2,column=1,pady=10)
        return_button.grid(row=3,column=1,pady=10)
        return
    def return_menu(self):
        self.infor_frame.destroy()
        if self.user=='student':
            studentPage(self.root,self.id)  
        else:
            teacherPage(self.root,self.id)      
    def quit(self):
        self.welcome_frame.destroy
        self.infor_frame.destroy()
        pass
        


#学生端界面
class studentPage(mainPage):
    def __init__(self,master=None,id=None):
        self.root=master
        self.id=id
        self.user='student'
        self.creatStudentPage()

    def creatStudentPage(self):
        self.infor_frame=ttk.Frame(self.root,padding=(10,10,10,10),relief='sunken')
        self.infor_frame.pack()
        inquire_button=ttk.Button(self.infor_frame,text='个人成绩查询',command=self.searchPage)
        class_button=ttk.Button(self.infor_frame,text='班级成绩情况',command=self.showClassData)
        return_button=ttk.Button(self.infor_frame,text='退出登陆',command=None)

        inquire_button.grid(row=1,column=1,padx=10,pady=10)
        class_button.grid(row=2,column=1,padx=10,pady=10)
        return_button.grid(row=3,column=1,padx=10,pady=10)
        self.infor_frame.mainloop()
    def searchPage(self):
        #销毁前一次界面
        self.infor_frame.destroy()
        self.infor_frame=ttk.Frame(self.root,padding=(10,10,10,10),relief='sunken')
        self.infor_frame.pack()
        data=dt.getInfor(self.id,self.user)
        data=dt.normalization(data)
        data_label=ttk.Label(self.infor_frame,text=data)
        return_button=ttk.Button(self.infor_frame,text='返回',command=self.return_menu)

        data_label.grid(row=1,column=1)
        return_button.grid(row=2,column=1)
        pass



#教师端界面
class teacherPage(mainPage):
    def __init__(self,master=None,id=None):
        self.root=master
        self.id=id
        self.user='teacher'
        self.search_input=tk.StringVar()
        self.creatTeacherPage()
    #教师端界面
    def creatTeacherPage(self):
        self.infor_frame=ttk.Frame(self.root,padding=(10,10,10,10),relief='sunken')
        self.infor_frame.pack()
        inquire_button=ttk.Button(self.infor_frame,text='学生成绩查询',command=self.searchPage)
        class_button=ttk.Button(self.infor_frame,text='班级成绩查询',command=self.showClassData)
        input_button=ttk.Button(self.infor_frame,text='成绩录入',command=self.putGradePage)
        return_button=ttk.Button(self.infor_frame,text='退出登陆',command=None)

        inquire_button.grid(row=1,column=1,padx=10,pady=10)
        class_button.grid(row=2,column=1,padx=10,pady=10)
        input_button.grid(row=3,column=1,padx=10,pady=10)
        return_button.grid(row=4,column=1,padx=10,pady=10)
        self.infor_frame.mainloop()
    def returnFun(self):
        self.infor_frame.destroy()
        self.creatTeacherPage()    
    #成绩查询界面
    def searchPage(self):
        #销毁前一次界面
        self.infor_frame.destroy()
        #重新绘制界面
        self.infor_frame=ttk.Frame(self.root,padding=(10,10,10,10),relief='sunken')
        self.infor_frame.pack()
        search_lable=ttk.Label(self.infor_frame,text='请输入学生姓名或学号')
        search_entry=ttk.Entry(self.infor_frame,textvariable=self.search_input)
        search_button=ttk.Button(self.infor_frame,text='确认',command=self.showStudentData)
        return_botton=ttk.Button(self.infor_frame,text='返回',command=self.returnFun)

        search_lable.grid(row=1,column=1,columnspan=2,pady=5)
        search_entry.grid(row=2,column=1,columnspan=2,padx=5,pady=2)
        search_button.grid(row=2,column=4,columnspan=2,padx=5,pady=2)
        return_botton.grid(row=3,column=4,columnspan=2)
    #成绩查询函数
    def showStudentData(self):
        string=self.search_input.get()
        data=dt.getInfor(string,'student')
        if data==None:
            tkm.showwarning(title='系统提示',message='未查找到任何信息')
            return
        data=dt.normalization(data)
        infor_label=ttk.Label(self.infor_frame,text=data)
        infor_label.grid(row=4,column=2,pady=10)
        return
    def putGradePage(self):
        namelist=tk.StringVar()
        self.infor_frame.destroy()
        self.infor_frame=ttk.Frame(self.root,padding=(10,10,10,10),relief='sunken')
        self.infor_frame.pack()
        #创建滚动条
        scrollbar=ttk.Scrollbar(self.infor_frame)
        #获取姓名列表 (1+n)*2 n+1:学生数和第一行的标签 2:学号+姓名
        namelist.set(dt.getNameList()[1:])
        name_list=tk.Listbox(self.infor_frame,listvariable=namelist,\
            height=8,yscrollcommand=scrollbar.set)
        #将滚动条与姓名列表联动
        scrollbar.config(command=name_list.yview)
        return_button=ttk.Button(self.infor_frame,text='返回',command=self.returnFun)

        scrollbar.grid(row=1,rowspan=2,pady=5,column=3,sticky='wns')
        name_list.grid(row=1,column=1,columnspan=2)
        return_button.grid(row=3,column=1,columnspan=2,sticky='n',pady=5)

        #双击学生姓名触发事件
        name_list.bind(sequence='<Double-1>',func=self.changeGrade)
        #name_list.bind(sequence='KeyPress-enter',func=self.changeGrade)

    def changeGrade(self,event):
        def fun():
            grade_list=[None]*len(grade)
            for i in range(len(grade)):
                grade_list[i]=grade_var[i].get()
            dt.writeGrade(grade_list,sequence=choice[0])
        choice=event.widget.curselection()
        self.infor_frame.destroy()
        self.infor_frame=ttk.Frame(self.root,padding=(10,10,10,10),relief='sunken')
        self.infor_frame.pack()
        frame1=ttk.Frame(self.infor_frame)
        frame2=ttk.Frame(self.infor_frame)
        frame3=ttk.Frame(self.infor_frame)
        frame1.grid(row=1,column=1)
        frame2.grid(row=1,column=2,padx=5)
        frame3.grid(row=2,column=1,columnspan=2)
        #按照序列号获取学生信息 data为字典类型
        data=dt.getInfor(sequence=int(choice[0]))
        information,grade=dt.normalization3(data)
        confirm_button=ttk.Button(frame3,text='保存',\
            command=fun)
        return_botton=ttk.Button(frame3,text='返回',\
            command=(lambda self: self.putGradePage)(self))
        #输出学号、姓名、课程等提示信息
        infor_label=ttk.Label(frame1,text=information)
        #创建和课程项目数相同的输入框 每个输入框内默认为原课程分数
        grade_var=[None]*len(grade)
        entry_arr=[None]*len(grade)
        for i in range(len(grade)):
            grade_var[i]=tk.StringVar()
            grade_var[i].set(str(grade[i]))
            entry_arr[i]=ttk.Entry(frame2,textvariable=grade_var[i])
            entry_arr[i].grid(row=i+1,column=1,columnspan=2,pady=5)
        infor_label.grid(row=1,column=1)
        return_botton.grid(row=1,column=2)
        confirm_button.grid(row=1,column=1)
        self.infor_frame.mainloop()


        
        
