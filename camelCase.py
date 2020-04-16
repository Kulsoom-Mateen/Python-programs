#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    l=list(s)
    count=1
    for i in l:
        if(i==i.upper()):
            count=count+1
    return count

s = "oneTwoThree"
result = camelcase(s)
print("Number of words in a given string is/are : ",result)
