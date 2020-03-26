type=int(input("Enter 1 for fiction books and 2 for non-fiction books : "))
if(type==1):
    print("Science , Comedy , Fantasy , Comic or Historical")
    genre=input("Enter the genre of book you want : ")
    if(genre=='Science'):
        print("Shelf : C")
    elif(genre=='Fantasy'):
        print("Shelf : D")
    elif(genre=='Comic'):
        print("Shelf : B")
    elif(genre=='Comedy'):
        print("Shelf : A")
    elif(genre=='Historical'):
        print("Shelf : E")
    else:
        print("Book not present")
elif(type==2):
    print("History , Arts , Science and technology or Other")
    genre=input("Enter the genre of book you want : ")
    if(genre=='Science and technology'):
        print("Shelf : H")
    elif(genre=='History'):
        print("Shelf : F")
    elif(genre=='Arts'):
        print("Shelf : G")
    elif(genre=='Other'):
        print("Shelf : I")
    else:
        print("Book not present") 
