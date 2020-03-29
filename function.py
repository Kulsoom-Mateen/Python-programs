#2 types of function: built in function and user defined function
def greet():    #function definition
    print("Good morning")
greet()         #function calling/activation
print("I am outside the function")
greet()
print("Completed")


a=int(input("Enter number 1 :"))
b=int(input("Enter number 2 : "))
def add(num1,num2):    
    my_sum=num1+num2
    print(my_sum)
def sub(num1,num2):     
    my_sum=num1-num2
    print(my_sum)
def mul(num1,num2):     
    my_sum=num1*num2
    print(my_sum)
def div(num1,num2):     
    my_sum=num1/num2
    print(my_sum)    
add(a,b)  #passing data called arguments
sub(a,b)  #it is also called positional argument bcz  whatever we write at first position will receive by first argument
mul(a,b)
div(a,b)

print("\n")
def my_pet(owner,pet):
    print(owner ," is an owner of ",pet)
my_pet("John","Rabbit")            #positional arguments
my_pet("Sarah","Cat")
my_pet(pet="Dog",owner="Sarah")      #keyword arguments

def my_pet1(owner,pet,city):
    print(owner ," is an owner of ",pet," living in ",city)
my_pet1("John","Rabbit","Karachi")   #if here we don't write Karachi means any argument is missing then error occur

def my_pet2(owner,pet,city="Karachi"):
    print(owner ," is an owner of ",pet," living in ",city)
my_pet2("James","Dog") #here we doesn't give 3rd argument bcz it is by default Karachi but we can also give so Karachi will overwrite by that argument 