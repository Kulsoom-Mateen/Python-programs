def swapcase(s):
    a=""
    for i in range(len(s)):
        if s[i].isupper():
            a=a+s[i].lower()
        else:
            a=a+s[i].upper()
    return a
ss="Hello I am from Pakistan"
result=swapcase(ss)
print(result)