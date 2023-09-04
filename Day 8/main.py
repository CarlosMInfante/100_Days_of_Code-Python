# def greet(name):
#     print(f"Hello, {name}")
#     print("How are you doing today?")
#     print("Third thing here")


# name = input("What is your name?\n")

# greet(name)

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}.")


name = input("What is your name?\n")
location = input("Where are you from?\n")

greet_with(name, location)
