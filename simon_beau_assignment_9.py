'''
Beau Simon
CSCI L02
Assignment #9
Online Student - 0869416
'''

import os

class Person:
    def __init__(self, ID, name, address, phone_number, email_id):
        self.ID = ID
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email_id = email_id

    @classmethod
    def read_data(cls):
        ID = input("Enter ID: ")
        name = input("Enter name: ")
        address = input("Enter address: ")
        phone_number = input("Enter phone number: ")
        email_id = input("Enter email ID: ")
        return ID, name, address, phone_number, email_id

    def output_data(self):
        return f"{self.ID}, {self.name}, {self.address}, {self.phone_number}, {self.email_id}"

class Student(Person):
    def __init__(self, ID, name, address, phone_number, email_id, class_status, major):
        super().__init__(ID, name, address, phone_number, email_id)
        self.class_status = class_status
        self.major = major

    @classmethod
    def read_data(cls):
        ID, name, address, phone_number, email_id = super().read_data()
        class_status = input("Enter class status (undergraduate or graduate): ")
        major = input("Enter major of study: ")
        return cls(ID, name, address, phone_number, email_id, class_status, major)

    def output_data(self):
        return f"{super().output_data()}, {self.class_status}, {self.major}"

class Employee(Person):
    def __init__(self, ID, name, address, phone_number, email_id, date_of_joining, department, salary):
        super().__init__(ID, name, address, phone_number, email_id)
        self.date_of_joining = date_of_joining
        self.department = department
        self.salary = salary

class Faculty(Employee):
    def __init__(self, ID, name, address, phone_number, email_id, date_of_joining, department, salary, title, room_no):
        super().__init__(ID, name, address, phone_number, email_id, date_of_joining, department, salary)
        self.title = title
        self.room_no = room_no

    @classmethod
    def read_data(cls):
        ID, name, address, phone_number, email_id = Person.read_data()
        date_of_joining = input("Enter date of joining: ")
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))
        title = input("Enter faculty title: ")
        room_no = input("Enter faculty room number: ")
        return cls(ID, name, address, phone_number, email_id, date_of_joining, department, salary, title, room_no)

    def output_data(self):
        return f"{super().output_data()}, {self.date_of_joining}, {self.department}, {self.salary}, {self.title}, {self.room_no}"

class Staff(Employee):
    def __init__(self, ID, name, address, phone_number, email_id, date_of_joining, department, salary, title):
        super().__init__(ID, name, address, phone_number, email_id, date_of_joining, department, salary)
        self.title = title

    @classmethod
    def read_data(cls):
        ID, name, address, phone_number, email_id = Person.read_data()
       


def menu():
    print("\nPlease choose an option:")
    print("1. Add a Student Details")
    print("2. Add a Faculty Details")
    print("3. Add a Staff Details")
    print("4. Exit")

def add_student_details():
    student = Student.read_data()
    output = student.output_data()
    print("\nAdded student details:")
    print(output)
    with open("Student.txt", "a") as file:
        file.write(output + "\n")

def add_faculty_details():
    faculty = Faculty.read_data()
    output = faculty.output_data()
    print("\nAdded faculty details:")
    print(output)
    with open("Faculty.txt", "a") as file:
        file.write(output + "\n")

def add_staff_details():
    staff = Staff.read_data()
    output = staff.output_data()
    print("\nAdded staff details:")
    print(output)
    with open("Staff.txt", "a") as file:
        file.write(output + "\n")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student_details()
        elif choice == "2":
            add_faculty_details()
        elif choice == "3":
            add_staff_details()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
