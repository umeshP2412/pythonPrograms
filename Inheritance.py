# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:37:20 2020

@author: LENOVO
"""


class A:  # parent class

    def feature1(self):
        print('feature1 is working')

    def feature2(self):
        print('feature2 is working')


class B(A):  # child class, This will have all instances of A class
    def feature3(self):
        print('feature3 is working')

    def feature4(self):
        print('Feature4 is workinf')


# class C(A,B):  #<------------- #use this for multiple inheritance so that C will have features of A and B if A & B are seperate

a1 = A()
a2 = A()

b1 = B()

a1.feature1()
b1.feature1()
