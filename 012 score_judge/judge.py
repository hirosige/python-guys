# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:43:13 2017

@author: mysurface
"""

class Judge:
    def __init__(self, name):
        self.name = name
        self.standards = []

    def add_standard(self, standard): 
        self.standards.append(standard)
        
    def judge_score(self, score):
        print(self.name)
        exval = random.choice(self.standards)
        if score < exval:
            print('期待以下')
            
        elif score == exval:
            print('期待通り')            
            
        else:
            print('期待以上!')