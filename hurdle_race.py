#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    a=0
    height=sorted(height)
    if(height[len(height)-1]>k):
        a=height[len(height)-1]-k
    return a

n = int(input("Enter number of hurdles : "))
k = int(input("Enter the maximum height an athlete can jump : "))
b=0
height=list()
print("Enter height of each hurdle : ")
for i in range(n):
    b=int(input())
    height.append(b)
result = hurdleRace(k, height)
print("An athelete must drink",result,"doses to be able to jump all hurdles")
