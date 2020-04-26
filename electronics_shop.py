#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()
    bill=0
    if(b<(keyboards[0]+drives[0])):
        print("The customer can't buy 1 keyboard and 1 USB drive")
    else:
        keyboards.reverse()
        drives.reverse()
        for i in range(len(keyboards)):
            for j in range(len(drives)):
                if(keyboards[i]+drives[j]<=b):
                    if(bill<keyboards[i]+drives[j]):
                        bill=keyboards[i]+drives[j]
        print("The customer can spend maximum of",bill, "Rupees to buy 1 keyboard and 1 USB drive")

p=int()
q=int()
keyboards=list()
drives=list()
b = int(input("Enter the budget : "))
n = int(input("Enter number of keyboard models : "))
m = int(input("Enter number of drive models : "))
print("Enter the price of each keyboard model : ")
for x in range(n):
    p=int(input())
    keyboards.append(p)
print("Enter the price of each drive model : ")
for y in range(m):
    q=int(input())
    drives.append(q)
getMoneySpent(keyboards, drives, b)