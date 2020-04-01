# entities are those physical things which has attributes and behaviours
# class define templates 
# function is behaviour
# there can't be behaviour inside function   
# entities that has attributes and behaviours are called classes
#Class functions that are behaviour are called methods
# positional arguments are before keyword arguments
# aese functions js ka phla argument self ho wo us k behaviours(methods) khlate hain

class Human():
    def __init__(self,favourite_dish="",name="James"):    #__init__ call automatically called by interpreter when its object is created(like constructor)
        self.name=name
        self.favourite_dish=favourite_dish
        print("I am constructor")
    def set_favourite_dish(self,favourite_dish):
        self.favourite_dish=favourite_dish
h1=Human()
h2=Human("Pizza")
h3=Human()
h4=Human()
print(h1.name)
print(h2.name)
print(h2.favourite_dish)
h2.set_favourite_dish("Biryani")
print(h2.favourite_dish)

#Functions in class are called methods
class student():
    def __init__(self,name,age,rollno,gender):
        self.name=name    #self.name is class's variable shown bt self
        self.age=age
        self.rollno=rollno
        self.gender=gender
    def print_details(self):
        print("Name: ",self.name,"Age: ",self.age,"Roll no.: ",self.rollno,"Gender: ",self.gender)
#student1 is object and it inherits all properties of student class
student1=student("Johny\t\t",20,5,"Female")
student1.print_details()
student1.name="Harry Potter\t"
student1.print_details()


class shape():
    def __init__(self,sides,color):
        self.sides=sides
        self.color=color
    def show_sides(self):
        print("The sides are : ",self.sides)
    def show_color(self):
        print("The color is ",self.color)
triangle=shape(3,"red")
triangle.show_color()
triangle.show_sides()