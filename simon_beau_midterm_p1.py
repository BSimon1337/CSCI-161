'''
Beau Simon
CSCI L02
Midterm - Part I
Online Student - 0869416
'''

number = input("Enter a number: ")

# Recast the input string to an integer and a floating point number
integer_number = int(number)
float_number = float(number)

# Print the number as a string, as an integer, and as a float
print("As string: " + str(number))
print("As integer: " + str(integer_number))
print("As float: " + str(float_number))

# Use the type() function and the id() function to print out the type and id of each of the items printed
print("Type of string: " + str(type(number)) + ", id: " + str(id(number)))
print("Type of integer: " + str(type(integer_number)) + ", id: " + str(id(integer_number)))
print("Type of float: " + str(type(float_number)) + ", id: " + str(id(float_number)))
