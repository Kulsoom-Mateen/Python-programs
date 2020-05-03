def findDigits(n):
    s=str(n)
    count=0
    print("Given integer is broken into:")
    for j in range(len(s)):
        print(s[j],end=" ")
    print("\n Given integer is divisible by:")
    for i in range(len(s)):
        a=int(s[i])
        try:
            if(n%a==0):
                print(a,end=" ")
                count=count+1
        except:
            pass
    return count

n = int(input("Enter a digit : "))
result = findDigits(n)
print("\n Integer",n,"is divisible by",result,"numbers")

