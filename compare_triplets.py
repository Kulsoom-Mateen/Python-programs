def compareTriplets(a, b):
    alias=0
    bob=0
    for x in range(len(a)):
        if a[x]>b[x]:
            alias=alias+1
        elif a[x]<b[x]:
            bob=bob+1
        else:
            alias=alias
            bob=bob
    print("Alias won ",alias," match / matches")
    print("Bob won ",bob," match / matches")


a = [5,4,3,5]
b = [3,4,5,3]
compareTriplets(a, b)
