# Function to calculate simple interest
def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


# Taking input
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

# Calculate simple interest
interest = simple_interest(principal, rate, time)

# Display result
print("Simple Interest:", interest)