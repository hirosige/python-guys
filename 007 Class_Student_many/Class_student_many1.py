# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:14:11 2017

@author: mysurface
"""

avg_score = 0

class Student:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

for i in range(1,100):

    student = Student()
    student.set_name('student' + str(i))
    student.set_score(0+i)

    print(student.get_name())
    print(student.get_score())
    
    avg_score += student.get_score() 
    
    average = avg_score / i
    print(average)

 
    
