# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:24:27 2020

@author: LENOVO
"""

#!/bin/python3


def countPrimeNumbers(numbers):
    # Write your code here

    count1 = 0
    for i in range(count):
       # print(i)
        if numbers[i] > 1:
            if numbers[i] == 2:
                count1 +=1
           # print("Entered in >1 for:",numbers[i])
            for j in range(2,numbers[i]):
              #  print(j)
                if (numbers[i]%j) == 0:
                    break
                else:
                    count1 +=1
        else:
            break
    return count1
    


if __name__ == '__main__':
    numbers=[]
    count=int(input())
    for i in range(count):
        numbers.append(int(input()))
        
    print(countPrimeNumbers(numbers))
        
