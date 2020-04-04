# pos=-1
# def search(list,n):
#     i=0
#     while(i<len(list)):
#         if(list[i]==n):
#             globals()['pos']=i
#             return True
#         i=i+1
#     return False

# list=[1,3,54,23,75,24,13]
# m=75
# if search(list,m):   #calling search function
#     print("Element found at : ",pos)
# else:
#     print("Not found")
# n=1
# if search(list,n):   #calling search function
#     print("Element found at : ",pos)
# else:
#     print("Not found")

# o=231
# if search(list,o):   #calling search function
#     print("Element found at : ",pos)
# else:
#     print("Not found")

############################BY USING FOR LOOP#######################

pos=-1
def search(list,n):
    j=0
    for i in list:
        if(list[j]==n):
            globals()['pos']=j
            return True
        else:
            j=j+1
    return False
print("")
list=[1,3,54,23,75,24,13]
m=75
if search(list,m):   #calling search function
    print("Element found at : ",pos)
else:
    print("Not found")
n=1
if search(list,n):   #calling search function
    print("Element found at : ",pos)
else:
    print("Not found")

o=231
if search(list,o):   #calling search function
    print("Element found at : ",pos)
else:
    print("Not found")