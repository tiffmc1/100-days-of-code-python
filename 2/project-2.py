# Project 2 - Tip Calculator

print("Welcome To The Tip Calculator!")

total_bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percent tip would you like to give? Enter either 18, 20, or 22. "))

party_size = int(input("How many people to split the bill? "))

tip = (tip_percentage / 100) + 1

total_per_person = round((total_bill * tip) / party_size, 2)

# format method below makes sure that each outcome will ALWAYS be rounded to the tenth decimal. So even if the final bill per person is a whole number, then it will still print "$12.00" instead of "$12.0"
final_bill = "{:.2f}".format(total_per_person)

print(f"Each person should pay: ${final_bill}")