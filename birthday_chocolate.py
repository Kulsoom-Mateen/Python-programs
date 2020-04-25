def birthday(s, d, m):
    count=0
    b=0
    c=0
    a=list()
    if(n==1 and m==1 and s[0]==d):
        count=1
        return count
    else:
        for i in range(len(s)-m+1):
            b=0
            a=list()
            c=i
            for j in range(m):
                a.append(s[c])
                c=c+1
            for x in range(len(a)):
                b=b+a[x]
            print(b)
            if(b==d):
                print(a)
                count=count+1
        return count

a=0
s=list()
n = int(input("Enter the number of squares in the chocolate : "))
print("Enter  the numbers on each of the squares of chocolate : ")
for z in range(n):
    a=int(input())
    s.append(a)

d= int(input("Enter Ron's birthday : "))
m= int(input("Enter Ron's birth month : "))
result = birthday(s, d, m)
print(result,"segment(s) meeting her criteria")
