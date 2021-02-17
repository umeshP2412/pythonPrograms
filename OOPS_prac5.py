# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:15:28 2020

@author: LENOVO
"""

"""
Inheritance with Super() to inherit previous and some new function"""

class Employee:
    
    increment = 1.5
    no_of_employee = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1
    
    def increase(self):
        self.salary = int(self.salary * self.increment)
     
    @classmethod
    def change_increment(clc, amount):
        clc.increment = amount
        
    @classmethod    
    def from_str(clc, emp_string):
        fname, lname, salary = emp_string.split("-")
        return clc(fname, lname, salary)
    
    @staticmethod
    def isopen(day):
        if day == "Sunday" or day == "sunday":
            return "Chuutti Hai"
        else:
            return True
#These following are dunder method which acts like inbuilt function but created by you

    def __add__(self, other):
        return self.salary + other.salary
    
    def __repr__(self):
        return 'Employee ({}, {}, {})'.format(self.fname, self.lname, self.salary)
    
    def __str__(self):
        return 'The name of Employee is {} \nHis Salary is {}'.format(self.fname, self.salary)

Dipak = Employee("Dipak", "Wagh", 46000)
Parth = Employee("Parth", "Patel ", 40000)
Rohit = Employee("Rohit", "Mehra", 25000)

print(Parth)





