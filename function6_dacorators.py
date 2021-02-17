# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 11:17:03 2019

@author: LENOVO
"""
def div(a, b):
    print(a/b)
    
    
def smart_div(func):
    
    def inner(a, b):
        if a < b:
            a, b = b, a
            
        return func(a, b)
    return inner

div1 = smart_div(div)

div1(2, 4)