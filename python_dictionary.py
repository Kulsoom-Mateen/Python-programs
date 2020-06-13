d1 = {"A":"Apple","B":"Ball","C":"Cat"}
print(d1)
print(d1["A"])
print(d1.get("B"))
d1["B"]="Balloon"
print(d1)
for a in d1:
    print(a)
for a in d1:
    print(d1[a])
for a in d1.values():
    print(a)
for a in d1.keys():
    print(a)
for a,b in d1.items():
    print(a,":",b)