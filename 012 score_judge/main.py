# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:24:42 2017

@author: mysurface
"""

import random
import judge

score = input('テストの点数を入力して下さい。→')
score = int(score)
print(score)
mens = []
for i in range(11):
    judgeman = Judge('Judgeman' + str(i))

    standard = random.randint(0,100)
    judgeman.add_standard(standard)
    judgeman.judge_score(score)
    mens.append(judgeman)
