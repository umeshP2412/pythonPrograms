# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:25:21 2020

@author: LENOVO
"""
from calc import add

def fun1():
    add()
    add()
    print("from fun1")
    
    
def fun2():
    add()
    print("from fun2")
    

def main():    
    fun1()
    fun2()


main()