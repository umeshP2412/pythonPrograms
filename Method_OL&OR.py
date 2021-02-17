# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:43:18 2020

@author: LENOVO
"""
#Method OverLoading
class Student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a=None,b=None,c=None):
        
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s =a
        return s
    
    
s1 = Student(25,52)

print(s1.sum(5,2,4))