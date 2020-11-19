import csv
import pandas as pd

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

#获得单个学生/老师信息
#这里可设置可选参数 可通过多种方式查找学生的信息 id index name
def getInfor(id,user):
    f=pd.read_csv(user+'s.csv')
    index=list(f.keys())
    index.remove('密码')
    with open(user+'s.csv','r',encoding='utf-8') as file:
        reader=csv.reader(file)
        for row in reader:
            if id==row[0] or id==row[1]:
                data=row[0:2]+row[3:]
                dic=dict(map(lambda x,y: [x,y],index,data))
                return dic
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
        if max<subject[i]:
            max=subject[i]
        elif min>subject[i]:
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