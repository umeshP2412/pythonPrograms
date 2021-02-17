# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 22:09:17 2020

@author: LENOVO
"""

class Employee:
    def __init__(self, emp_no,emp_name,leaves):
        self.emp_no=emp_no
        self.emp_name=emp_name
        self.leaves=leaves
        
class Company:
    def __init__(self, company_name,emps):
        self.company_name= company_name
        self.emps = emps
     
    def display_leave(self, emp_no1,Ltype):
        for i in self.emps:
            if i.emp_no==emp_no1:
                return i.leaves[Ltype]
            
    def Number_of_leaves(self,emp_no1,Ltype,nol):
        for i in self.emps:
            if i.emp_no==emp_no1:
                if i.leaves[Ltype]>=nol:
                    return "Granted"
                else:
                    return "Rejected"
                
n = int(input())
emps=[]
c= Company("ABC",emps)
leaves={}
for i in range(n):c
    emp_no=int(input())
    emp_name=input()
    leaves["CL"]= int(input())
    leaves["EL"]= int(input())
    leaves["SL"]= int(input())
    c.emps.append(Employee(emp_no,emp_name,leaves))

emp_no1=int(input())
Ltype= input()
nol=int(input())
print(c.display_leave(emp_no1,Ltype))
print(c.Number_of_leaves(emp_no1,Ltype,nol))




