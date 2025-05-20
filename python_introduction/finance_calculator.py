
"""
This script will calculate the user’s monthly savings based on inputted monthly
income and expenses. It will then project these savings over a year, assuming a fixed interest rate,
to demonstrate compound interest’s effect on savings.


Calculate the projected savings after one year, incorporating the interest. Use the simplified formula for annual
savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
"""

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses= int(input("Enter your total monthly expenses: "))
annual_interest_rate = 5/100

monthly_savings = monthly_income - monthly_expenses

print(f"Your monthly savings are ${monthly_savings}")

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

print(f"Projected savings after one year, with interest, is: ${projected_savings}.")


