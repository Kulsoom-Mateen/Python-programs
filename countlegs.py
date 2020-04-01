def count_legs(chicken,cow,pig):
    chicken_leg=chicken*2
    cow_leg=cow*4
    pig_leg=pig*4
    total=chicken_leg+cow_leg+pig_leg
    return total
chicken_no=int(input("Enter number of chickens : "))
cow_no=int(input("Enter number of cows : "))
pig_no=int(input("Enter number of pigs : "))
print(count_legs(chicken_no,cow_no,pig_no))