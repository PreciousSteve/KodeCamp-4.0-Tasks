# Create a program that generates a random password based on user-specified criteria (length, inclusion of special characters, etc.).

import random
import string


def generate_password(length, special_chars, use_numbers):
    characters = string.ascii_letters
    if special_chars:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


length = int(input("Enter password length: "))
special_chars = input("Include special characters? (y for yes /n for no): ").lower() == 'y'
use_numbers = input("Include numbers? (y for yes/n for no): ").lower() == 'y'

print(" Your generated Password is: ", generate_password(length, special_chars, use_numbers))
