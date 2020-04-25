#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count=0
    ar.sort()
    ar.append("#")
    print(ar)
    i=0
    while i<n:
    # for i in range(n):
        if(ar[i]==ar[i+1]):
            count=count+1
            i=i+2
        else:
            i=i+1

    return count

b=int()
ar=list()
n = int(input("Enter the number of socks in the pile : "))
print("Enter the colour number of each sock : ")
for x in range(n):
    b=int(input())
    ar.append(b)
result = sockMerchant(n, ar)
print("Number of matching pair of socks : ",result)
