def perform_operation(num1:float, num2:float, operation:str):
    result = 0
    match operation:
        case "add":
            result = num1 + num2
        case "subtraction":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num1 > num2:
                result = num1 / num2
            else:
                result = num2 / num1
    return result
