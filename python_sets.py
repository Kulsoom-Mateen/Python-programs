s = {"apple","apple","banana","cherry"}
print(s)
for i in s:
    print(i)
if "banana" in s:
    print('Yes')
print("apple" in s)
s.add("mango")   #add single item
print(s)
s.update(["grapes","orange","watermelon"])
print(s)
print(len(s))
s.remove("banana")
print(s)
s.discard("apple")
print(s)
a = s.pop()
print(a)
print(s)
s1 = {"1","2","3"}
s2 = s1.union(s)
print(s2)
s.update(s1)
print(s)
s3 = set(("a","b","c"))
print(s3)
print(type(s3))
s1.add("4")
print(s1)
s4=s1.copy()
print(s4)
s4.add("5")
print(s4)
z = s4.difference(s1)
print(z)
x = s1.intersection(s4)
print(x)