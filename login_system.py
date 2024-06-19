# Create a basic login system that checks username and password against a stored list. 
# Handle exceptions for invalid input, and locked accounts after multiple failed attempts


# Stored list of users
users = {
    "precious": {"password": "9188", "attempts": 0, "locked": False},
    "steve": {"password": "2001", "attempts": 0, "locked": False}
}

# Maximum allowed attempts
max_attempts = 3

def login(username, password):
    while True:
        try:
            # Checking if the user exists in the list
            if username in users:
            # Checking if account is locked
                if users[username]["locked"]:
                    raise Exception("Account is locked. Please try again later.")
            # Check password
                if password == users[username]["password"]:
                # Reseting attempts and return True
                    users[username]["attempts"] = 0
                    return True
                else:
                # Increment attempts and raise exception
                    users[username]["attempts"] += 1
                    if users[username]["attempts"] >= max_attempts:
                        users[username]["locked"] = True
                    raise Exception("Invalid password. Try again.")
            else:
                raise Exception("Invalid username. Try again.")
        except Exception:
            print("Error found")
        return False

username = input("Enter username: ")
password = input("Enter password: ")
if login(username, password):
    print("Login successful!")
else:
    print("Login failed. Please try again.")
