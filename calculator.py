# This is a basic calculator

# Ask user for the first number
num1 = int(input("Enter the first number: "))

# Ask user for the second number
num2 = int(input("Enter the second number: "))

# Ask user for the operation to use
operation = input("Enter the operation (+, -, *, /): ")

# Perform the chosen operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
