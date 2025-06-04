def perform_operation(num1, num2, operation):
    # result = 0
    # match operation:
    #     case "add":
    #         result = num1 + num2
    #     case "subtraction":
    #         result = num1 - num2
    #     case "multiply":
    #         result = num1 * num2
    #     case "divide":
    #         if num1 > num2:
    #             result = num1 / num2
    #         else:
    #             result = num2 / num1
    # return result
    if operation == "add":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 > 0:
            if num1 > num2:
                return num1 / num2
            else:
                return num2 / num1
