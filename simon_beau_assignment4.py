'''
Beau Simon
CSCI L02
Assignment #4
Online Student - 0869416
'''

# Define an empty dictionary to store employee details
emp = {}

# Function to create a new employee in the dictionary
def create_employee():
    # Ask for employee ID and name from user input
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    # Add the employee to the dictionary
    emp[emp_id] = emp_name
    # Print a message to confirm the employee was added
    print("Employee details added successfully")

# Function to display all employees in the dictionary
def display_employee():
    # Check if the dictionary is empty
    if not emp:
        print("No employee details found")
    else:
        # Iterate over each key-value pair in the dictionary and print the details
        print("Employee details:")
        for key, value in emp.items():
            print("Employee ID:", key, "\tEmployee Name:", value)

# Function to update an existing employee in the dictionary
def update_employee():
    # Ask for the employee ID to update
    emp_id = input("Enter Employee ID to update: ")
    # Check if the ID exists in the dictionary
    if emp_id in emp:
        # Ask for the new name and update the dictionary
        emp_name = input("Enter new Employee Name: ")
        emp[emp_id] = emp_name
        # Print a message to confirm the employee was updated
        print("Employee details updated successfully")
    else:
        # Print a message if the ID was not found in the dictionary
        print("Employee ID not found")

# Function to sort the employee dictionary by ID and display the sorted results
def sort_employee():
    # Check if the dictionary is empty
    if not emp:
        print("No employee details found")
    else:
        # Sort the dictionary by key (employee ID)
        sorted_emp = sorted(emp.items(), key=lambda x: x[0])
        # Iterate over each key-value pair in the sorted dictionary and print the details
        print("Employee details sorted by Employee ID:")
        for item in sorted_emp:
            print("Employee ID:", item[0], "\tEmployee Name:", item[1])

# Main program loop
while True:
    # Display the menu options to the user
    print("========= Employee Management System =========")
    print("1. Create Employee Details")
    print("2. Display the Employee Details")
    print("3. Update the dictionary")
    print("4. Sort the dictionary based on key")
    print("5. Exit")
    print("==============================================")

    # Ask for the user's choice
    choice = input("Enter your choice: ")

    # Call the appropriate function based on the user's choice
    if choice == '1':
        create_employee()

    elif choice == '2':
        display_employee()

    elif choice == '3':
        update_employee()

    elif choice == '4':
        sort_employee()

    elif choice == '5':
        print("Exiting the program")
        break

    else:
        # Print a message if an invalid choice was entered
        print("Invalid choice, please try again")

