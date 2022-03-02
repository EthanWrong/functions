# NB: for some functions I have asked the user to input values, and for others I have called the values myself.
#     I want to show that I can do both.

# exercise 11
def calc_fine(days_overdue):
    per_day_charge = days_overdue * 0.80
    total_charge = 0.5 + per_day_charge
    if total_charge > 30.00:
        total_charge = 30.00
    return "Fine is ${0:.2f}".format(total_charge)


# MAIN ROUTINE

print("Exercise 11: ")
days_overdue = int(input("How many days is your book overdue: "))
print(calc_fine(days_overdue))
print()
