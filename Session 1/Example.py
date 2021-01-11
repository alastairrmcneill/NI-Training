# Data types 
# x = 5.0
# print(type(x))
# Question fixed points?
# Question imaginary numbers 

# text = "Hello"
# print(type(text))

# boolean1 = True
# boolean2 = not boolean1

# print(boolean2)


# Different Data Types

# myList = [10, 20, 30, 40, 50]


# Alastair = {"first_name":"Alastair", "last_name": "McNeill", "Mental_Age": 5}
# David = {"first_name":"David", "last_name": "Guest", "Mental_Age": 7}

# people = [Alastair, David]

# print(people[1]["Mental_Age"])



# Loops

# for i in range(5,10):
#     print("Hi")

# names = ["James", "Chris", "Dan", "Jonah"]

# for name in names:
#     print("Hello " + name)

# x = 0
# while x < 5:

#     print(x)
#     x += 1 

# Comparissons 
# a = 5
# b = 1


# if a == 5:
#     print("Winner")
# elif a > 0: 
#     print("Tie")
# else: 
#     print("Loser")


# if a == 5 or b == 10:
#     print("Winner")

# Break and continues

# for i in range(10):
#     if i < 5: 
#         print("Less")
#         continue 
#     else: 
#         print("More")
#         break

#     print("than 5")
#     print("")


# # Input
# number = input("What numbers do want for x? ")


# try: 
#     x = int(number)

#     print(type(x))
# except ValueError:
#     print("That wasn't a number")

#Exercise
# Make a small code that asks the user to guess a pre-determined number and lets them know when they got it right,
# if not then they need to guess again


# number = 7

# while True: 
#     response = input("Please guess a number between 1 and 10: ")
#     if response.lower() == "exit":
#         break


#     try:
#         guess = int(response)
#     except:
#         print("Please put in a whole number.")
#         continue 

#     if guess == number: 
#         print("Congrats!")
#         break
#     else: 
#         print("Incorrect please guess again.")



# Fucntions
# def helloWorld():
#     print("Hello World")


# def add5(x):
#     y = x + 5
#     print(y)

# def multiply(x, y):
#     z = x * y
#     return z

# answer = multiply(5, 10)
# print(multiply(5, 9))

# def acquire_data():
#     pass


# while True: 
#     pass

# if a == 5: 
#     pass 

# Classes
# class Car:
#     brand = "Seat"
#     model = "Ibiza"
#     colour = "Red"

# myCar = Car()
# yourCar = Car()
# print(myCar.brand)
# print(yourCar.brand)

class Car: 
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour

    def start_car(self):
        print("Starting my " + self.model)

myCar = Car("Seat", "Ibiza FR", "Red")
# yourCar = Car("Ford", "Mustang", "Blue with white stipes")
# print(myCar.model)
# print(yourCar.model)

myCar.start_car()







    











    


