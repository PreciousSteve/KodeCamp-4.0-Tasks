# 1. Calculator with Error Handling:

# Enhance a basic calculator program to handle exceptions such as division by zero, 
# invalid input types (like strings instead of numbers), and unsupported operations


def divide(x, y):
    try:
        result = x / y
    except (ZeroDivisionError):
        print("Division by 0 cannot be possible")
    except (TypeError):
        return "Error: Invalid input. Both inputs must be numbers."
    else:
        return result
    

user_input1 = int(input("Enter your number: "))
user_input2 = int(input("Enter your number: "))

result = divide(user_input1, user_input2)

print(f"{user_input1} divided by {user_input2} is {result}")
    