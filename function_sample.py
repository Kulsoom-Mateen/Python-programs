# # t=takes    r=return    n=nothing      s=something   i.i tnrn=takes nothing returns nothing
def tnrs():
    a=2
    b=5
    return(a+b)
result=tnrs()
print("Takes nothing returns something")
print(result)

def tnrn():
    a=2
    b=5
    print("Takes nothing returns nothing")   
    print("Sum is : ",(a+b))
tnrn()


print("Takes something returns something")
a=int(input("enter number 1 : "))
b=int(input("enter number 2 : "))
def tsrs(val1,val2):
    result=val1+val2
    return result
output_of_function=tsrs(a,b)
print(output_of_function)

def tsrn(owner,pet):
    print("Takes nothing returns nothing")
    print(owner ," is an owner of ",pet)
tsrn("Cat","Sarah")
print("This output is wrong bcz output is swapped")