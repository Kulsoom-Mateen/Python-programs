def angryProfessor(k, a):
    ontime=0
    for i in range(len(a)):
        if(a[i]<=0):
            ontime=ontime+1
    if(ontime<k):
        print("YES, the class will cancel")
    else:
        print("NO, the class will not cancel")

n = int(input("Enter number of students : "))
k = int(input("Enter number of students that must be on time so that class won't cancel : "))
b=0
a=list()
print("Enter the arrival time for each student. Before time arrival should be negative, on time arrival should be 0 and late arrival must be positive")
for j in range(n):
    b=int(input())
    a.append(b)
result = angryProfessor(k, a)
