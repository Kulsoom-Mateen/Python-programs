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

arr = [1,2,3,4]
res = reverseArray(arr)
print(res)