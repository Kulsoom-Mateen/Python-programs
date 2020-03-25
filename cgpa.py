user_input=float(input("Enter your CGPA : "))
if user_input<4.0 and user_input>=3.7:
    print("Your grade is A+ and your cgpa is " + str(user_input))
elif user_input<3.7 and user_input>=3.5:
    print("Your grade is A and your cgpa is " + str(user_input))
elif user_input<3.5 and user_input>=3.0:
    print("Your grade is B and your cgpa is " + str(user_input))
elif user_input<3.0 and user_input>=2.5:
    print("Your grade is C and your cgpa is " + str(user_input))
else:
    print("You are fail")