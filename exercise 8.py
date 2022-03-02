# NB: for some functions I have asked the user to input values, and for others I have called the values myself.
#     I want to show that I can do both.


# exercise 8
def print_word(word, number):
    return word[0:number].upper() + word[number:].lower()


# MAIN ROUTINE

print("Exercise 8: ")
print(print_word("Pineapple", 4))
print()
