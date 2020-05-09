s = "   My name is Kulsoom Mateen   "
print(len(s))
print(s.strip())
print(s.lower())
print(s.upper())
print(s.replace('My name is','I am'))
print(s.split(' '))
x = 'name' in s
print(x)
age = 20
txt = s+'and I am {}'
print(txt.format(age))