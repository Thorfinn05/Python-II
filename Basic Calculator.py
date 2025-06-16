class FormulaError (Exception):
    '''Custom exception for invalid formula'''
    pass

def calculate(expression):
    parts =  expression.split()
    if len(parts) != 3:
        raise FormulaError("Input must have 3 elements (e.g., 3 + 5).")
    num1 , operator, num2 = parts
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise FormulaError("The first and third elements must be numbers")
    if operator not in ('+', '-'):
        raise FormulaError("Only '+' or '-' operators are allowed.")
    return num1 + num2 if operator == '+' else num1 - num2

while True:
    user_input = input("Enter expression (or type 'quit'): ")
    if user_input == 'quit':
        break
    try:
        result = calculate(user_input)
        print("Result: ", result)
    except FormulaError as e:
        print("FormulaError: ", e)