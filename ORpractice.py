#to comment out all lines : select all line and press CTRL/
# print("Hello")
# print("OR practice file")
user_input=input("Enter day :")
if (user_input=="Saturday" or user_input=="saturday" or user_input=="SATURDAY" or 
   user_input=="Sunday" or user_input=="sunday" or user_input=="SUNDAY"):
    print("Today is off")
elif (user_input=="Monday" or user_input=="monday" or user_input=="MONDAY" or user_input=="Tuesday" or user_input=="tuesday" 
     or user_input=="TUESDAY" or user_input=="Wednesday" or user_input=="wednesday" or user_input=="WEDNESDAY" or user_input=="Thursday"
     or user_input=="thursday" or user_input=="THURSDAY" or user_input=="Friday" or user_input=="friday" or user_input=="FRIDAY"):
    print("You have to work..")
else:
    print("Wrong input")