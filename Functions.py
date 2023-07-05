# this is the 1st part of the code
def software_egineering():
  print("Welcome to the team")

# this is calling
software_egineering()

def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")

# Create a function that takes two parameters for :  name and age, and outputs a Birthday message “ Happy Birthday ‘name’ I hear you are ‘age’ today!”

def birthday(name, age):
  print("Happy Birthday,",name, "I hear you are ",age, "today!")

birthday("Jay",28)

# Create a function that takes two parameters: size and type of drink, and then outputs the drinks order.

def drink(TypeDrink, size):
  print("Your drink order is: ",TypeDrink,size)

drink("coke","Lrg")

# Create a cash machine program that takes a pin number and amount. Outputs cash is being dispensed if the pin is correct and there is enough money to withdraw. Finally outputs the new balance.

pin = 172839
cash = 500
def withdraw(pin_num,amount):
  balance = cash - amount
  if (pin_num == pin and cash >= amount):
    print("Here is your cash")
    print("Your balance is:",balance)
  else:
    print("Wrong Pin or Amount too big to withdraw")

withdraw(172839,20)