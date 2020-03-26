# def is_leap(year):
#     leap = False
#     if(year%4==0):
#         leap=True
#         if(year%100==0):
#             leap=False
#             if(year%400==0):
#                 leap=True
#     return leap
# year = int(input("Enter year:"))
# print(is_leap(year))

#both are right

def is_leap(year):
    if((year % 4==0) or ((year % 100==0) and (year % 400==0))):
        leap="Its a leap year"
    else:
        leap="It is not a leap year"
    return leap
year = int(input("Enter year : "))
print(is_leap(year))