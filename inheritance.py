class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName,lastName,idNumber,scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNumber
        self.scores=scores
    def calculate(self):
        a=0
        for i in self.scores:
            a=a+i
        a=int(a/len(scores))
        print(a)
        if(a>=90 and a<=100):
            return "O"
        elif(a>=80 and a<90):
            return "E"
        elif(a>=70 and a<80):
            return "A"
        elif(a>=55 and a<70):
            return "P"
        elif(a>=40 and a<55):
            return "D"
        elif(a<40):
            return "T"

x=0
scores=list()
firstName = input("Enter first name : ")
lastName = input("Enter laste name : ")
idNum = int(input("Enter id number : "))
numScores = int(input("Enter number of subjects : "))
for z in range(numScores):
    x=int(input())
    scores.append(x)
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())