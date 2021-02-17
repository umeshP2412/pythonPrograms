# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:53:24 2020

@author: LENOVO
"""

f = open('MyData.txt','r')

#print(f.read())        #to read hall text file

#print(f.readline())      #read line only

f1= open('abc', 'a')    #to append in text file
'''To copy text from one file to another''' 

'''f1 = open('abc','w')     #for image use 'wb' or 'rb' instead of 'w'
for data in f:
    f1.write(data)'''
    
f1.write("Umesh Patil")


