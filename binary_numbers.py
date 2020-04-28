n = int(input("Enter a decimal number : "))

a=list()
b=list()
i=0
count=0
while(i<n):
    a.append(n%2)
    n=int(n/2)
a.reverse()
a.append("#")
print("Binary equivalent of",n,"is :",end="")
for l in range(len(a)-1):
    print(a[l],end="")
print("")
for j in range(len(a)):
    if(a[j]==1 and a[j+1]==1):
        count=count+1
    else:
        b.append(count+1)
        count=0

b.sort()
b.reverse() 
print("Maximum number of consecutive 1's is/are : ",b[0])