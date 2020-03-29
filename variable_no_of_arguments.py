def add(num1,num2,*numbers):
    total=num1+num2
    for num in numbers:
        total+=num
    return total
print(add(6,8,9))

#there can be no positional argument after keyword argument
# print(add(num1=8