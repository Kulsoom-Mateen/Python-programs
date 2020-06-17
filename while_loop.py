a = 1
while a<=5:
    print("2*",a,"=",a*2)
    a = a + 1

b = 1
while b <= 5:
    print(b)
    if b==3:
        break
    b=b+1

c = 10
while c <= 15:
    c = c + 1
    if c==13:
        continue
    print(c)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")