
class Student:

    def __init__(self, sid, name, score, point, result, parents):
        self.sid = sid
        self.name = name
        self.score = score
        self.total_point = point
        self.result_judge = result
        self.parents = parents
        self.bags = []

    def set_sid(self, sid):
        self.sid = sid

    def set_name(self, name):
        self.name = name

    def set_score(self, score):
        self.score = score

    def set_total_point(self, point):
        self.total_point += point

    def set_parent_name(self, oya_name):
        self.parents = oya_name

    def get_score(self):
        return self.score

    def set_result_judge(self, oya_judge):
        self.result_judge = oya_judge

