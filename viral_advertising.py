import math
def viralAdvertising(n):
    shared=5
    liked=0
    cum=0
    print("Shared  Liked  Cummulative likes")
    for i in range(1,n+1):
        liked=math.floor(shared/2)
        cum=cum+liked
        shared=liked*3
        print(shared,"     ",liked,"       ",cum)  
    return cum

n = int(input("Enter number of days : "))
result = viralAdvertising(n)
print("The commulative number of likes are : ",result)
