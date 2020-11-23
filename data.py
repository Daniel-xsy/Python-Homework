import csv
import pandas as pd
import tkinter.messagebox as tkm

#将getInfor函数中返回的dic标准化为可输出格式
def normalization(data):
    string=''
    for key in data:
        string+=str(key)+'\t'+str(data[key])+'\n'
    return string

#将classGrade返回的数据标准化
def normalization2(data):
    string=''
    for i in range(len(data)):
        string+=data[i][0]+'\t'+str(data[i][1])+'\t'+\
            data[i][2]+'\t'+data[i][3]+'\n'
    return string

#将getInfo返回为key(str)和value(list)的形式
def normalization3(data):
    key=list(data.keys())
    value=list(data.values())
    #学号、姓名、平均分不可修改
    key=key[3:]
    value=value[3:]
    string=''
    for i in range(len(key)):
        string+='\n'+key[i]+'\n'
    return string,value

#获得单个学生/老师信息
#这里可设置可选参数 可通过多种方式查找学生的信息 id index name
def getInfor(id=None,user='student',sequence=None):
    f=pd.read_csv(user+'s.csv')
    index=list(f.keys())
    index.remove('密码')
    count=-1
    with open(user+'s.csv','r',encoding='utf-8') as file:
        reader=csv.reader(file)
        for row in reader:
            if id==row[0] or id==row[1] or count==sequence:
                data=row[0:2]+row[3:]
                dic=dict(map(lambda x,y: [x,y],index,data))
                return dic
            count+=1
        return None

'''
班级成绩信息汇总
grade是处理前的数据 mxn m:科目 n:学生成绩
data 分别为 科目名称 平均分 最高分 最低分
'''
def classGrade():
    grade=getGradeData()
    data=[None]*len(grade)
    for i in range(len(grade)):
        average=getAverage(grade[i][1:])
        max,min=getLimit(grade[i][1:])
        data[i]=[grade[i][0],round(average,2),max,min]
    return normalization2(data)

#得到成绩列表 grade: mx(n+1) m:总科数 n:学生数 第一项为科目名称
def getGradeData():
    data=pd.read_csv('students.csv')
    course=data.keys()
    course_number=len(course)-4
    grade=[[None]]*course_number
    for i in range(course_number):
        grade[i]=get_csv_Column(i+4)
    return grade

def get_csv_Column(column):
    with open('students.csv','r',encoding='utf-8') as file:
        reader=csv.reader(file)
        data=[row[column] for row in reader]
        return data

#计算平均值
def getAverage(subject):
    average=0.0
    for i in range(len(subject)):
        average+=float(subject[i])
    average/=len(subject)
    return average

#计算最高分 最低分
def getLimit(subject):
    max=subject[0]
    min=subject[0]
    for i in range(len(subject)):
        if int(max)<int(subject[i]):
            max=subject[i]
        if int(min)>int(subject[i]):
            min=subject[i]
    return max,min

#计算排名
def getRank(classgrade,grade):
    classgrade=sorted(classgrade,reverse=True)
    rank=classgrade.index(grade)
    return rank

#绘制成绩分布图
def getPlot():
    pass

#获得名单
def getNameList():
    with open('students.csv','r',encoding='utf-8') as file:
        reader=csv.reader(file)
        #为获取学生数 data 为mx(n+1) n为学生数
        data=getGradeData()
        namelist=[None]*len(data[0])
        count=0
        for row in reader:
            namelist[count]=row[0:2]
            count+=1
    #namelist 第一行为index 即 '学号,姓名'
    return namelist

#写入数据，既可以通过学号，也可以通过csv文件中的序列
def writeGrade(grade,id=None,sequence=None):
    filename='students.csv'
    data=pd.read_csv('students.csv',encoding='utf-8')
    course=list(data.head())#获取课程列表
    course=course[4:]
    for i in range(len(course)):
        data[course[i]].loc[sequence]=grade[i]
        #data['线性代数'].loc[sequence]=grade[1]
        #data['Python'].loc[sequence]=grade[2]
    data.to_csv(filename, encoding='utf-8',index=0)
    '''
    需要修改 data的索引值最好读出来，否则函数模块化程度不好
    '''