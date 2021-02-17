# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:39:14 2020

@author: LENOVO
"""


class Car:
    wheels = 4  # Class variable

    def __init__(self):
        self.mil = 10  # Method variable
        self.com = "BMW"


c1 = Car()
c1.mil = 8

c2 = Car()

Car.wheels = 6  # to change class variable we use this
# c1.wheels = 6      #to change class variable only for that instance then use this

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
