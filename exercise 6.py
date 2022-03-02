# NB: for some functions I have asked the user to input values, and for others I have called the values myself.
#     I want to show that I can do both.


# exercise 6
def numbers_in_list(list):
    multiple = int(input("Please pick a factor: "))
    output = []
    for i in range(len(list)):
        if list[i] % multiple == 0:
            output.append(list[i])
    return output


# MAIN ROUTINE

print("Exercise 6: ")
list_of_numbers = [1, 4, 6, 7, 15, 22, 35, 45]
print(numbers_in_list(list_of_numbers))
print()
