# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:27:10 2020

@author: LENOVO
"""

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
        
    @classmethod    
    def from_str(clc, emp_string):
        fname, lname, salary = emp_string.split("-")
        return clc(fname, lname, salary)

Umesh = Employee("Umesh", "Patil", 75000)

Rohan = Employee("Rohan", "Mehra", 44000)

Lovish = Employee.from_str("Lovish-Jackson-76000")


print(Lovish.salary)


