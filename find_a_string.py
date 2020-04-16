def count_substring(string, sub_string):
    s=0
    for i in range(len(string)-len(sub_string)+1):
        y=0
        if(string[i]==sub_string[y]):
            y=y+1
            z=0
            for j in range(i,i+len(sub_string)):
                if(string[j]==sub_string[z]):
                    f=True
                else:
                    f=False
                    break
                z=z+1
            if(f==True):
                s=s+1
    return s

string = input("Enter a string : ")
sub_string = input("Enter the string you want to find : ")

count = count_substring(string, sub_string)
print("Number of occurence(s) of ", sub_string , " in " , string , " is : " ,count)