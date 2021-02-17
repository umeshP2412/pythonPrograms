# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 21:33:17 2020

@author: LENOVO
"""
'''
Decorators can be called modifiers also
Suppose you have written a program and made many functions 
But now you/someone :) wants a bit change (same for every func.) in every function 
then will you go to modify every function one by one??? 
No!!! ...........Here comes important role of 'decorators'

we can use them by calling with '@' before the function (In which you want modification)
'''



def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

'''Upper shown are modification function'''


@strong     #Here by applying '@<modification Func.>' we can modify below one
@emphasis
def greet(): #this is the function in which we want modification
    return 'Hello!'

#this below function gives strong and emphasis (In stack manner) wrapped around:
print(greet())

