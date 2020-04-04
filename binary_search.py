pos=-1
def search(list,n):
    lb=0
    ub=len(list)-1
    while(lb<=ub):
        mid=(lb+ub)//2
        if(list[mid]==n):
            globals()['pos']=mid
            return True
        else:
            if(list[mid]<n):
                lb=mid+1
            else:
                ub=mid-1
    return False

list=[132,243,6,32,6,3,4243,5,23,5,233,5,3,52,3,532]
list.sort()
print("Sorted list : ",list)
n=233
if search(list,n):
    print(n,"Found at : ",pos)
else:
    print("Not found")
