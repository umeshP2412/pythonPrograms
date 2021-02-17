# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:31:49 2020

@author: LENOVO
"""

a =5
b=2.5

try:
    print("File opened")
    print(a/b) 
    k = int(input("give any integer:\n"))
    print(k)
       #compiler will try to solve this and if error occurs it will jump to ...exception.....
except ZeroDivisionError:
    print("Hey, you can't divide by zero")      #...ZeroDivision error exception

except ValueError:
    print("Invalid input")    #...value error exception
    
except Exception:
    print("Something went wrong")     #...General type of error & exception for that
    
finally:
    print("file closed")      #whererver the compiler goes (in try or exception) it will execute this block (as a use of file closing)
    
print("Bye")