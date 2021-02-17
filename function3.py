# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 22:52:16 2019

@author: LENOVO
"""

def person(name, age=18):
    print(name)
    print(age-5)
    
person(age=21, name='umesh')
#person('umesh')


def sum(a, *b):
    c = a
    
    for i in b:
        c = c+i
    print(c)
    
sum(5, 6, 7, 8)
