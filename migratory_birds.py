def migratoryBirds(arr):
    bird_freq = [0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
        bird_freq[arr[i]] += 1
        print(bird_freq)
    return bird_freq.index(max(bird_freq))

arr_count = int(input("Enter number of birds sighted and reported : "))
print("Enter the type numbers of each bird sighted : ")
arr=list()
b=int()
for a in range(arr_count):
    b = int(input())
    arr.append(b)
result = migratoryBirds(arr)
print("The most common bird is : ",result)