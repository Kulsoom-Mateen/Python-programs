#!/bin/python3

import os
import sys

def timeConversion(s):
    a=list()
    b=""
    a=s.split(":")
    a1=a[2].split(s[7])

    if a[0]=='12' and a[1]=='00' and a[2]=='00AM' :
        b='00:00:00'

    elif a[0]=='12' and a[1]=='00' and a[2]=='00PM' :
        b='12:00:00'
    
    elif int(a[0])<12 and a1[1]=='PM':
        b=(str(int(a[0])+12)+':'+a[1]+":"+a[2][0:2])

    elif int(a[0])<12  or a[1]!='00' or a[2][0:2]!='00' and a1[1]=='AM':
        if(a[0]=='10' or a[0]=='11'):
            b=(str(int(a[0]))+':'+a[1]+":"+a[2][0:2])
        else:
            b=('0'+str(int(a[0]))+':'+a[1]+":"+a[2][0:2])
    
    elif a[0]=='12' and a[1]!='00' and a[2][0:2]!='00' and a1[1]=='AM':
        b=(str(int(a[0])-12)+'0'+':'+a[1]+":"+a[2][0:2])

    elif a[0]=='12' and a[1]!='00' and a[2][0:2]!='00' and a1[1]=='PM':
        b=(str(int(a[0]))+':'+a[1]+":"+a[2][0:2])

    elif a[0]=='12' and a[1]!='00' and a[2][0:2]!='00' and a1[2]=='AM':
        b=(str(int(a[0])-12)+'0'+':'+a[1]+":"+a[2][0:2])

    elif a[0]=='12' and a[1]!='00' and a[2][0:2]!='00' and a1[1]=='AM':
        b=(str(int(a[0]))+'0'+':'+a[1]+":"+a[2][0:2])

    return b
   
s = input("Enter time in 12 hour format i.e. 11:34:05AM  : ")

result = timeConversion(s)
print(result)
