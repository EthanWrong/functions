# NB: for some functions I have asked the user to input values, and for others I have called the values myself.
#     I want to show that I can do both.

# exercise 10
def calc_gst(net_price):
    return "${0:.2f}".format((net_price * 1.15))


# MAIN ROUTINE

print("Exercise 10: ")
print(calc_gst(59.95))
print()
