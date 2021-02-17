# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:08:21 2020

@author: LENOVO
"""

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
    
n = int(input("Enter a number:"))

print(factorial(n))