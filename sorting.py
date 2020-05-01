n = int(input("Enter number of elements in a list : "))
a = list()
b = 0
print("Enter elements of a list : ")
for x in range(n):
    b = int(input())
    a.append(b)
numberOfSwaps = 0
for i in range(n):
    for j in range(n-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            numberOfSwaps=numberOfSwaps+1

    if(numberOfSwaps==0):
        break
print("Array is sorted in",numberOfSwaps ,"swaps.")
print("Sorted array : ",a)
print("First Element:",a[0])
print("Last Element:",a[len(a)-1])