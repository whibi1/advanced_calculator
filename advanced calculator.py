import math

def calculate(numbers, operators):
    """Performs calculation based on the numbers and operators list."""
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i+1]
        elif operators[i] == "-":
            result -= numbers[i+1]
        elif operators[i] == "*":
            result *= numbers[i+1]
        elif operators[i] == "/":
            result /= numbers[i+1]
        elif operators[i] == "^":
            result = pow(result, numbers[i+1])
        elif operators[i] == "sqrt":
            result = math.sqrt(numbers[i])
    return result

print("dvanced Calculator")
print("Please enter the numbers and operators to perform calculations.")
print("Example: 3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3 sqrt 25")

while True:
    try:
        user_input = input("Expression: ")
        user_input = user_input.replace(" ", "")  # remove whitespaces
        numbers = []
        operators = []
        number = ""
        
        # separate the numbers and operators
        for char in user_input:
            if char.isnumeric() or char == ".":
                number += char
            else:
                if number:
                    numbers.append(float(number))
                    number = ""
                if char in "+-*/^sqrt":
                    operators.append(char)
        
        if number:
            numbers.append(float(number))
        
        # reorder the operators based on priority
        while "^" in operators:
            index = operators.index("^")
            numbers[index] = pow(numbers[index], numbers[index+1])
            del numbers[index+1]
            del operators[index]
            
        while "sqrt" in operators:
            index = operators.index("sqrt")
            numbers[index] = math.sqrt(numbers[index])
            del operators[index]
        
        while "/" in operators or "*" in operators:
            index = operators.index("/") if "/" in operators else operators.index("*")
            if operators[index] == "/":
                numbers[index] = numbers[index] / numbers[index+1]
            else:
                numbers[index] = numbers[index] * numbers[index+1]
            del numbers[index+1]
            del operators[index]
            
        while "+" in operators or "-" in operators:
            index = operators.index("+") if "+" in operators else operators.index("-")
            if operators[index] == "+":
                numbers[index] = numbers[index] + numbers[index+1]
            else:
                numbers[index] = numbers[index] - numbers[index+1]
            del numbers[index+1]
            del operators[index]
        
        print("Result: ", numbers[0])
        
    except (ValueError, ZeroDivisionError):
        print("Invalid input. Please try again.")
    except IndexError:
        print("Invalid expression. Please try again.")
    
    continue_calculation = input("Do you want to continue? (Y/N): ")
    if continue_calculation.lower() == "n":
        break

print("Calculator closed. Have a nice day!")
