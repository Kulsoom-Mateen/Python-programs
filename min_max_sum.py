def miniMaxSum(arr):
    min_sum=0
    max_sum=0
    for i in range(0,len(arr)-1):
        min_sum=min_sum+arr[i]
    for j in range(len(arr)-1,0,-1):
        max_sum=max_sum+arr[j]
    print (min_sum,max_sum)


arr=[1,2,5,3,4]
miniMaxSum(sorted(arr))
