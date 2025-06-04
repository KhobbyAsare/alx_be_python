def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num1 == 0 or num2 == 0:
            return "Error: Division by zero is not allowed."
        if num1 > num2:
            return num1 / num2
        else:
            return num2 / num1
