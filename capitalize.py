def solve(s):
    l=list(s)
    for i in range(len(l)):
        if(l[i]==" "):
            l[0]=l[0].upper()
            l[i+1]=l[i+1].upper()
    z="".join(l)
    return z

s = "my name is kulsoom mateen"
result = solve(s)
print(result)
