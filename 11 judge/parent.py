import random

class Parent:

    def __init__(self, name, point, judge):
        self.name = name
        self.point = point
        self.judge = judge

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_judge(self, score):
        exval = random.randint(0, 100)

        if score < exval:
            self.judge = '期待以下でした'
            self.point = 1

        elif score == exval:
            self.judge = '期待通りでした'
            self.point = 3

        else:
            self.judge = '期待以上でした'
            self.point = 5

    def get_judge(self):
        return self.judge

    def get_point(self):
        return self.point



