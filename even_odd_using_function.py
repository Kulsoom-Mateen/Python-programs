'''take an input from user, pass it in the argument and return whether it is even or odd'''
a=int(input("Enter number : "))
def check(t):
    if (t%2)==0:
        return("Number is even")
    elif (t%2)!=0:
        return("Number is odd")
    else:
        return("Wrong input")
output=check(a)
print(output)