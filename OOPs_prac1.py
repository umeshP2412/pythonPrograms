# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:15:28 2020

@author: LENOVO
"""

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

Umesh = Employee("Umesh", "Patil", 44000)

Rohan = Employee("Rohan", "Mehra", 44000)

print(Umesh.salary)
Employee.change_increment(2)
Umesh.increase()
print(Umesh.salary)
print(Rohan.salary)


"""        
print(Employee.no_of_employee)      
Umesh = Employee("Umesh", "Patil", 44000)

print(Employee.no_of_employee)
Rohan = Employee("Rohan", "Mehra", 74000)

print(Employee.no_of_employee)
"""