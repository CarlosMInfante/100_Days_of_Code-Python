# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = round(bill * tip_as_percent, 2)
total_bill = round(bill + total_tip_amount, 2)
split_amount = "{:.2f}".format(round(total_bill / people, 2))

print(f"Total Tip: ${total_tip_amount}")
print(f"Total Bill: ${total_bill}")
print(f"Per Person: ${split_amount}")
