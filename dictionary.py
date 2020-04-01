#student=['James',123456789,'ABC','Jones']

# dictionary is represented by curly brackets , every value should be comma separated
student={          #Name,Cell no etc are keys
    'Name': 'James',
    'Cell Number': 123456789,
    #'Cell no.':[123,456]     here cell no is list inside a dictionary bcz some students can have more than 1 cell no.
    'Area':'ABC',
    'Children':[{'CName':'abc','Age':3,'Address':'xyz'},{'CName':'abc','Age':3,'Address':'xyz'}],    #dictionary inside a dictionary
    'Fathers Name':'Jones'
}


print("Printing keysa and values both")
print(student['Children'][1]['CName'])
for k in student:
    print(k,student[k])        #when we traverse on dictionary ,we get keys


print("Printing only values")
for v in student.values():    # this is second method t get values of dictionary
    print(v)    

print('Name' in student)    #returns true if this key(name) is present in dictionary    
print('Name1' in student) 


print(student['Name'])       #print Name key value of student dictionary
student['Name']='James Jack'         
print(student['Name'])
student['Module']='Module1'   # add one more key/value in dictionary
print(student)
del student['Area']          #delete area key
print(student)
print(student.pop('Cell Number'))    #pop key Cell Number
print(student)

students=[]
for i in range(2):   #take input for 2 students
    student1={}
    student1['Name']=input('Enter student name: ')
    student1['Father name']=input('Enter father name : ')
    student1['Cell no.']=input('Enter cell no. : ')
    students.append(student1)
print("Currently enrolled students : ",len(students))
for student1 in students:
    print("student")
    print(student1)
    if student1['Name'].lower()=='jimmy':
        print('Yes Jimmy is our student')
