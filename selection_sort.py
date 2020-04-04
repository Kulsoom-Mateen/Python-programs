def sort(list):
    for i in range(len(list)-1):
        minpos=i
        for j in range(i+1,len(list)):
            if(list[j]<list[minpos]):
                minpos=j
        temp=list[minpos]
        list[minpos]=list[i]
        list[i]=temp


list=[5,3,8,366,37,722,546,124,678,2,4,3,5]
print("List : ",list)
sort(list)
print("Sorted list : ",list)