'''
Beau Simon
CSCI L02
Extra Credit Assignment 
Online Student - 0869416
'''

import tkinter as tk
from tkinter import filedialog

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def caesar_cipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_text += chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                decrypted_text += chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_caesar_cipher(ciphertext, crib_words):
    for shift in range(26):
        decrypted_text = caesar_cipher(ciphertext, shift)
        if all(crib_word in decrypted_text for crib_word in crib_words):
            return shift, decrypted_text
    return None

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    print("Select the ciphertext file")
    ciphertext_filename = filedialog.askopenfilename(title="Select the ciphertext file")
    print("Select the crib file")
    crib_filename = filedialog.askopenfilename(title="Select the crib file")

    ciphertext = read_file(ciphertext_filename)
    crib_words = read_file(crib_filename).split()

    result = brute_force_caesar_cipher(ciphertext, crib_words)

    if result:
        shift, decrypted_text = result
        print(f"\nDecrypted with a shift of {shift}:\n{decrypted_text}")
    else:
        print("No decryption with the provided crib words was found.")

if __name__ == "__main__":
    main()
