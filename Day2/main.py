# num_char = len(input("What is your name?"))
# print("Your name has " + str(num_char) + " characters.")


# two_digit_number = input("Type a two digit number:")
# print(type(two_digit_number))
# a = int(two_digit_number[0]) + int(two_digit_number[1])
# print(a)


# height = float(input("Enter your height in m:\n"))
# weight = int(input("Enter your weight in kg:\n"))

# bmi = round(weight / height ** 2)
# print(bmi)

age = input("What is your current age?")
int_age = int(age)

years = 90 - int_age
days_remaining = years * 365
weeks_remaining = years * 52
months_remaining = years * 12

print(
    f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
