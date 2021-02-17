# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:43:40 2020

@author: LENOVO
"""
#Duck typing means, a bird which behaves like a duck, walk like a duck, talks like a duck then it is a 'duck'
#Here we are concern about class's behaviour


class Spyder:
    
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


class Laptop:
    
    def code(self, ide):
        ide.execute()
 
        
#ide = Spyder() 

#Doesnt matter whether execute is of MyEditor or execute it will call execute instance

#Or
ide = MyEditor()       
        
lap1 = Laptop()
lap1.code(ide)