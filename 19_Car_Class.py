# Create a class
class Car:

    # Function to store car details
    def set_details(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Function to display car details
    def display(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
        print("Car Price:", self.price)


# Create object
car = Car()

# Take input
brand = input("Enter car brand: ")
model = input("Enter car model: ")
price = float(input("Enter car price: "))

# Store details
car.set_details(brand, model, price)

# Display details
car.display()