def is_prime(n):
    if n == 1:
        return False
    else:
        square_root = int(n**0.5)
        for i in range(2, square_root + 1):
            if ((n % i) == 0) and (i != n):
                return False
        return True

n = int(input("Enter a number : "))
if is_prime(n):
    print(n,"is prime")
else:
    print(n,"is not prime")