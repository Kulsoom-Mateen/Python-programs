#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    for i in range(1000000000):
        x1=x1+v1
        x2=x2+v2
        if(x1==x2):
            s="YES"
            print("Both kangaroos will meet at point : ",x1)
            return s

        else:
            s="NO"
        
        if(x1>=100000000 or x2>=100000000):
            return s

x1 = 0
v1 = 3
x2 = 4
v2 = 2
result = kangaroo(x1, v1, x2, v2)
print(result," both the kangaroos can meet at a single point")
