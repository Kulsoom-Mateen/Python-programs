def mutate_string(string, position, character):
    st=list(string)
    st[position]=character
    string=''.join(st)
    return string

s = "abracadabra"
i = 5
c = "k"
s_new = mutate_string(s, int(i), c)
print(s_new)