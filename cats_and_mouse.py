#x,y,z are positions of cat A, cat B and mouse respectively
# if cat A reaches to the mouse first then print cat A
# if cat B reaches to the mouse first then print cat B 
#if both cats reaches to the mouse at same time then mouse will escape and we have to print mouse C
def catAndMouse(x, y, z):
    ans=()
    if(x<z and y<z):
        for i in range(x,z+1):
            for j in range(y,z+1):
                if(i==z and j==z):
                    ans="Mouse C"
                    break
                elif(i==z):
                    ans="Cat A"
                    break
                elif(j==z):
                    ans="Cat B"
                    break
                i=i+1
            break
    elif(x<z and y>z):
        for i in range(x,z+1):
            for j in range(y,z-1,-1):
                if(i==z and j==z):
                    ans="Mouse C"
                    break
                elif(i==z):
                    ans="Cat A"
                    break
                elif(j==z):
                    ans="Cat B"
                    break
                i=i+1
            break
    elif(x>z and y<z):
        for i in range(x,z-1,-1):
            for j in range(y,z+1):
                if(i==z and j==z):
                    ans="Mouse C"
                    break
                elif(i==z):
                    ans="Cat A"
                    break
                elif(j==z):
                    ans="Cat B"
                    break
                i=i-1
            break
    elif(x>z and y>z):
        for i in range(x,z-1,-1):
            for j in range(y,z-1,-1):
                if(i==z and j==z):
                    ans="Mouse C"
                    break
                elif(i==z):
                    ans="Cat A"
                    break
                elif(j==z):
                    ans="Cat B"
                    break
                i=i-1
            break
    elif(x==z and y==z):
        ans="Mouse C"
    elif(x==z and y!=z):
        ans="Cat A"
    elif(x!=z and y==z):
        ans="Cat B"
    return ans

q = int(input("Enter number of situations : "))

l=list()
for q_itr in range(q):
    x = int(input("Enter Cat A's position : "))
    y = int(input("Enter Cat B's position : "))
    z = int(input("Enter Mouse's position : "))
    print("Next situation")
    result = catAndMouse(x, y, z)
    l.append(str(result))

print(l)