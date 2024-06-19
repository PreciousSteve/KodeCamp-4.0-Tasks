# Develop a basic banking system where the user can deposit, withdraw, and check their balance.

initial_balance = 0
balance = initial_balance


# defining the functions
def deposit(amount, initial_balance = 0):
    balance = initial_balance
    balance += amount
    print(f"Deposited {amount}. New balance: {balance}")


def withdraw(amount, initial_balance = 0):
    balance = initial_balance
    if amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        print(f"Withdrew {amount}. New balance: {balance}")


def check_balance():
    print(f"Current balance: {balance}")


print("Please choose your desired option")
print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")

choice = input("Choose an option: ")


if choice == "1":
    amount = int(input("Enter amount to deposit: "))
    deposit(amount)
elif choice == "2":
    amount = int(input("Enter amount to withdraw: "))
    withdraw(amount)
elif choice == "3":
    check_balance()
else:
    print("Invalid option. Please try again")


