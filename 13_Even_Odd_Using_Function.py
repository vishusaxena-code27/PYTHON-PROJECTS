# Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Taking input
number = int(input("Enter a number: "))

# Display result
result = check_even_odd(number)

print("The number is:", result)