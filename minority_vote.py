def minority_vote(vote1):
    counter=0
    least=0
    for i in vote1:

        count1=vote1.count(i)
        if(count1>counter):
            counter=count1
            if(counter/len(vote1)>=0.5):
                least=vote1[count1+1]
            else:
              
                least=False
    print("Minimum votes are for : ",least)
    print("Number of votes of ",least," is / are : ",count1)
vote=["A","A","A","A","B","C","D","E"]
minority_vote(vote)