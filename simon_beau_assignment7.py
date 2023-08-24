'''
Beau Simon
CSCI L02
Assignment #7
Online Student - 0869416
'''

from datetime import datetime

# Function to read date from user input and return a date object
def read_date():
    date_str = input("Enter a date in the format yyyy-mm-dd: ")
    return datetime.strptime(date_str, '%Y-%m-%d').date()

# Function to sort the list of date objects and display in 'mm/dd/yyyy' format
def sort_dates(date_list):
    sorted_dates = sorted(date_list)
    sorted_dates_str = [d.strftime('%m/%d/%Y') for d in sorted_dates]
    print("Sorted dates: ", sorted_dates_str)

# Function to calculate and display the number of days between the last two dates in the sorted date list
def days(date_list):
    if len(date_list) < 2:
        print("At least two dates are required for this option.")
    else:
        last_date = date_list[-1]
        second_last_date = date_list[-2]
        days_diff = (last_date - second_last_date).days
        print("Number of days between last two dates: ", days_diff)

# Function to display menu options and call the corresponding functions
def menu():
    date_list = []
    while True:
        print("\nMENU")
        print("1. Read the Dates")
        print("2. Sort the Dates")
        print("3. Calculate and display the number of days between the last two dates")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            date = read_date()
            date_list.append(date)
            print("Date added: ", date.strftime('%m/%d/%Y'))
        elif choice == '2':
            if len(date_list) == 0:
                print("At least one date is required for this option.")
            else:
                sort_dates(date_list)
        elif choice == '3':
            days(date_list)
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    menu()
