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
if "A" in d1:
    print("Yes")
print(len(d1))
d1["D"]="Doll"
print(d1)
d1.pop("D")
print(d1)
d1["D"]="doll"
d1["E"]="Egg"
print(d1)
del d1["B"]
print(d1)