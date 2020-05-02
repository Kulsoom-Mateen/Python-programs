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

nk = input().split()

n = int(nk[0])

k = int(nk[1])

height = list(map(int, input().rstrip().split()))

result = hurdleRace(k, height)
print(result)
