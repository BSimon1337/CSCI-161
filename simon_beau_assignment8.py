'''
Beau Simon
CSCI L02
Assignment #8
Online Student - 0869416
'''

import os

#I had to change the directory. Might not be needed when you grade this.

os.chdir(r"C:\Users\beau.a.simon\OneDrive - North Dakota University System\Desktop\CSCI\assignment 8")

# Function to read employee details from file
def read_employee(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            employee = line.strip().split(',')
            print(f"{employee[0]}, '{employee[1]}'")

# Function to calculate monthly payment and write to output file
def calculate_payment(regular_file, hourly_file):
    with open(regular_file, 'r') as rf, open(hourly_file, 'r') as hf, open('Paycheck.txt', 'w') as pf:
        for line in rf:
            employee = line.strip().split(',')
            monthly_salary = float(employee[2])/12
            pf.write(f"{employee[0]}, '{employee[1]}', {monthly_salary:.2f}\n")

        for line in hf:
            employee = line.strip().split(',')
            monthly_salary = float(employee[2]) * float(employee[3])
            pf.write(f"{employee[0]}, '{employee[1]}', {monthly_salary:.2f}\n")

# Function to display paycheck details
def display_paycheck():
    try:
        with open('Paycheck.txt', 'r') as f:
            for line in f:
                employee = line.strip().split(',')
                print(f"{employee[0]}, '{employee[1]}', {employee[2]}")
    except FileNotFoundError:
        print("Paycheck file not found. Please calculate payment first.")

# Main program
while True:
    print("Choose an option:")
    print("Option 1: Display all employee details from both input files")
    print("Option 2: Calculate monthly payment of all employees and write to output file")
    print("Option 3: Display paycheck details of all employees")
    print("Option 4: Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Employee details from Regular_emp.txt:")
        read_employee('Regular_emp.txt')
        print("Employee details from Hourly_emp.txt:")
        read_employee('Hourly_emp.txt')
    elif choice == '2':
        calculate_payment('Regular_emp.txt', 'Hourly_emp.txt')
        print("Payment details written to Paycheck.txt")
    elif choice == '3':
        display_paycheck()
    elif choice == '4':
        print("Exiting program")
        break
    else:
        print("Invalid choice. Please try again.")
