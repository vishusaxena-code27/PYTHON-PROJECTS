id="k3q8px"
# Function to calculate factorial
def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


# Taking input
number = int(input("Enter a number: "))

# Display result
print("Factorial:", factorial(number))
