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

# for i in range(m):
#     a=int(input("Enter units distance from a where each apple falls : "))
#     apples=apples.append(a)
# for j in range(n):
#     b=int(input("Enter units distance from b where each orange falls : "))
#     oranges=oranges.append(b)
# print("Apple tree is located at a = ",a)
# print("Orange tree is located at b = ",b)
# countApplesAndOranges(s, t, a, b, apples, oranges)
apples=[2,3,-4]
oranges=[3,-2,-4]

for i in range(len(apples)):
    apples[i]=apples[i]+a
print(apples)

for j in range(len(oranges)):
    oranges[j]=oranges[j]+b
print(oranges)

apple_count=0
for x in range(len(apples)):
    if apples[x]>=s and apples[x]<=t :
        apple_count=apple_count+1

orange_count=0
for y in range(len(oranges)):
    if oranges[y]>=s and oranges[y]<=t :
        orange_count=apple_count+1

print(apple_count," apple(s) and ",orange_count," orange(s) land in inclusive range of ",s,"-",t)
