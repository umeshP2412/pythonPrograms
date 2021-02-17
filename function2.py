# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 22:39:50 2019

@author: LENOVO
"""

def update(x):
    print(id(x))
    x=8
    print(id(x))
    print(x)

a=10
print(id(a))
update(a)
print(a)
#here int a won't change the value int is immutable but...


def update(lst):
    print(id(lst))
    lst[1]=25
    lst.append(45)
    print(id(lst))
    print(lst)
    
lst=[10,20,30]
print(id(lst))
update(lst)
print(lst)

#here lst is changing because lst is list and it is mutable