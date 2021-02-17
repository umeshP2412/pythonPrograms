# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:40:26 2020

@author: LENOVO
"""

#!/bin/python3

#Enter your code here. Read input from STDIN. Print output to STDOUT
class Student:

    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.per = None

    def calculate_percentage(self):
        l = len(self.marks)
        s = sum(self.marks)
        percentage = s//l
        self.per = percentage
        return percentage 

    def find_grade(self):
        percentage = self.per
        if percentage >= 80:
            g = 'A'
        elif percentage >=60:
            g = 'B'
        elif percentage >= 40:
            g = 'C'
        else:
            g = 'F'
        return g
                

if __name__ == '__main__':
    roll=int(input())
    name=input()
    count=int(input())
    marks=[]
    for i in range(count):
        marks.append(int(input()))
    s=Student(roll,name,marks)
    print(s.calculate_percentage())
    print(s.find_grade())