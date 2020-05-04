def utopianTree(n):
    height=1
    for i in range(1,n+1):
        if(i%2!=0):
            height=height*2
        else:
            height=height+1
        # print(height)
    return height

n = int(input("Enter the number of growth cycyles : "))
result = utopianTree(n)
print("At the end of",n,"cycles, the tree height will be :",result,"meters")
