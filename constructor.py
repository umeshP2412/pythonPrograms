# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:42:56 2020

@author: LENOVO
"""

class A:               
    
    def __init__(self):
    #    super().__init__()
        print('in A init')

    def feature1(self):
        print('feature1 is working')
    def feature2(self):
        print('feature2 is working')
        
class B:           
  
    def __init__(self):
        super().__init__()  #without this you will get init of B only(check for B first) if object of B is made but this(super) will access init of A
        print('in B init')

    def feature3(self):
        print('feature3 is working')
    def feature4(self):
        print('Feature4 is working')
        
class C(A,B):
    def __init__(self):
  #      super().__init__()
        print("in C init")


b1 = B()
c1 = C()

c1.feature4()

