#nested loop uses where we have to work on sme population and also work on that population

import random
student_ages=[]
for i in range(10):
    student_ages.append(random.randint(10,65))
print(student_ages)
print("\t\tSorted list")
for j in range(0,len(student_ages)):
    for i in range(j+1,len(student_ages)):
        if student_ages[j]>student_ages[i]:
            temp=student_ages[j]
            student_ages[j]=student_ages[i]
            student_ages[i]=temp
print(student_ages)