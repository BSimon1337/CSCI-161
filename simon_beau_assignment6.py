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

    def display_balance(self):
        savings_balance = self.savings
        checking_balance = self.checking
        card_balance = self.card
        card_limit = self.limit

        # Rule a: Minimum amount of $10 must be maintained in the savings account
        if savings_balance < 10:
            savings_available_balance = 0
        else:
            savings_available_balance = savings_balance - 10

        # Rule b: Checking account can have any amount larger than or equal to zero
        checking_available_balance = checking_balance

        # Rule c: Card available balance cannot exceed its limit
        if card_balance >= card_limit:
            card_available_balance = 0
        else:
            card_available_balance = card_limit - card_balance

        # Calculate total account balance and available balance
        account_balance = savings_balance + checking_balance + card_balance
        available_balance = savings_available_balance + checking_available_balance + card_available_balance

        # Print out the account balance and available balance
        print(f"Account owner's name: {self.name}")
        print("Account Balance".rjust(25), "Available Balance".rjust(25))
        print("Savings".rjust(10), f"${savings_balance:.2f}".rjust(11), f"${savings_available_balance:.2f}".rjust(20))
        print("Checking".rjust(10), f"${checking_balance:.2f}".rjust(11), f"${checking_available_balance:.2f}".rjust(20))
        print("Card".rjust(10), f"${card_balance:.2f}".rjust(11), f"${card_available_balance:.2f}".rjust(20))

    def update_account(self):
        self.savings += 200
        print("Savings account has been credited by $200.")
        self.display_balance()


def menu(account):
    while True:
        print("\nMenu:")
        print("1. Display Balance")
        print("2. Update Account")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            account.display_balance()
        elif choice == '2':
            account.update_account()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    name = input("Enter your name: ")
    account = Account(name, 100.0, 20.0, 10.0, 50)
    menu(account)

if __name__ == '__main__':
    main()
