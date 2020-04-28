class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        a.sort()
        b=a[0]-a[len(a)-1]
        if(b>=0):
            self.maximumDifference=b
        elif(b<0):
            self.maximumDifference=b*(-1)

c=0
a=list()
n=int(input("Enter number of elements in a list : "))
print("Enter a list of ",n," elements :")
for i in range(n):
    c=int(input())
    a.append(c)
d = Difference(a)
d.computeDifference()

print("The maximum absolute difference is : ",d.maximumDifference)