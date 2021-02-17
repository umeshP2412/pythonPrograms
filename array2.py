# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 18:13:26 2019

@author: LENOVO
"""
arr = []

n = int(input('Give length of array: '))

for i in range(n):
    print('Give', i+1, 'th value:',end=' ')
    x = int(input())
    arr.append(x)
    
    
print(arr)

val = int(input('Enter the value for search: '))
k=0
for e in arr:
    if e==val:
        print('THe position of no is:',k+1)
        break
        
    k+=1
    
print(arr.index(val)+1)