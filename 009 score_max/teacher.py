# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:24:21 2017

@author: mysurface
"""

class Teacher:
    def __init__(self, name):
        self.students = []
        self.average = 0
        self.name = name
        self.student_score_list = []
        
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_student(self, student):
        self.students.append(student)
        self.student_score_list.append(student.get_score())           
        
    def get_max_score(self):
        return max(self.student_score_list)
 
    def get_min_score(self):
        return min(self.student_score_list)     
        
    def calc_average(self):
        total = 0

        for student in self.students:
            total += student.get_score()

        return total / len(self.students)