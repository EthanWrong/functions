# NB: for some functions I have asked the user to input values, and for others I have called the values myself.
#     I want to show that I can do both.

# exercise 3
def check_status():
    bmi = int(input("Please enter BMI: "))
    if bmi >= 30:
        return "obese"
    elif bmi >= 25:
        return "overweight"
    elif bmi >= 18.5:
        return "normal"
    else:
        return "underweight"


# MAIN ROUTINE

print("Exercise 3: ")
print(check_status())
print()
