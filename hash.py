integer_list = [1,2]
for i in range(len(integer_list)):
    t=tuple(integer_list)
print(hash(t))