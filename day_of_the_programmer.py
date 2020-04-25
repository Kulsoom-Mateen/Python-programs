def dayOfProgrammer(year):
    l = [31,29,31,30,31,30,31,31]
    a=0
    final=256
    if(year==1918):
        l[1]=16
        if(year%400==0 or (year%4==0 and year%100!=0)):
            for i in range(len(l)):
                a=a+l[i]
            final = final - a 
            print(final)
        else:
            for i in range(len(l)):
                a=a+l[i]
            final = final - a + 1 
    elif(year>=1700 and year<=1917):
        if(year%4==0):
            for i in range(len(l)):
                a=a+l[i]
            final = final - a 
        # print(final)
        else:
            for i in range(len(l)):
                a=a+l[i]
            final = final - a + 1
    elif(year>=1919 and year<=2700): 
        if(year%400==0 or (year%4==0 and year%100!=0)):
            for i in range(len(l)):
                a=a+l[i]
            final = final - a 
            print(final)
        else:
            for i in range(len(l)):
                a=a+l[i]
            final = final - a + 1 
    return str(final)+".09."+str(year)

year = int(input("Enter a year : "))
result = dayOfProgrammer(year)
print(result)