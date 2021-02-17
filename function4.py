# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 10:42:18 2019

@author: LENOVO
"""
def person(name, **data):
    print(name)
    print(data.items())
    print(data['age'])
    for i, j in data.items():
        print(i, j)
        print(i)
        print(j)
    
    

person('umesh', age=28, city='Ahmedabad', mob=9558829646)
