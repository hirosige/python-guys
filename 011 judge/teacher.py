import random


class Teacher:

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.students = []
        self.scores = []
        self.max_students = []
        self.min_students = []
        self.exam = 1
        self.num = 0

    def add_student(self, seito_obj):
        self.students.append(seito_obj)

    def set_score(self):
        self.score = random.randint(0, 100)
        self.scores.append(self.score)

    def get_score(self):
        return self.score

    def add_max_student(self, maxscore_student):
        self.max_students.append(maxscore_student)

    def add_min_student(self, minscore_student):
        self.min_students.append(minscore_student)

    def avecal(self):
        total = 0

        for i in self.students:
            total += i.score

        return total / len(self.students)

    def maxcalc(self):
        maxscore = max(self.scores)

        for i in self.students:
            if maxscore <= i.score:
                self.add_max_student(i)

    def mincalc(self):
        minscore = min(self.scores)

        for i in self.students:
            if minscore >= i.score:
                self.add_min_student(i)

    def clear_list(self):
        self.max_students.clear()
        self.min_students.clear()
        self.scores.clear()

    def to_string_scoring_result(self):
        print('-----第{0}回目のテスト結果-----'.format(self.exam))
        print('-----{0}先生の採点-----\n'.format(self.name))
        print('全体の人数は：{0}人'.format(len(self.students)))
        print('全体の平均は：{0}点\n'.format(self.avecal()))

    def to_string_maxmin(self):
        print('最高得点は：{0}点'.format(max(self.scores)))

        for i in self.max_students:
            print('{0}'.format(i.name))

        print('\n---------------\n')

        print('最低得点は：{0}点'.format(min(self.scores)))

        for i in self.min_students:
            print('{0}'.format(i.name))

        print('\n---------------\n')

    def serch_and_nextexm(self):
        while self.num == 0:
            print('検索する場合は、[1]を押して下さい')
            print('終了する場合は、[2]を押して下さい')
            print('テストを続行する場合は、[3]以上を押して下さい')

            self.num = input()
            self.num = int(self.num)

            if self.num == 1:
                number = input('検索したい生徒の番号を入力→')
                number = int(number)

                if number < len(self.students):
                    print('\n生徒ID：{0}'.format(self.students[number].sid))
                    print('氏名：{0}'.format(self.students[number].name))
                    print('今回の採点結果は{0}点'.format(self.students[number].score))
                    print('{0}さんの評価「{1}」でした'.format(self.students[number].parents, self.students[number].result_judge))
                    print('合計ポイントは{0}pt\n'.format(self.students[number].total_point))
                    self.num = 0

                else:
                    print('該当のIDは見つかりませんでした')
                    self.num = 0

            if self.num == 2:
                loop = 1
                return loop

            elif self.num >= 3:
                print('テストを実施')
                self.clear_list()
                self.exam += 1
                self.num = 0
                loop = 0
                return loop



