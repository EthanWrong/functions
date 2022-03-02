# NB: for some functions I have asked the user to input values, and for others I have called the values myself.
#     I want to show that I can do both.


# exercise 7
def print_name():
    name = str(input("Please enter your name: "))
    number = int(input("Please enter number of times to be repeated: "))
    while number > 0:
        print(name)
        number -= 1


# MAIN ROUTINE

print("Exercise 7: ")
print_name()
print()
