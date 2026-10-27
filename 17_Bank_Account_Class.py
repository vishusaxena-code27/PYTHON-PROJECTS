# Create a class
class BankAccount:

    # Function to store account details
    def set_details(self, name, balance):
        self.name = name
        self.balance = balance

    # Function to deposit money
    def deposit(self, amount):
        self.balance = self.balance + amount

    # Function to display account details
    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


# Create object
account = BankAccount()

# Take input
name = input("Enter account holder name: ")
balance = float(input("Enter opening balance: "))

# Store account details
account.set_details(name, balance)

# Deposit money
amount = float(input("Enter amount to deposit: "))
account.deposit(amount)

# Display details
account.display()