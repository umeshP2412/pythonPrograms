
#non-keyward Arguments
def my_funct2(*user):
  print("This is user1: " + user[0])
  print("This is user2: " + user[1])

my_funct2("Umesh", "Patil")

#Keyward Arguments, supplied as dict type
def my_function(**kid):
  print("His last name is " + kid["lname"])
  print("His first name is " + kid["fname"])

my_function(fname = "Umesh", lname = "Patil")

#Keyward Arguments, supplied as dict type using for loop
def myfunc3(**things):
  for key, value in things.items():
    print(key +":" +value)

myfunc3(fruit="apple", fruit2="orange", resident="flat", gender="male")