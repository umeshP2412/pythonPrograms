# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:52:24 2020

@author: LENOVO
"""

nums = [7,8,9,5]

#print(nums[2])        #One way to print values

'''for i in nums:
    print(i)'''            #second way to print value
'''    
it =iter(nums)
                              #third method
print(it.__next__())
'''
class TopTen:
    
    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):              #next of this...
        
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = TopTen()

print(next(values))      #....and next of this will not allow repetition of iteration

for i in values:
    print(i)