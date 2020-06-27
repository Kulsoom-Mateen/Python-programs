def my_function():
  print("Hello from a function")

def my_function1(fname):
  print(fname + " Refsnes")

def my_function2(fname, lname):
  print(fname + " " + lname)

def my_function3(*kids):
  print("The youngest child is " + kids[2])

def my_function4(child3, child2, child1):
  print("The youngest child is " + child3)

def my_function5(**kid):
  print("His last name is " + kid["lname"])

def my_function6(country = "Norway"):
  print("I am from " + country)


my_function()

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

my_function2("Emil", "Refsnes")

my_function3("Emil", "Tobias", "Linus")

my_function4(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

my_function5(fname = "Tobias", lname = "Refsnes")

my_function6("Pakistan")
my_function6("India")
my_function6()
my_function6("Brazil")