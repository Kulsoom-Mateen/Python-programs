t = ("Orange","Mango","Banana","Grapes","Apple")
print(t)
print(t[2])
print(t[-3])
print(t[2:5])
print(t[-3:-1])
l = list(t)
l[2] = "Pomegranate"
t = tuple(l)
print(t)
for i in range(len(t)):
    print(t[i])
if("Mango" in t):
    print("Mango is present")
    print(len(t))
t1 = ("strawberry","Cherry")
t2 = t + t1
print(t2)
print(t.count("Grapes"))
print(t.index("Grapes"))