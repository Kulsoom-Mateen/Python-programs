def plusMinus(arr):
    minus=0
    plus=0
    zero=0
    for i in arr:
        if i < 0:
            minus=minus+1
        elif i > 0:
            plus=plus+1
        else:
            zero=zero+1
    plus=plus/len(arr)
    minus=minus/len(arr)
    zero=zero/len(arr)
    print(format('%f'%plus))
    print(format('%f'%minus))
    print(format('%f'%zero))

arr = [3,-5,4,-6,0,1]
plusMinus(arr)
