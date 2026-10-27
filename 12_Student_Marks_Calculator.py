
# Function to calculate total marks
def calculate_total(marks):
    return sum(marks)


# Function to calculate average marks
def calculate_average(total, subjects):
    return total / subjects


# Taking marks of 5 subjects
marks = []

for i in range(5):
    mark = float(input(f"Enter marks of subject {i + 1}: "))
    marks.append(mark)

# Calculate total
total = calculate_total(marks)

# Calculate average
average = calculate_average(total, 5)

# Display result
print("\nTotal Marks:", total)
print("Average Marks:", average)
