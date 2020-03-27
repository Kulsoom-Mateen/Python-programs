def no_of_characters(string1,string2):
    if(len(string1)==len(string2)):
        return "Both strings are equal"
    else:
        return "Strings are unequal"
str1=input("Enter 1st string : ")
str2=input("Enter 2nd string : ")
print(no_of_characters(str1,str2))