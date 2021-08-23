# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 17:22:14 2019

@author: LENOVO
"""
vals = [5,9,8,4,2]

vals.append(8)
print(vals)
print(vals[1]+vals[2]+vals[5])
print(vals[1]+vals[2]+int(vals[5]))
print(vals)
vals.sort()

for i in vals:
    print(i)
    
newArr = vals

print(newArr)
