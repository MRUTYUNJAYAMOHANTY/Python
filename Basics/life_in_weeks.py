# Example Input
# 56

# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.
# Target age is 90 years

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# N.B : 1 year is 365 days, 52 weeks, 12 months

# Write your code below this line 👇

age_int = int(age)
years_remaining = 90 - age_int
days_remaining = years_remaining * 365
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
print(f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left.")









