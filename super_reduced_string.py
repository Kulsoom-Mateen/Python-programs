def superReducedString(s):
    if not s:
        return "Empty String"
    for i in range(0,len(s)):
        if i < len(s)-1:
            if s[i] == s[i+1]:
                return superReducedString(s[:i]+s[i+2:])
    return s

s = input("Enter a string : ")
result = superReducedString(s)
print("Reduced string is :",result)
