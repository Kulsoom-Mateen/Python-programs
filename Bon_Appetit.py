def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    a=0
    for i in range(len(bill)):
        a=a+bill[i]
    a=int(a/2)
    if(a==b):
        print("Anna paid correct amount")
    else:
        print("Brian should return ",b-a," rupees to Anna")

z=int()
bill=list()
n = int(input("Enter the number of items ordered : "))
k = int(input("Enter the zero-based index of the item Anna is allergic and doesn't eat : "))
print("Enter an array of integers representing the cost of each item ordered : ")
for x in range(n):
    z=int(input())
    bill.append(z)
b = int(input("Enter the amount of money that Anna contributed to the bill : "))
bonAppetit(bill, k, b)