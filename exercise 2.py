# NB: for some functions I have asked the user to input values, and for others I have called the values myself.
#     I want to show that I can do both.

# exercise 2
def make_positive():
    number = int(input("Please enter a number to make positive: "))
    if number < 0:
        return number * -1
    else:
        return number


# MAIN ROUTINE

print("Exercise 2: ")
print(make_positive())
print()
