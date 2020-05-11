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
t = "helloworld"
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
print(q.find("l"))
a = "Hello I am {name}"
print(a.format(name = "Kulsoom"))
print(a.index("I"))
print(r.isalnum())
b = "HELLO12"
print(b.isalnum())
print(t.isalpha())
c = "45"
print(c.isdecimal())
print(c.isdigit())
d = "3Demo"
print(d.isidentifier())
print(q.islower())
