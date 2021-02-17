# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 18:55:21 2019

@author: LENOVO
"""

#from numpy import *

arr1= array([2,3,4,5,2,3,2])


#arr2= array([1,2,3,5,3,2,3])
#arr = arr1+arr2

arr2 = arr1.copy()

arr1[1]=1
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

