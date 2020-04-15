#This python program prints True if input string has any alphanumeric character,
#alphabetic character, digit, lowercase and uppercase letter and print output for each validator in different lines.
s = input("Enter any string : ")
l=list(s)
for i in range(len(l)):
    if(l[i].isalnum()):
        print(True)
        break
else:
    print(False)
for i in range(len(l)):
    if(l[i].isalpha()):
        print(True)
        break
else:
    print(False)
for i in range(len(l)):
    if(l[i].isdigit()):
        print(True)
        break
else:
    print(False)
for i in range(len(l)):
    if(l[i].islower()):
        print(True)
        break
else:
    print(False)
for i in range(len(l)):
    if(l[i].isupper()):
        print(True)
        break
else:
    print(False)