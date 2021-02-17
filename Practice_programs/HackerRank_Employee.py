# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:40:19 2020

@author: LENOVO
"""

class Employee:
    def __init__(self,n,i,a,g):
        self.n=n
        self.i=i
        self.a=a
        self.g=g
class Organisation:
    def __init__(self,na,e):
        self.na=na
        self.e=e
    def addEmployee(self,n,i,a,g):
        s=Employee(n,i,a,g)
        self.e.append(s)
    def getEmployeeCount(self):
        return len(self.e)
    def findEmployeeAge(self,id):
        print(self.e)
        for i in self.e:
            print('In findEmployeeAge loop')
            print(i)
            print(i.i)
            
            if(i.i==id):
                return i.a
        return -1
    def countEmployees(self,ag):
        c=0
        for i in self.e:
            if(i.a>ag):
                print(i.a)
                c+=1
        return c


if __name__ == '__main__':
    employees=[]
    o = Organisation('XYZ',employees)
    n=int(input())
    for i in range(n):
        name=input()
        id=int(input())
        age=int(input())
        gender=input()
        o.addEmployee(name,id,age,gender)

    id=int(input())
    age=int(input())
    print(o.getEmployeeCount())
    print(o.findEmployeeAge(id))
    print(o.countEmployees(age))
