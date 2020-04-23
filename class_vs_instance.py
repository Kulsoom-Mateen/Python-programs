class Person:
    def __init__(self,initialAge):
        if(initialAge>0):
            self.age = initialAge
        elif(initialAge<0):
            self.age = 0
            print("Age is not valid, setting age to 0.")
    def yearPasses(self):
        self.age=self.age+1
        return self.age

    def amIOld(self):
        if(self.age<13):
            print("Age = ",self.age," , You are young.")
        elif(self.age>=13 and self.age<18):
            print("Age = ",self.age," , You are a teenager.") 
        elif(self.age>=18):
            print("Age = ",self.age," , You are old.")

t = int(input("Enter number of people : "))
for i in range(0, t):
    age = int(input("Enter age of person "+str(i+1)+" : "))         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses() 
    print("After 3 years")      
    p.amIOld()
    print("")