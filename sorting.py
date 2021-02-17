# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:06:45 2020

@author: LENOVO
"""
numbs= []
h= int(input("Give no of inputs you want to give:/n"))

for i in range(h):
    y= int(input("Give number:"))
    numbs.append(y)

print(numbs)

"""
numbs.sort()

print(numbs)
    
"""
for i in range(len(numbs)-1,0,-1):
    for j in range(i):
        if numbs[j] > numbs[j+1]:
            temp= numbs[j]
            numbs[j]= numbs[j+1]
            numbs[j+1]= temp

print(numbs)            