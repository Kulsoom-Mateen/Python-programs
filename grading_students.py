def gradingStudents(grades):
    # Write your code here
    grade1=[]
    for i in grades:
        j=((i/5)+1)*5
        print(j)
        if( i < 38):
            i = i
            grade1.append(i)
        elif( (j - i) < 3):
            i = j                                                 
            grade1.append(i)
        else:
            i = i 
            grade1.append(i)
    return grade1


grades = [73,67,38,33]
result = gradingStudents(grades)
print(result)
