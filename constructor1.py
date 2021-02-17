# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:03:31 2020

@author: LENOVO
"""

class Computer:
    
    def __init__(self):
        self.name = 'Umesh'
        self.age = 21
    
    def update(self):
        self.age = 30
    
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
            
    
c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are Different")
    
   
#c1.name = 'Maahi'
#c1.update()

print(c1.name)
print(c2.name)