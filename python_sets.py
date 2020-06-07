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