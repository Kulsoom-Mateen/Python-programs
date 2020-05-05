def extraLongFactorials(n):
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    print("Factorial of",n,"is",fact)

n = int(input("Enter a number : "))
extraLongFactorials(n)
