# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:31:04 2020

@author: LENOVO
"""

def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(switcher.get(argument, "Invalid month"))
    
argument= int(input("Give Month num: "))    
switch_demo(argument)