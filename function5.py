# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 10:55:53 2019

@author: LENOVO
"""
def count(lst):
    even= 0
    odd= 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = [20, 11, 22, 45, 65, 85, 13, 89, 78, 66]

even, odd = count(lst)

print('even=', even, 'odd=', odd)

print("Even : {} and Odd : {}".format(even, odd))