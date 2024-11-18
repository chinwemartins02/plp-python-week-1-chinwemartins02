# Ask for user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Perform the chosen operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

# Display the result
print("Result:", result)
