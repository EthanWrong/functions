# NB: for some functions I have asked the user to input values, and for others I have called the values myself.
#     I want to show that I can do both.
#     Please uncomment an exercise in the main routine to test it.

# exercise 1
def addition():
    number1 = int(input("Please enter first number: "))
    number2 = int(input("Please enter second number: "))
    return number1 + number2


# exercise 2
def make_positive():
    number = int(input("Please enter a number to make positive: "))
    if number < 0:
        return number * -1
    else:
        return number


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


# exercise 4
def starts_with_A():
    word = str(input("Please enter a word to test if the first letter is a capital A: "))
    # this will only return True if the word begins with a capital A
    if word[0] == "A":
        return True
    else:
        return False


# exercise 5 (does num1 have the factor num2)
def check_factor():
    num1 = int(input("Please enter a number to test if it has a factor: "))
    num2 = int(input(f"Please enter a number to test if it is the factor of {num1}: "))

    if num1 % num2 == 0:
        return f"{num2} is a factor of {num1}"
    else:
        return f"{num2} is not a factor of {num1}"


# exercise 6
def numbers_in_list(list):
    multiple = int(input("Please pick a multiplier: "))
    output = []
    for i in range(len(list)):
        if list[i] % multiple == 0:
            output.append(list[i])
    return output


# exercise 7
def print_name():
    name = str(input("Please enter your name: "))
    number = int(input("Please enter number of times to be repeated: "))
    while number > 0:
        print(name)
        number -= 1


# exercise 8
def print_word(word, number):
    return word[0:number].upper() + word[number:].lower()


# exercise 9
def longest_word(string_list):
    current_longest = 0
    current_word = ""
    for i in string_list:
        if len(i) > current_longest:
            current_longest = len(i)
            current_word = i
    return current_word


# exercise 10
def calc_gst(net_price):
    return "${0:.2f}".format((net_price * 1.15))


# exercise 11
def calc_fine(days_overdue):
    per_day_charge = days_overdue * 0.80
    total_charge = 0.5 + per_day_charge
    if total_charge > 30.00:
        total_charge = 30.00
    return "Fine is ${0:.2f}".format(total_charge)


# exercise 12
def ticket_sales():
    want_to_sell = "y"
    a_sales = 0
    s_sales = 0
    c_sales = 0
    g_sales = 0
    while want_to_sell != "n":
        want_to_sell = input("Do you want to sell a ticket (Y/N): ").lower()
        if want_to_sell == "y":
            ticket_to_buy = input(
                "What type of ticket do you want? \nA for adult, or \nS for student, or \nC for child, or \nG for gift voucher, or \nAnything else to cancel \n>> ").lower()
            if ticket_to_buy == "a":
                a_sales += 1
            elif ticket_to_buy == "s":
                s_sales += 1
            elif ticket_to_buy == "c":
                c_sales += 1
            elif ticket_to_buy == "g":
                g_sales += 1
            else:
                print("Ticket sale cancelled. ")

        elif want_to_sell == "n":
            total_sales = a_sales*12.50 + s_sales*9.00 + c_sales*7.00
            print("=============================================")
            print(f"The total tickets sold today was {a_sales+s_sales+c_sales+g_sales}")
            print("This was made up of: ")
            print(f"{a_sales} for adults; and")
            print(f"{s_sales} for students; and")
            print(f"{c_sales} for children; and")
            print(f"{g_sales}  gift vouchers")
            print()
            print(f"Sales for the day came to ${total_sales}")
            print("=============================================")
        print()


# MAIN ROUTINE (each function called is in order of exercises)

# print("Exercise 1: ")
# print(f"The sum of the two numbers is: {addition()}")
# print(f"The sum of the two numbers is: {addition()}")
# print()
#
# print("Exercise 2: ")
# print(make_positive())
# print()
#
# print("Exercise 3: ")
# print(check_status())
# print()
#
# print("Exercise 4: ")
# print(starts_with_A())
# print()

# print("Exercise 5: ")
# print(check_factor())
# print()

# print("Exercise 6: ")
# list_of_numbers = [1, 4, 6, 7, 15, 22, 35]
# print(numbers_in_list(list_of_numbers))
# print()

# print("Exercise 7: ")
# print_name()
# print()

# print("Exercise 8: ")
# print(print_word("Pineapple", 4))
# print()

# print("Exercise 9: ")
# string_list = ["Jack", "Tomato", "Cat", "Trains"]
# print(f"The longest word is: {longest_word(string_list)}")
# print()

# print("Exercise 10: ")
# print(calc_gst(59.95))
# print()

# print("Exercise 11: ")
# print(calc_fine(13))
# print()

# print("Exercise 12: ")
# ticket_sales()
