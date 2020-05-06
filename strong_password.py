#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    count=0
    a=0
    for i in range(len(password)):
        if(password[i]=="0" or password[i]=="1" or password[i]=="2" or password[i]=="3" or password[i]=="4" or password[i]=="5" or
           password[i]=="6" or password[i]=="7" or password[i]=="8" or password[i]=="9"):
            break
    else:
        count=count+1
    # print(count)
    for i in range(len(password)):
        if(password[i].islower()):
            break
    else:
        count=count+1
    # print(count)
    for i in range(len(password)):
        if((password[i]).isupper()):
            break
    else:
        count=count+1
    # print(count)
    for i in range(len(password)):
        if(password[i]=="!" or password[i]=="@" or password[i]=="#" or password[i]=="$" or password[i]=="%" or 
            password[i]=="^" or password[i]=="&" or password[i]=="*" or password[i]=="(" or password[i]==")" or
            password[i]=="-" or password[i]=="+"):
            break
    else:
        count=count+1
    # print(count)
    if(len(password)<6):
        a=6-len(password)
        if(count<a):
            return a
        else:
            return count
    else:
        return count

n = int(input("Enter number of characters in password : "))
password = input("Enter password : ")
answer = minimumNumber(n, password)
print("Insert",answer,"more characters to make strong password")
