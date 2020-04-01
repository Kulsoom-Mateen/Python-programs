# #single asterik(*) stores in tuple and double asterik will store in dictionary(and give both key and value)
def pizza(crust,*topping,size):    # * is for unknown number of arguments  
    print("You have ordered a pizza with ",crust," crust , size : ",size ," and the following toppings : ")
    for each in topping:
        print(each)
pizza("Thick","Green olives","Black olives","Chicken",size="13") #thick will store in crust and remaining in topping


def pizza1(crust,**topping):
    print("You have ordered a pizza with ",crust," crust and following toppings : ")
    for key,value in topping.items():
        print(key,":", value)
pizza1("Thick" , topping1="Green olives" , topping2="Black olives" , topping3="Chicken")
#it will store like this   topping={topping1="Green olives",toping2="Black olives",topping3="Chicken"}

def pizza2(crust,**topping):
    print("You have ordered a pizza with ",crust," crust and following toppings : ")
    for value in topping.values():
        print(value)
pizza2("Thick" , topping1="Green olives" , topping2="Black olives" , topping3="Chicken")

def pizza3(crust,**topping):
    print("You have ordered a pizza with ",crust," crust and following toppings : ")
    for key in topping.keys():
        print(key)
pizza3("Thick" , topping1="Green olives" , topping2="Black olives" , topping3="Chicken")