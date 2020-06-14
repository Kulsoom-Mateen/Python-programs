if 10>5:
    print("10 is greater than 5")
elif 10<5:
    print("10 is less than 5")
else:
    print("HH")

#Short hand if else

if 5<10: print("5 is less than 10")
a = 2
b = 330
print("A") if a > b else print("B")

c = 331
d = 330
print("C") if c > d else print("=") if c == d else print("D")

e = 200
f = 33
g = 500
if e > f and g > e:
    print("Both conditions are True")

h = 200
i = 33
j = 500
if h > i or h > j:
    print("At least one of the conditions is True")

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

k = 33
l = 200
if l > k:
    pass

print("Finish!!")