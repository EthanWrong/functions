# NB: for some functions I have asked the user to input values, and for others I have called the values myself.
#     I want to show that I can do both.

# exercise 9
def longest_word(string_list):
    current_longest = 0
    current_word = ""
    for i in string_list:
        if len(i) > current_longest:
            current_longest = len(i)
            current_word = i
    return current_word


# MAIN ROUTINE

print("Exercise 9: ")
string_list = ["Jack", "Tomato", "Cat", "Trains"]
print(f"The longest word is: {longest_word(string_list)}")
print()
