# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:55:17 2020

@author: LENOVO
"""
def search(lst, n):
    m=0
    for i in lst:
        m = m+1
        if i== n:
            print(m)
            return True 
        
    return False



lst =  [5,8,4,6,9,2]

n=6 


if search(lst,n):
    print("found")
    
else:
    print("Not found")