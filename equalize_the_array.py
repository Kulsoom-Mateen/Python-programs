def equalizeArray(arr):
    count=0
    count1=0
    n=0
    d=0
    for i in range(len(arr)):
        count1=0
        for j in range(len(arr)):
            if(arr[j]==arr[i]):
                count1=count1+1
        if(count1>count):
            n = arr[i]
            count=count1
    for x in range(len(arr)):
        if(arr[x]!=n):
            d = d + 1
    return d
    
n = int(input("Enter number of elements in an array : "))
arr = []
b = 0
print("Enter elements of an array : ")
for i in range(n):
    b = int(input())
    arr.append(b)
result = equalizeArray(arr)
print(result,"minimum deletions should take place to equalize the array")
