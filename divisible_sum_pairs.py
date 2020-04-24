def divisibleSumPairs(n, k, ar):
    count=0
    print(ar)
    for i in range(n):
        for j in range(n):
            if(i<j):
                if((ar[i]+ar[j])%k==0):
                    count=count+1
    return count

n = int(input("Enter number of elements in an array : "))
k = int(input("Enter the number whose sum you want to find : "))
b = int()
ar=list()
print("Enter the elements of an array : ")
for a in range(n):
    b=int(input())
    ar.append(b) 

result = divisibleSumPairs(n, k, ar)
print(result)