import random

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

class Student:
    def __init__(self, name):
        self.name  = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

teacher = Teacher('花子')

for i in range(100):

    student = Student('student_' + str(i))
    student.set_score(random.randint(1, 100))

    teacher.add_student(student)

print(teacher.get_name() + '先生の計算によると、')
print('全体の人数は：{0}人'.format(len(teacher.students)))
print('全体の平均は：{0}点'.format(teacher.calc_average()))
print('最高得点は{0}点'.format(teacher.get_max_score()))
print('最低得点は{0}点'.format(teacher.get_min_score()))
print('でした。次も頑張って下さい')