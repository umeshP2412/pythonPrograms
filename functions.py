# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 22:12:39 2019

@author: LENOVO
"""
'''
def greet():
    print("Hello")
    print("Good Morning")
    
greet()'''

def add_sub(m, n):
    l = m+n
    b = m-n
    return l, b
m = int(input('Give 1st value: '))
n = int(input('Give 2nd value: '))

val1,val2= add_sub(m,n)
print(val1,val2)
