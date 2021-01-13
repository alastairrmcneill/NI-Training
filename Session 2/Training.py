# Data tpyes

# x = 5.0 
# print(type(x))

# text = "Hello World > "
# print(text)


# boolean1 = True
# boolean2 = not boolean1

# print(boolean1)

# myList = [10,20,30,40,50]
# myList.append(60)
# myList.pop(0)
# myList.remove()


# print(myList.index(40))

# # print(myList)

# myDict = {"first_name": "Alastair","last_name": "McNeill", "age": 26}

# print(myDict["first_name"])


###############################################################################
# Loops

# for i in range(0,10):
#     print(i)

# print("Done")

# Names = ["Sach", "Ash", "Ed", "Alasdair"]

# for name in Names:
#     print(name)

# j = 0

# while j < 5:
#     j += 1
#     for i in range(0,10):
#         print(i * j)

# print("Done")
    


##################################
# Conditionals, if etc


# x = 1
# y = 11


# if x >= 10 :
#     print("Winner")


# print("Done")

# # QUESTION Printf?

############################
# Break and continue

# for i in range(0,10):
#     if i < 5:
#         print("Hi")
#         continue
#     else:
#         print("Hello")
#         # break 

#     print("World")


################################
# User inputs

# x = input("What are your dog's names? ").split(",")


# print(x)

#####################################################
# Make a guessing game 
# Ask the user to guess a number 
# Let them know if correct or not 
# If not, redo and keep asking
# If they get it right, end the game

# number = 20
# run = True

# while run:
#     guessed = input("What number would you like to guess? ")
#     guessed_num = int(guessed)
#     if guessed_num == number:
#         print("Congratulations you got it right!")
#         run = False
#     else:
#         print("Incorrect. Please guess again.")



##################
# Error handling
# number = 20
# run = True

# while run:
#     guessed = input("What number would you like to guess? ")
#     try:
#         guessed_num = int(guessed)
#     except ValueError:
#         print("That wasn't a whole number.")
#         continue

#     if guessed_num == number:
#         print("Congratulations you got it right!")
#         run = False
#     else:
#         print("Incorrect. Please guess again.")


#####################
# Function

# def add5(x):
#     y = x + 5
#     return y

# def multiply(x, y):
#     return x * y

# print(multiply(2,4))

# def divide(x,y):
#     pass 

####################
class Car:
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour

    def start_car(self):
        print("Starting my " + self.model)

myCar = Car("Seat", "Ibiza", "Red")
myCar.start_car()


##########
# Starting again at 3:10pm

