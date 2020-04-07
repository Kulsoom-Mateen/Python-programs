def sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                temp=list[j+1]
                list[j+1]=list[j]
                list[j]=temp




list=[3,18,1611,41,213,132,7,2343,123,21]
sort(list)
print(list)
