# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:20:08 2020

@author: LENOVO
"""
nums= []
no_of_in = int(input("Give no of inputs: "))
for i in range(no_of_in):
    print("Give",i+1,"th no:", sep=" ", end=" ")
    o = int(input())
    nums.append(o)
    
l = len(nums)
nums.sort()
print("Maximum value of them is:",nums[l-1])
    