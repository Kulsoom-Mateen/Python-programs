def is_leap(year):
    leap = False
    
    # Write your logic here
    #if((year % 4 == 0) or ((year%100!=0) and (year%400==0)) ):
    if(year%4==0):
        leap = True
        if(year%100==0):
            leap = False
            if(year%400 == 0):
                leap = True
    return leap

year = int(input("Enter a year : "))
print(is_leap(year))