def diagonalDifference(arr):
    # Write your code here 
    sumltr = 0
    sumrtl = 0 
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                sumltr=sumltr+arr[i][j]
    l=len(arr)-1
    for k in range(len(arr)):
        sumrtl=sumrtl+arr[k][l]
        l=l-1
    final=sumrtl-sumltr
    if(final<0):
        final=final*(-1)
    return final
    

arr=[[11,2,4],[4,5,6],[10,8,-12]]
result = diagonalDifference(arr)
print(result)

