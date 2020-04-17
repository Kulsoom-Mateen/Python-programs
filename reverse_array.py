#!/bin/python3

import math
import os
import random
import re
import sys

def reverseArray(a):
    s=list()
    b=0
    for i in range(len(a)-1,-1,-1):
        s.append(a[i])
        b=b+1
    return s

count = int(input("Enter the number of elements in a list : "))
arr = list()
print("Enter elements of a list : ")
for i in range(count):
    arr.append(int(input()))

res = reverseArray(arr)
print(res)