# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:49:35 2020

@author: LENOVO
"""

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

class Programmer(Employee):
    
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp
    
    def increase(self):
        self.salary = int(self.salary * (self.increment+0.2)) 
    
Dipak = Programmer("Dipak", "Wagh", 46000, "Python", "5")

print(Dipak.proglang)

print(help(Programmer))