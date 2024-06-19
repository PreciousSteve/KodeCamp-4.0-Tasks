# Build a script that prompts the user for the amount, input and output currencies,
# and displays the converted amount.

from currency_converter import get_exchange_rates, convert_currency, format_output, convert_and_format

amount = int(input("Enter the amount: "))
from_currency = input("Enter the input currency (USD, EUR, GBP): ").upper()
to_currency = input("Enter the output currency (USD, EUR, GBP): ").upper()

result = convert_and_format(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result}")
