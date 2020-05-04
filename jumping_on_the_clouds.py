#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e=100
    energy=0
    i=0
    while(i!=len(c)):
        if(c[i]==1):
            energy=e-3
            e=energy
        else:
            energy=e-1
            e=energy
        i+=k
    return energy

n = int(input("Enter number of clouds : "))
k = int(input("Enter jump distance : "))
b=0
c=list()
print("Enter 1 for thunder cloud and 0 for cumulus cloud : ")
for x in range(n):
    b=int(input())
    c.append(b)
result = jumpingOnClouds(c, k)
print("The remaining energy level is :",result)
