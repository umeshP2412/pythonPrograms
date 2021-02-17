# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:17:50 2020

@author: LENOVO
"""


class Student:
    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # instance Method is normal method we use
        return (self.m1 + self.m2 + self.m3) / 3

    # instance method has to sub methods called accessors/gettors and mutators/settors

    def get_m1(self):  # gettors just get the value and return it
        return self.m1

    def set_m1(self, value):  # settors just modifies the value
        self.m1 = value
        return self.m1

    @classmethod  # Class method is special method
    def getSchool(cls):  # it doesn't pass self but passes cls (as class)
        return cls.school

    @staticmethod  # Static method is used when this class is used by another module
    def info():  # it doesn't need self or any argument, it is used in factorial kind of program where class doesn't
        # matter
        print("This is student class.... in abc module")  # It doesn't return any value but prints


s1 = Student(34, 47, 32)
s2 = Student(89, 32, 12)

print(s1.avg())
print(s2.avg())

print(Student.getSchool())  # Class methpd is called by class name as shown

print(Student.info())  # for Static also class name is used to call it

print(s1.get_m1())

print(s1.set_m1(56))
