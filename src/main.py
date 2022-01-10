from lib.get_currencies import GetCurrencies
from decimal import Decimal

currencyFrom = input("Currency to convert from: ")
currencyTo = input("Currency to convert to: ")
amount = Decimal(input("Amount to convert: "))

c = GetCurrencies(currencyFrom, currencyTo, amount)
print(c.convertAmount())