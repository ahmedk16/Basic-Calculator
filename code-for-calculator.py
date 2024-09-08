# Basic Calculator

# Get input from user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get the desired operation
operation = input("Enter operation (+, -, *, /): ")

# Perform the operation and display the result

#For Addition
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

# For Subtraction
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

# For Multiplication
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

# For Division 
elif operation == '/':
    if num2 != 0:                                   
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

# If there Is any Command Other than ( +, -, *, /)        
else:
    print("Invalid operation.")
