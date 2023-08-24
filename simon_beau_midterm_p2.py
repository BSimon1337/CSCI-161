'''
Beau Simon
CSCI L02
Midterm Part II
Online Student - 0869416
'''

import math

# Prompt user to enter an integer value for degrees
degrees = int(input("Enter the number of degrees: "))

# Convert degrees to radians using the radians() function from the math module
radians = math.radians(degrees)

# Calculate the cosine of the radians using the cos() function from the math module
cosine = math.cos(radians)

# Print out the degrees, radians, and cosine value
print(f"Degrees: {degrees} ({type(degrees)}, id={id(degrees)})")
print(f"Radians: {radians} ({type(radians)}, id={id(radians)})")
print(f"Cosine: {cosine} ({type(cosine)}, id={id(cosine)})")
