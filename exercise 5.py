# NB: for some functions I have asked the user to input values, and for others I have called the values myself.
#     I want to show that I can do both.


# exercise 5 (does num1 have the factor num2)
def check_factor():
    num1 = int(input("Please enter a number to test if it has a factor: "))
    num2 = int(input(f"Please enter a number to test if it is the factor of {num1}: "))

    if num1 % num2 == 0:
        return f"{num2} is a factor of {num1}"
    else:
        return f"{num2} is not a factor of {num1}"


# MAIN ROUTINE

print("Exercise 5: ")
print(check_factor())
print()
