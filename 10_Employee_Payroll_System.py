class Employee:
    def __init__(self, employee_id, name, basic_salary):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = self.basic_salary * 0.20
        da = self.basic_salary * 0.10
        pf = self.basic_salary * 0.12

        net_salary = self.basic_salary + hra + da - pf

        print("\nEmployee ID:", self.employee_id)
        print("Employee Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", hra)
        print("DA:", da)
        print("PF:", pf)
        print("Net Salary:", net_salary)


# Taking employee details
employee_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

# Create employee object
employee = Employee(employee_id, name, basic_salary)

# Calculate and display salary
employee.calculate_salary()