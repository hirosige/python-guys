import parent
import student


class Guide:

    def set_people(self, people, sensei):
        for i in range(people):
            self.oya = parent.Parent('name', 0, 'none')
            self.oya.set_name('parent_' + str(i))
            seito = student.Student('none', 'none', 0, 0, 'none', 'none')
            seito.set_sid(str(i))
            seito.set_name('student_' + str(i))
            seito.set_parent_name(self.oya.get_name())
            sensei.add_student(seito)

    def set_score_judge(self, people, sensei):
        for i in range(people):
            sensei.set_score()
            sensei.students[i].set_score(sensei.get_score())
            self.oya.set_judge(sensei.students[i].get_score())
            sensei.students[i].set_total_point(self.oya.get_point())
            sensei.students[i].set_result_judge(self.oya.get_judge())



