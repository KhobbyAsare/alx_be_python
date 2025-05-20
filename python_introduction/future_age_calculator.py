
"""
asks the user for their current age and then calculates how old they will be in a specific future year.

"""

user_current_age = int(input("How old are you? "))

future_year = 2050
current_year = 2023

years_from_now = future_year - current_year

age = user_current_age + years_from_now

print(f"In {future_year}, you will be {age} years old")