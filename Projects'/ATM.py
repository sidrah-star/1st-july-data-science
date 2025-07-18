class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"\nYour current balance is ₹{self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("\nDeposit amount must be positive.")
        else:
            self.balance += amount
            print(f"\n₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("\nWithdrawal amount must be positive.")
        elif amount > self.balance:
            print("\nInsufficient balance.")
        else:
            self.balance -= amount
            print(f"\n₹{amount} withdrawn successfully.")

    def run(self):
        print("=== Welcome to Python ATM ===")
        while True:
            print("\nPlease choose an option:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter choice (1/2/3/4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: ₹"))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: ₹"))
                self.withdraw(amount)
            elif choice == '4':
                print("\nThank you for using Python ATM!")
                break
            else:
                print("\nInvalid option. Please try again.")

# Create ATM instance and run
atm_machine = ATM(balance=5000)  # Starting balance ₹5000
atm_machine.run()
