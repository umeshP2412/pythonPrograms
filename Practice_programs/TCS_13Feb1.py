# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:14:26 2020

@author: LENOVO
"""

class Account:
    def __init__(self, account_number, account_name, account_balance):
        self.account_number=account_number
        self.account_name=account_name
        self.account_balance=account_balance
       
    def depositAmount(self, depamnt):
        self.depamnt+=depamnt
    def withdrawAmount(self, withamnt):
        if self.account_balance-withamnt>= 1000:
            self.account_balance-=withamnt
            return 1
        else:
            return 0
        
if __name__=='__main__':
    account_number=int(input())
    account_name=input()
    account_balance=int(input())
    o= Account(account_number,account_name,account_balance)
    depamnt= int(input())
    withamnt= int(input())
    o.depositAmount(depamnt)
    result=o.withdrawAmount(withamnt)
    if result == 1:
        print('Current Balance is:', o.account_balance)
    else:
        print('Withdrawl not possible')