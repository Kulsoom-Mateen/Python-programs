# employee_list=['Hamdah','Kulsoom','Muniba','Anas','Monis','1.0',3,8.4]
# print(employee_list[0])
# print(employee_list)
# print("Employee name is : "+employee_list[0])
# print(employee_list[5])
# print("Employee grade is : "+employee_list[5])
# print("Employee grade is : "+str(employee_list[6])) #error bcz string doesn't concatinate with integer so use str 

# emp_det=['Kulsoom',19,'Karachi']
# print("Employee name is : "+emp_det[0]+"\nEmployee age is "+str(emp_det[1])+"\nEmployee city is : "+emp_det[2])
# emp_det.append('Pakistan') #append this value at last index of list
# print(emp_det)

# emp_det[2]='Lahore'  #Change/overwrite value at index 2 
# print(emp_det)

# #to insert and other indexes move forward
# emp_det.insert(1,'Mateen')
# print(emp_det)

# emp_det.pop() #last index value delete
# print(emp_det)

# del emp_det[2]   #to delete value from particular/specific index  / index wise deletion
# print(emp_det)

# emp_det.remove('Kulsoom')  #to delete particular/specific value
# print(emp_det)

list=["ABC" , "XYZ" , "EE-000" , 2020]
print("Name : ",list[0], "\nFtaher's Name : ",list[1],"\nRoll no : ",list[2],"\nYear : ",str(list[3]))
list.append("City")
print(list)
list.insert(2,"Undergraduate")
print(list)
list.remove(list[0])
print(list)
list.pop()
print(list)
del list[2]
print(list)