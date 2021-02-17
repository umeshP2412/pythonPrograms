# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:49:11 2020

@author: LENOVO
"""
#Armstrong
def Armstrong(v):
    for i in range(v):
        num = i
        result=0
        n=len(str(i))
        while(i!= 0):
            digit = i%10
            result= result+digit**n
            i = i//10
        
        if num ==result:
            print(result)
            
            
            
v= int(input("give Limit value"))
Armstrong(v)