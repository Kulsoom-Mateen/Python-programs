lst = ["Volvo", "Honda", "Civic", "Toyota", "Suzuki"]
print(lst)
print(lst[2])
print(lst[-1])
print(lst[-3])
print(lst[1:3])
print(lst[:3])
print(lst[3:])
print(lst[-3:-1])
lst[2] = "Nissan"
print(lst)
for i in lst:
    print(i)
if("Nissan" in lst):
    print("Yes")
print(len(lst))
lst.append("Civic")
print(lst)
lst.insert(2,"Corolla")
print(lst)
lst.remove("Volvo")
print(lst)
lst.pop()
print(lst)
del lst[3]
print(lst)
lst1 = lst.copy()
print(lst1)
lst.clear()
print(lst)
lst2 = ["Hello" , "world"]
lst3 = lst1 + lst2
print(lst3)
for j in lst2:
    lst.append(j)
print(lst)
lst.extend(lst1)
print(lst)
lst.reverse()
print(lst)
lst.sort()
print(lst)
