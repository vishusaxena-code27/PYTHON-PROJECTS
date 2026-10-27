# Function for addition
def add(a, b):
    return a + b


# Function for subtraction
def subtract(a, b):
    return a - b


# Function for multiplication
def multiply(a, b):
    return a * b


# Function for division
def divide(a, b):
    return a / b


# Taking input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display results
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))

if num2 != 0:
    print("Division:", divide(num1, num2))
else:
    print("Division is not possible by zero.")