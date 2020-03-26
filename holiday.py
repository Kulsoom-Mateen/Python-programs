x=input("Enter a day :")
if(x=='Sunday' or x=='sunday' or x=='SUNDAY'):
    print("Its a holiday")
elif(x=='Monday' or x=='monday' or x=='MONDAY' or x=='Tuesday' or x=='tuesday' or x=='TUESDAY' or
    x=='Wednesday' or x=='wednesday' or x=='WEDNESDAY' or x=='Thursday' or x=='thursday' or x=='THURSDAY' or
    x=='Friday' or x=='friday' or x=='FRIDAY' or x=='Saturday' or x=='saturday' or x=='SATURDAY'):
    print("You have to go to work")
else:
    print("wrong input")



# days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# for day in days:
#     if day=="Sunday":
#         print("Its holiday")
#     else:
#         print("You have to go to work")
# element=days[2:4]
# print(element)
# a=days.pop()
# print(a)
# print(days)
