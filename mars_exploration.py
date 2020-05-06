def marsExploration(s):
    # a=list()
    count=0
    for i in range(0,len(s),3):
        a=list()
        for j in range(i,i+3):
            a.append(s[j])
        print(a)
        if(a[0]=="S"):
            pass
        else:
            count=count+1
        if(a[1]=="O"):
            pass
        else:
            count=count+1
        if(a[2]=="S"):
            pass
        else:
            count=count+1
        
    return count

s = input("Enter a received signal : ")
result = marsExploration(s)
print(result,"characters has been changed")
