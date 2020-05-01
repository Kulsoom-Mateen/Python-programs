class AdvancedArithmetic(object):
    def divisorSum(self,n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum=0
        for i in range(1,n+1):
            if(n%i==0):
                print(i,end="  ")
                sum=sum+i
        print("")
        return sum

n = int(input("Enter a number : "))
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)