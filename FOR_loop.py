import random
lst=[]
for i in range(2,20):
    lst.append(random.randint(1,1000))
for i in lst:
    print(i)     #this will print all numbers which are in list but not in list form
print(lst)        #this will print all numbers which are in list in list form i.e [ , , , ...]
print(len(lst))