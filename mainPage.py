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
        pass
    def creatTeacherPage(self):
        pass