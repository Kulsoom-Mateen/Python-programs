def minority_vote(vote1):
    counter=0
    most=0
    for i in vote1:
        count1=vote1.count(i)
        if(count1>counter):
            counter=count1
            most=i
    print("Maximum votes are for : " ,most)
    print("Number of votes for ",most," is / are : ",counter)
vote=["A","C","A","Z","Z","D","Z","Z","D","C","C"]
minority_vote(vote)