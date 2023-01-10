# Project 1 - Band Name Generator

# Instructions:
# Create a greeting for your program
# Ask the user for the city that they grew up in
# Ask the user for the name of a pet
# Combine the name of their city and pet and show them their band name
# Make sure the input cursor shows on a new line!

print("Welcome To The Band Name Generator!")
user_city = input("What city did you grow up in?\n")
user_pet = input("If you own a pet, please provide the name of your pet here. Otherwise, if you've never owned a pet, think of a name anyway :)\n")
generate_band_name = user_city + " " + user_pet
print("Your band's name is " + generate_band_name + "! Yeaaaa Rock On!")