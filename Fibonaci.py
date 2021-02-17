# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:33:26 2020

@author: LENOVO
"""

n = int(input("Give the number:"))


def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
         
for i in range(n):
    print(fibo(i), sep="" , end=", ") 

    