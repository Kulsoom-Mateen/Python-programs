num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
operand = input("Enter Operator : ")
if operand == "+":
    result = num1 + num2
    print(result)
elif operand == "-":
    result = num1 - num2
    print(result)
elif operand == "*":
    result = num1 * num2
    print(result)
elif operand == "/":
    result = num1 / num2
    print(result)
else:
    print("Invalid operator")

# num1=int(input("Enter 1st number: "))
# num2=int(input("Enter 2nd number : "))
# opr=input("Enter operand : ")
# if opr=="+":
#     print(str(num1) + " + " + str(num2) + " = " + str(num1+num2))
# elif opr=="-":
#     print(str(num1) + " - " + str(num2) + " = " + str(num1-num2))
# elif opr=="*":
#     print(str(num1) + " * " + str(num2) + " =  " + str(num1*num2))
# elif opr=="/":
#     print(str(num1) + " / " + str(num2) + " = " + str(num1/num2))
# else:
#     print("Invalid operator")

    