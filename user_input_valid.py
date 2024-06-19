# 2. User Input Validation:

# Develop a program that repeatedly asks the user for input until valid data is entered. 
# Handle exceptions for invalid types, out-of-range values, and incorrect formats.
#
# I want to ask the user to input his phone number

import re

def valid_phone_num(prompt):
    while True:
        try:
            user_input = input(prompt)
            if not re.fullmatch(r'\d{11}', user_input):
                raise ValueError("Phone number must be exactly 10 digits.")            
            return user_input
        except ValueError:
            print(f"Invalid input: Input your correct phone number")
        except Exception:
            # Handle any other unexpected exceptions
            print(f"An error occurred")


print("Please enter a 10-digit phone number.")
valid_phone_number = valid_phone_num("Enter your phone number: ")
print(f"You have entered a valid phone number: {valid_phone_number}")



