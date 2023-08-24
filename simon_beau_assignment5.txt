'''
Beau Simon
CSCI L02
Assignment #5
Online Student - 0869416
'''

def displayBalance(account):
    name = account['Name']
    savings_balance = account['Savings']
    checking_balance = account['Checking']
    card_balance = account['Card']
    card_limit = account['Limit']

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
    print(f"{'Account owner’s name:':<25}{name:<15}")
    print(f"{'Account Balance':>25}{'Available Balance':>23}")
    print(f"Savings{'${:,.2f}'.format(savings_balance):>17}{'${:,.2f}'.format(savings_available_balance):>23}")
    print(f"Checking{'${:,.2f}'.format(checking_balance):>16}{'${:,.2f}'.format(checking_available_balance):>23}")
    print(f"Card{'${:,.2f}'.format(card_balance):>20}{'${:,.2f}'.format(card_available_balance):>23}")


def updateAccount(account):
    savings_balance = account['Savings']
    account['Savings'] += 200
    print("Savings account has been credited by $200.")
    
    displayBalance(account)


def menu(account):
    while True:
        print("\nMenu:")
        print("1. Display Balance")
        print("2. Update Account")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            displayBalance(account)
        elif choice == '2':
            updateAccount(account)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    name = input("Enter your name: ")
    account = {
        'Name': name,
        'Savings': 100.0,
        'Checking': 20.0,
        'Card': 10.0,
        'Limit': 50
    }
    menu(account)

if __name__ == '__main__':
    main()
