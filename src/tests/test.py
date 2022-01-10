from lib.get_currencies import *
import unittest

class TestGetCurrencies(unittest.TestCase):
    def test_convertAmount(self):        
        f = GetCurrencies('GBP', 'EUR')
        rate = f.convertAmount(1)
        self.assertAlmostEqual(rate, 1.2, 1, "Assert convertAmount")
    
    def test_convertAmount(self):        
        f = GetCurrencies('USD', 'EUR')
        rate = f.getCurrentRate()
        self.assertAlmostEqual(rate, 0.9, 1, "Assert getCurrentRate")
          

if __name__ == '__main__':
    unittest.main()
    
    