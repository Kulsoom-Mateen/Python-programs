def countingValleys(n, s):
    count=0
    final=0
    a=list()
    for i in range(len(s)):
        if(s[i]=="U"):
            count=count+1
        elif(s[i]=="D"):
            count=count-1
        a.append(count)
    print(a)
    for j in range(0,len(a)-1,2):
        if(a[j]==0 and a[j+1]<0):
            final=final+1
        elif(a[j]<0 and a[j+1]>=0):
            final=final+1
    return final

n = int(input("Enter number of steps : "))
b = 0
s = list()
print("Enter up and down steps of a hiker : ")
for x in range(n):
    b = input()
    s.append(b)
result = countingValleys(n, s)
print("Number of valleys hiker passed is/are : ",result)
