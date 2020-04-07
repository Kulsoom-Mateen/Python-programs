def countApplesAndOranges(s, t, a, b, apples, oranges):
    k=0
    l=0
    for i in range (0,len(apples)):
        if( (a+apples[i])>=s and (a+apples[i])<=t):
            k=k+1
    print(k)
    for j in range (0,len(oranges)):
        if( (b+oranges[j])>=s and (b+oranges[j])<=t):
            l=l+1
    print(l)

s = int(input("Enter starting point of Sam's house location : "))
t = int(input("Enter ending point of Sam's house location : "))
a = int(input("Enter location of apple tree : "))
b = int(input("Enter location of orange tree : "))
m = int(input("Enter number of apples on apple tree : "))
n = int(input("Enter number of oranges on orange tree : "))

apples=[]
oranges=[]

for i in range(m):
    a=int(input("Enter units distance from a where each apple falls : "))
    apples1=[]
    apples1=apples.append(a)
globals(apples)['apples']=apples1
for j in range(n):
    b=int(input("Enter units distance from b where each orange falls : "))
    oranges1=[]
    oranges1=oranges.append(b)
globals(oranges)['oranges']=oranges1
print("Apple tree is located at a = ",a)
print("Orange tree is located at b = ",b)
countApplesAndOranges(s, t, a, b, apples, oranges)

