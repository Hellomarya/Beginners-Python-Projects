class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have successfully deposited ${amount}.")
            self.check_balance()
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"You have successfully withdrawn ${amount}.")
            self.check_balance()
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def run(self):
        while True:
            print("\nWelcome to the ATM")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Please choose an option (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    atm = ATM(balance=1000)  # Starting balance is $1000
    atm.run()
