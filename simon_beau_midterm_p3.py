'''
Beau Simon
CSCI L02
Midterm Part III
Online Student - 0869416
'''

def clamp(n):
    if n < 0:
        return 0
    elif n > 255:
        return 255
    else:
        return n

def main():
    n = int(input("Enter a number: "))
    result = clamp(n)
    print("Result:", result)

if __name__ == "__main__":
    main()
