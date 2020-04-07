arr=[2,3,6,6,5]
a=sorted(arr)

runner=0
for i in range(len(a)-1,0,-1):
    if(a[i]==a[i-1]):
        runner=a[i-2]
    elif(a[i]!=a[i-1]):
        runner=a[i-1]
        break

print(runner)
