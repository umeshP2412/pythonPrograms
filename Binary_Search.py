# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 17:59:17 2020

@author: LENOVO
"""
pos = -1

def search(lst, n):
    
    l=0
    u= len(lst)-1
    
    while l <= u:
        mid = (l+u)//2     #to get integer value of mid
        
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] <= n:
                l = mid+1
            else:
                u = mid-1
        
    return False

    
lst =  [4,7,8,12,45,99]

n=5


if search(lst,n):
    print("found @",pos+1)
    
else:
    print("Not found")