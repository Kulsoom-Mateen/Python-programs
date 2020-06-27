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

def my_function7(food):
  for x in food:
    print(x)

def my_function8(x):
  return 5 * x

def tri_recursion9(k):
  if(k > 0):
    result = k + tri_recursion9(k - 1)
    print(result)
  else:
    result = 0
  return result

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

fruits = ["apple", "banana", "cherry"]
my_function7(fruits)

print(my_function8(3))
print(my_function8(5))
print(my_function8(9))

print("\n\nRecursion Example Results")
tri_recursion9(6)