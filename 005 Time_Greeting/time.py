# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 12:13:07 2017

@author: mysurface
"""

import datetime # datetimeモジュールのインポート

d = datetime.datetime.today()

print(d.hour) # hour

if d.hour > 4 and d.hour < 11:
    print('おはよう')
    
elif d.hour > 11 and d.hour <18:
    print('こんにちわ')
    
elif d.hour >18 and d.hour <4:
    print('こんばんわ')

else:
    print('err')
    

    