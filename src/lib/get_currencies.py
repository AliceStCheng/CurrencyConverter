from forex_python.converter import CurrencyRates

class GetCurrencies:
    
    def __init__(self, currencyFrom, currencyTo):
        self.currencyFrom = currencyFrom
        self.currencyTo = currencyTo
  
    def convertAmount(self, amount):
        c = CurrencyRates()
        return c.convert(self.currencyFrom, self.currencyTo, amount)
 
    def getCurrentRate(self):
        c = CurrencyRates()
        return c.get_rate(self.currencyFrom, self.currencyTo)
