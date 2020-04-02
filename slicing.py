print("1st list")
lst=[2,566,4,7,73,44,23]
new_lst=[]
for i in range(2,5):
    new_lst.append(lst[i])
print(new_lst)
print(lst[2:5])

print("2nd list")
lst1=[2,3,4,5]
lst2=lst1
print(lst1)  
lst2.append(20)
print(lst1)  #here lst will be same as lst 2 although we didn't append 20 with lst.the reason is in this case reference(address) is copying
print(lst2)

print("3rd list")
#to reverse slicing
lst3=[2,3,4,5]
lst4=lst3[3::-1]
print(lst3)  
lst4.append(20)
print(lst3)  #here lst will be same as lst 2 although we didn't append 20 with lst.the reason is in this case reference(address) is copying
print(lst4)