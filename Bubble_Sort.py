# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:58:30 2020

@author: LENOVO
"""

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]> nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1] = temp
                print('comparing',nums[j],'&',nums[j+1])
                print(nums)
        print(j)
    print(i)

nums = [5,3,8,6,7,2]

sort(nums)

print(nums)


















