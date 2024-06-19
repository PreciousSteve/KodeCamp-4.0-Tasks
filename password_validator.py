# Design functions to:
# Ensure password length meets a minimum requirement.
# Verify presence of uppercase, lowercase, digits, and special characters.
# Optionally, check against a list of common weak passwords

import re

# i used re because re (regular expression) specifies a set of strings that matches it; 
# the functions in re module let you check if a particular string matches a given regular expression 
# (or if a given regular expression matches a particular string, which comes down to the same thing).

def valid_password(password, min_length=8, common_passwords=[]):
    """
    Check password length, strength, and presence in a list of common weak passwords.
    
        password (str): The password to check.
        min_length (int): The minimum length required. Defaults to 8.
        common_passwords (list): A list of common weak passwords. Defaults to an empty list.
    
    Returns:
        bool: True if password meets all requirements, False otherwise.
    """
    if len(password) < min_length:
        return False
    # r"[A-Z]" is a regular expression pattern that matches any uppercase letter from A to Z.
    # password is the string being searched.
    if not re.search(r"[A-Z]", password):
        return False
    # r"[A-Z]" is a regular expression pattern that matches any lowercase letter from a to z.
    # password is the string being searched.
    if not re.search(r"[a-z]", password):
        return False
    #  r"\d" is a regular expression pattern that matches any digit from 0 to 9
    if not re.search(r"\d", password):
        return False
    #  r"\W" is a regular expression pattern that matches any special character.
    if not re.search(r"\W", password):
        return False
    if password in common_passwords:
        return False
    return True


