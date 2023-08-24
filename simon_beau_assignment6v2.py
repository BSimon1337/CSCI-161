'''
Beau Simon
CSCI L02
Assignment #6
Online Student - 0869416
'''

class Account:
    def __init__(self, name, savings, checking, card, limit):
        self.name = name
        self.savings = savings
        self.checking = checking
        self.card = card
        self.limit = limit

    def displayBalance(self):
        print(f"Account owner’s name: {self.name}")
        print("{:<15} {:>10} {:>10}".format("Account Type", "Balance", "Available"))
        print("{:<15} {:>10.2f} {:>10.2f}".format("Savings", self.savings, self.savings - 10))
        print("{:<15} {:>10.2f} {:>10.2f}".format("Checking", self.checking, self.checking))
        print("{:<15} {:>10.2f} {:>10.2f}".format("Card", self.card, self.limit - self.card))


    def updateAccount(self):
        account_type = input("Enter account type (Savings - S or Checking - K): ")
        amount = float(input("Enter amount to be updated: "))
        if account_type == 's':
            if self.savings + amount >= 0:
                self.savings += amount
                print("Savings account has been updated.")
            else:
                print("Insufficient funds in savings account.")
        elif account_type == 'k':
            if self.checking + amount >= 0:
                self.checking += amount
                print("Checking account has been updated.")
            else:
                print("Insufficient funds in checking account.")
        else:
            print("Invalid account type. Please try again.")


def main():
    name = input("Enter your name: ")
    account = Account(name, 100.0, 20.0, 10.0, 50)
    while True:
        print("\nMenu:")
        print("1. Display Balance")
        print("2. Update Account")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            account.displayBalance()
        elif choice == '2':
            account.updateAccount()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

