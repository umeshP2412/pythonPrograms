# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:22:54 2020

@author: LENOVO
"""
def is_even(n):
    return n%2==0
    
def is_odd(n):
    return n%2!=0
     
nums = [3,2,6,8,4,6,2,9]

even= list(filter(is_even,nums))
odd= list(filter(is_odd, nums))
print(even) 
print(odd)