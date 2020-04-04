def minority_vote(vote1):
    counter=len(vote1)
    least=0
    for i in vote1:
        count1=vote1.count(i)
        print(count1)
        if(counter>count1):
            counter=count1
            least=i
            # if(counter/len(vote1)>=0.5):
            #     least=vote1[count1+1]
            # else:
              
            #     least=False
    print("Minimum votes are for : ",least)
    print("Number of votes of ",least," is / are : ",counter)
vote=["A","A","A","E","B","B","C","A","B","C","C","E"]
minority_vote(vote)


