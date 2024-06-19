# Utilize the built-in requests module to fetch real-time exchange rates from an API.
# Create functions to:
# Convert an amount from one currency to another.
# Format the output for readability (e.g., include currency symbols).
# Construct a module named currency_converter.py.


import requests
import json

# Define the API endpoint and your API key
API_URL = "https://v6.exchangerate-api.com/v6/3281061ae70bf2b65dcc6dc6/latest/"

def get_exchange_rates():
    r = requests.get(API_URL)
    data = json.loads(r.text)
    return data['rates']

def convert_currency(amount, from_currency, to_currency):
    exchange_rates = get_exchange_rates()
    if from_currency != 'USD':
        amount = amount / exchange_rates[from_currency]
    return amount * exchange_rates[to_currency]

def format_output(amount, currency):
    symbol = ''
    if currency == 'USD':
        symbol = '$'
    elif currency == 'EUR':
        symbol = '€'
    elif currency == 'GBP':
        symbol = '£'
    return f'{symbol}{amount:.2f}'

def convert_and_format(amount, from_currency, to_currency):
    converted_amount = convert_currency(amount, from_currency, to_currency)
    return format_output(converted_amount, to_currency)

