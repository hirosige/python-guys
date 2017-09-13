# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:06:53 2017

@author: mysurface
"""

import random
import teacher
import student
        
teacher = Teacher('花子')

for i in range(1000000):

    student = Student('student_' + str(i))
    student.set_score(random.randint(1, 100))

    teacher.add_student(student)

print(teacher.get_name() + '先生の計算によると、')
print('全体の人数は：{0}人'.format(len(teacher.students)))
print('全体の平均は：{0}点'.format(teacher.calc_average()))
print('でした。次も頑張って下さい')