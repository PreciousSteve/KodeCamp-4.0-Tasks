#  Ask the user for a number and generate the multiplication table for that number.

def multiplication_table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")


num = int(input("Enter a number: "))
multiplication_table(num)

