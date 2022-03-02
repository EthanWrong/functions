# NB: for some functions I have asked the user to input values, and for others I have called the values myself.
#     I want to show that I can do both.


# exercise 4
def starts_with_A():
    word = str(input("Please enter a word to test if the first letter is a capital A: "))
    # this will only return True if the word begins with a capital A
    if word[0] == "A":
        return True
    else:
        return False


# MAIN ROUTINE

print("Exercise 4: ")
print(starts_with_A())
print()
