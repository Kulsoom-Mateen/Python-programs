def beautifulDays(i, j, k):
    z=str()
    count=0
    for x in range(i,j+1):
        a=list()
        y=str(x)
        for m in range(len(y)):
            a.append(y[m])
        a.reverse()
        # print(a)
        z="".join(a)
        z=int(z)
        # print(x,z)
        l=x-z
        if(l<0):
            l=l*(-1)
        # print(l)
        if(l%k==0):
            count=count+1
    return count

i = int(input("Enter the starting day number : "))
j = int(input("Enter the ending day number : "))
k = int(input("Enter the divisor : "))
result = beautifulDays(i, j, k)
print("In the given interval,",result,"days are beautiful")
