class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")


# Create first account
name1 = input("Enter first account holder name: ")
balance1 = float(input("Enter opening balance: "))

account1 = BankAccount(name1, balance1)

# Create second account
name2 = input("\nEnter second account holder name: ")
balance2 = float(input("Enter opening balance: "))

account2 = BankAccount(name2, balance2)

# Transactions for first account
print("\n--- First Account ---")
account1.check_balance()

deposit_amount = float(input("Enter amount to deposit: "))
account1.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account1.withdraw(withdraw_amount)

account1.check_balance()

# Transactions for second account
print("\n--- Second Account ---")
account2.check_balance()

deposit_amount = float(input("Enter amount to deposit: "))
account2.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account2.withdraw(withdraw_amount)

account2.check_balance()