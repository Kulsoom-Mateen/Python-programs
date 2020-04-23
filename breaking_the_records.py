def breakingRecords(scores):
    minn= scores[0]
    min_count=0
    maxx = scores[0]
    max_count=0
    final = list()
    for i in range(1,len(scores)):
        if(scores[i]>maxx):
            maxx=scores[i]
            max_count=max_count+1
    for j in range(1,len(scores)):
        if(scores[j]<minn):
            minn=scores[j]
            min_count=min_count+1
    
    final.append(max_count)
    final.append(min_count)
    return final


n = int(input("Enter number of games in a season : "))
print("Enter score in each game")
scores=list()
for a in range(n):
    b=int(input())
    scores.append(b)
result = breakingRecords(scores)
print("Number of times gamer broke his/her most point records in a season : ",result[0])
print("Number of times gamer broke his/her least point records in a season : ",result[1])
