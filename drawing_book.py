def pageCount(n, p):
    right=int(p/2)
    left=0
    for i in range(n,0,-2):
        if(n%2==0 and p==i-1):
            left=left+1
            break
        elif(i==p or i-1==p):
            break
        else:
            left=left+1
    if(right>left):
        print("Turn ",left," page(s) from back side")
    else:
        print("Turn ",right," page(s) from front side")

n = int(input("Enter number of pages in a book : "))
p = int(input("Enter page number you want to open : "))
pageCount(n, p)