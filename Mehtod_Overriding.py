# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:47:48 2020

@author: LENOVO
"""
#Method_overriding
class A:
    
    def show(self):
        print("in A show")
        
class B(A):
    def show(self):
        print("in B show")


        
a1= B()

a1.show()