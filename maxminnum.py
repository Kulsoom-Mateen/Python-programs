list=[]
for i in range(0,10):
    num=int(input("Enter number "+ str(i+1) +" : "))
    list.append(num)
print(list)
max=list[1]
min=list[1]
indexmax=1
indexmin=1
for x in range(0,10):
    if max<list[x]:
        max=list[x]
        indexmax=x
print("Maximum no. is : ",max)
print("Index of maximum no. is : ",indexmax)
for x1 in range(0,10):
    if min>list[x1]:
        min=list[x1]
        indexmin=x1
print("Minimum no. is : ",min)
print("Index of minimum no. is : ",indexmin)
sum=0
for x2 in range(0,10):
        sum=sum+list[x2]
print("Sum of all elements of list : ",sum) #this program gives both max & min no. & its index in the list & sum of all elements of list