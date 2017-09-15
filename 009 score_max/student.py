# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:24:22 2017

@author: mysurface
"""

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