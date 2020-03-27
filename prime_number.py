
##########FIRST METHOD#######################

num=int(input("Enter a number : "))
if num==0 or num==1:
    print(num," is not prime")
elif num==2:
    print(num ," is prime")
else:
    for i in range(2,num):
        if num%i==0:
            print(num," is not prime")
            break
        elif i==num-1:
            print(num, " is prime")

##########SECOND METHOD#######################


# With flag
# num=int(input("Enter number : "))
# if num==1 or num<=0:
#     print(num," is not prime") 
# elif num==2:
#     print(num," is prime")
# else:
#     is_prime=True 
#     for i in range(2,num):
#         #print(i)
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:   
#         print(num , " is prime")
#     else:
#         print(num, " is not prime")


##########THIRD METHOD#######################

# without flag
# num=int(input("Enter number : "))
# if num==1 or num<=0:
#     print(num," is not prime") 
# elif num==2:
#     print(num," is prime")
# else:
#     iter=2   #iter is variable
#     for i in range(2,num):
#         iter+=1
#         if num%i==0:
#             break
#     if iter==num:
#         print(num, " is prime")
#     else:
#         print(num," is not prime")



##########FOURTH METHOD#######################

# num=int(input("Enter a number : "))
# if num==0 or num==1 or num<0:
#     print(num," is not prime")
# elif num==2:
#     print(num, " is prime")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print(num , " is not prime")
#             break
# if i==(num-1):
#     print(num , " is prime")




##########FIFTH METHOD#######################

# num1=int(input("Enter a number : "))
# if num1==0 or num1==1 or num1<0:
#     print(num1, " is not prime")
# elif num1==2:
#     print(num1, " is prime")
# else:
#     flag1=True
#     for i in range(2,num1):
#         if(num1%i==0):
#             flag1=False
#             break
#     if flag1:
#         print(num1," is prime")
#     else:
#         print(num1," is not prime")