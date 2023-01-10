# What is the difference between print() and input()?

print("Hello, " + "Tiffany" + "!")
print("Hello, " + input("What is your name?") + "!")

# print() only “prints” out the data supplied to it via its argument, whereas the input function prints the argument (usually in the form of a question) and then waits for an input to be returned from the user. This returned data then replaces the original input data

# Exercise 1: Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string. Warning. Your program should work for different inputs. e.g. any name that you input.
# Example:
# Input - Angela
# Output - 6

# option 1
print(len(input("What is your name? ")))

# option 2 -- notice how Python uses underscores for variables with multiple words, whereas JS uses camelCase
name = input("What is your name? ")
name_len = len(name)
print(name_len)
