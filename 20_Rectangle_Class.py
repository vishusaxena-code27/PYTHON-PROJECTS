# Create a class
class Rectangle:

    # Function to store length and width
    def set_details(self, length, width):
        self.length = length
        self.width = width

    # Function to calculate area
    def calculate_area(self):
        return self.length * self.width

    # Function to calculate perimeter
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Create object
rectangle = Rectangle()

# Take input
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Store details
rectangle.set_details(length, width)

# Display results
print("Area:", rectangle.calculate_area())
print("Perimeter:", rectangle.calculate_perimeter())