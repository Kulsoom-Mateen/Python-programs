class Book():
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    # @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)

title=input("Enter title of book : ")
author=input("Enter name of book's author : ")
price=int(input("Enter price of book : "))
new_novel=MyBook(title,author,price)
new_novel.display()