def findMean(a, n):
    sum = 0
    for i in range( 0, n):
        sum += a[i]
    return float(sum/n)

def findMedian(a, n):
    a.sort()
    even = True
    if len(a)%2 == 1:
        even = False
    if even:
        slice_start = (len(a)//2) - 1
        slice_end   = (len(a)//2) + 1
        median      = sum(a[slice_start:slice_end]) / 2
    else:
        median      = a[len(a)//2]
    return float(median)

def findMode(a,n):
    sorted(a)
    numbers = dict()
    for item in a:
        if item not in numbers:
            numbers[item] = 1
        else:
            numbers[item] = numbers[item] + 1
    max_count = 0
    for key in numbers:
        if numbers[key] > max_count:
            max_count = numbers[key]
    max_modal_elements = []
    for key in numbers:
        if numbers[key] == max_count:
            max_modal_elements.append(key)
    mode = min(max_modal_elements)
    return float(mode)


n = int()
number = [45,23,76,34,9,3,6,23,23,7]
n=10
mean = findMean(number,n)
median = findMedian(number,n)
mode = findMode(number,n)

print("Mean: ",mean)
print("Median: ",median)
print("Mode : ",mode)
