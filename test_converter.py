import unittest
from currency_converter import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.converter = CurrencyConverter()

    def test_rates_exist(self):
        self.assertTrue(self.converter.rates)
        self.assertTrue(self.converter.available_currency_codes())

    def test_calc(self):
        self.assertEqual(self.converter.calc(100, 'USD', 'USD'), 100)

    def test_codes(self):
        self.assertEqual(self.converter.check_currency('USD'), 'USD')
        self.assertEqual(self.converter.check_currency('CZK'), 'CZK')

    def test_symbols(self):
        for symb, code in self.converter.symbols.items():
                self.assertEqual(self.converter.check_currency(symb), code)

    def test_wrong_code(self):
        self.assertRaises(ValueError, self.converter.check_currency, 'CZR')
        self.assertRaises(ValueError, self.converter.check_currency, '')
        self.assertRaises(ValueError, self.converter.check_currency, '*')

    def test_convert(self):
        self.converter.rates = {
            'EUR': 1,
            'USD': 0.885015,
            'CZK': 0.0388622
        }
        
        result = self.converter.convert('EUR', 1, None)
        inside = ['currency', 'EUR', 'amount', '1.0', 'output', 'USD', '1.13', 'CZK', '25.73']
        for s in inside:
            self.assertIn(s, result)

        result2 = self.converter.convert('EUR', 1, 'CZK')
        inside = ['currency', 'EUR', 'amount', '1.0', 'output', 'CZK', '25.73']
        for s in inside:
            self.assertIn(s, result2)

if __name__ == '__main__':
    unittest.main()
