actual_return = input("Enter actual returned date : ")
actual_return = list(map(int, actual_return.split()))
expected_return = input("Enter expected return date : ")
expected_return = list(map(int, expected_return.split()))
# print(actual_return)
# print(expected_return)
a=actual_return[0]-expected_return[0]
b=actual_return[1]-expected_return[1]
c=actual_return[2]-expected_return[2]
if(a<=0 and b<=0 and c<=0):
    print("Fine = 0")
elif(a>0 and b>0 and c<0):
    print("fine = 0")
elif(a>0 and b==0 and c==0):
    print("Fine =",a*15)
elif(b>0 and c==0):
    print("Fine =",b*500)
elif(c>0):
    print("Fine = 10000")