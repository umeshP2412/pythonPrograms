# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:06:30 2020

@author: LENOVO
"""
#we use generator when we want to fetch a large amount of list and do some manipulation over it one by one
 
def topten():
        
    n =1
    while n<=10:
        var = n*n
        yield var    #we use yield instead of return because return will terminate the loop
        n += 1
    
values = topten()

for i in values:
    print(i)