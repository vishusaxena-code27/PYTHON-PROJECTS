# Create a class
class Employee:

    # Function to store employee details
    def set_details(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    # Function to display employee details
    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


# Create object
employee = Employee()

# Take input
name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))

# Store details
employee.set_details(name, employee_id, salary)

# Display details
employee.display()