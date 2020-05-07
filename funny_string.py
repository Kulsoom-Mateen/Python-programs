import math
def funnyString(word):
    i = 0
    length = len(word)
    # arr = []
    # revarr = []
    for i in range(0,math.ceil(length/2)):
        sdiff = abs(ord(word[i])-ord(word[i+1]))
        rdiff = abs(ord(word[length-i-1])-ord(word[length-i-2]))
        if sdiff == rdiff:
               continue
        else:
               return "Not Funny"
    return "Funny"

s = input("Enter a string : ")
result = funnyString(s)
print(result,"String")
