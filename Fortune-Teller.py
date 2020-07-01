from random import randint



print("Fortune Teller")
print("Insturctions: ")
print("Type the number you get")
print("The number you get is the fortune you get")
print(randint(1, 4))


userInput = input("Enter your number: ")
if (userInput == "1"):
  print("You will win alot of money")
elif (userInput == "2"):
  print("You will ace a test")
elif (userInput == "3"):
  print("You will score a touchdown")
elif (userInput == "4"):
  print("You will get cool stuff for free")
else:
  print("Thats not a number between 1-4.")