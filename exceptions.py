class Calculator:
    def power(self,n,p):
        self.n=n
        self.p=p
        if(n<0 or p<0):
            raise Exception("n and p should be non-negative")
        return n**p
myCalculator=Calculator()
n=int(input("Enter base : "))
p=int(input("Enter power : "))
try:
    ans=myCalculator.power(n,p)
    print(ans)
except Exception as e:
    print(e)   