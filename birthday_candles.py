def birthdayCakeCandles(ar):
    maximum=max(ar)
    count=0
    for i in ar:
        if i == maximum:
            count=count+1
    return count

ar = [4,3,4,3,1]
result = birthdayCakeCandles(ar)
print(result)
