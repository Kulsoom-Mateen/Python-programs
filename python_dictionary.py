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
d2 = d1.copy()
print(d2)
d3 = dict(d1)
print(d3)

####Nested dictionary
family = {
    "child1" : {
        "name" : "Ali",
        "age" : "10"
    },
    "child2" : {
        "name" : "Amna",
        "age" : "7"
    },
    "child3" : {
        "name" : "Ahmed",
        "age" : "3"
    }
}
print(family)
print(family["child1"])
print(family["child2"]["name"])

child1 = {
        "name" : "Ali",
        "age" : "10"
}
child2 = {
        "name" : "Amna",
        "age" : "7"
}
child3 = {
        "name" : "Ahmed",
        "age" : "3"
    }
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)
print(myfamily["child3"])
print(myfamily["child3"]["age"])

d4 = dict(name="ABC",age="10")
print(d4)

x = d4.values()
print(x)

y = ("Apple","Mango","Banana")
z = 1
d5 = dict.fromkeys(y,z)
print(d5)
d5.update({"Pineapple":"2"})
print(d5)