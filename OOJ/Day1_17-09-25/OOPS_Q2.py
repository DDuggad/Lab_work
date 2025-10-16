class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Updated balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Updated balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance for {self.name}: {self.balance}")

account1 = BankAccount("Bob", 500)

account1.check_balance()
account1.deposit(200)
account1.withdraw(100)
account1.check_balance()
account1.withdraw(800)
