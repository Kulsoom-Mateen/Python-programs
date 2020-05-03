#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    l = (s - 1 + m) % n
    # Cannot be 0, this is 1-base
    # Could go with another modulo difference
    if l == 0:
        l = n
    return l

n = int(input("Enter number of prisoners : "))
m = int(input("Enter number of sweets : "))
s = int(input("Enter the seat number from which distribution of treat starts : "))
result = saveThePrisoner(n, m, s)
print("Warn prisoner",result,"about awful candy")
