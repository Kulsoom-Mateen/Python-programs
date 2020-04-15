def split_and_join(line):
    # write your code here
    a=line.split(" ")
    z="-".join(a)
    return z

line = "My name is Kulsoom Mateen"
result = split_and_join(line)
print(result)