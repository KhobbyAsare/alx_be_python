"""
Task Description:

Develop a Python script named match_case_calculator.py. This calculator will prompt the user to enter two numbers
and select an operation (addition, subtraction, multiplication, or division). The script will then perform the
selected operation using a Match Case statement and display the result.
"""

num1 = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

result = 0

match operation:
    case "+":
        result =  num1 + num2
    case "-":
        result = num1 - num2   
    case "*":
        result = num1 * num2
    case "/":
        if num2 <= 0 :
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
        
print(f"The result is {result}")