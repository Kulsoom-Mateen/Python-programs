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
t = "hello world"
print(t.capitalize())
print(t.casefold())
print(t.center(20))
print(t.count("l"))
r = "$%^72/  436skjashdf"
print(r.encode())
print(r.endswith("f"))
print(r.endswith("h"))
q = "H\te\tl\tl\to"
print(q.expandtabs(4))