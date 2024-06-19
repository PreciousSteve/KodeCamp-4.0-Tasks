# Import the built-in random module for generating random characters.
# Design functions to:
# Generate a random password of a specified length.
# Ensure the password meets complexity requirements (uppercase, lowercase, digits, symbols).
# Combine these into a module named password_generator.py.

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def meet_complexity_requirements(password):
    requirements = [
        lambda s: any(x.isupper() for x in s),  # have at least one uppercase letter
        lambda s: any(x.islower() for x in s),  # have at least one lowercase letter
        lambda s: any(x.isdigit() for x in s),  # have at least one digit
        lambda s: any(x in string.punctuation for x in s)  # have at least one symbol
    ]
    return all(req(password) for req in requirements)

def generate_password_with_complexity(length):
    password = generate_password(length)
    while not meet_complexity_requirements(password):
        password = generate_password(length)
    return password

