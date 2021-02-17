# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:39:43 2020

@author: LENOVO
"""

class Employee:
    
    increment = 1.5
    no_of_employee = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
#        self.email = fname + lname + '@gmail.com'
        
        Employee.no_of_employee += 1
    
    def increase(self):
        self.salary = int(self.salary * self.increment)
        
    @property    
    def email(self):
        if self.fname == None and self.lname == None:
            return "Email is not available"
        else:
            return self.fname + '.' + self.lname + '@gmail.com'
    
    @email.setter
    def email(self, other_email):
        name_list = other_email.split('@')[0].split('.')
        print(name_list)
        self.fname = name_list[0]
        self.lname = name_list[1]
        
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
        
     
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

    
if __name__== '__main__':
    Dipak = Employee("Dipak", "Wagh", 46000)
    Parth = Employee("Parth", "Patel ", 40000)
    Rohit = Employee("Rohit", "Mehra", 25000)
    print(Dipak.email, Parth.email)
    Dipak.lname = "Patil"
    print(Dipak.email)
    Dipak.email = "Wagh.Dipak@gmail.com"
    print(Dipak.email)
    del Dipak.email
    print(Dipak.email)




