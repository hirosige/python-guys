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

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_student(self, student):
        self.students.append(student)

    def calc_average(self):
        total = 0

        for student in self.students:
            total += student.get_score()

        return total / len(self.students)