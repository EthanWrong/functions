# NB: for some functions I have asked the user to input values, and for others I have called the values myself.
#     I want to show that I can do both.

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


# MAIN ROUTINE

print("Exercise 12: ")
ticket_sales()
