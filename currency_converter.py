import json
import argparse
import requests

class CurrencyConverter:
    """ Class CurrencyConverter for kiwi task """

    symbols = {
        '$': 'USD',
        '€': 'EUR',
        '£': 'GBP',
        '₽': 'RUB',
        '¥': 'CNY',
        '₣': 'CHF'
    }

    def __init__(self):
        self.rates = self.get_rates()

    def get_rates(self):
        """ Get rates from Skypicker api """

        r = requests.get('https://api.skypicker.com/rates')
        r.raise_for_status()
        return r.json()

    def calc(self, amount, from_currency, to_currency):
        """ Calculate from one currency to another """

        return round(amount * (self.rates[from_currency] / self.rates[to_currency]), 2)

    def available_currency_codes(self):
        """ Return list of available currency codes """

        return list(self.rates)

    def check_currency(self, code):
        """ Check if currency code or symbol exist, if not raise ValueError """

        if code in self.available_currency_codes():
            return code

        if code in self.symbols:
            return self.symbols[code]

        allcodes = ', '.join(self.available_currency_codes())
        raise ValueError(f'Wrong code: \'{code}\'.\nAvailable codes: {allcodes}.')

    def convert(self, input_currency, amount, output_currency = None):
        """
            Convert input currency with amount to output currency
            If output_currency == None then convert to all available currencies
        """

        input_currency = self.check_currency(input_currency)
        amount = float(amount)

        data = {}
        data['input'] = {
            'currency': input_currency,
            'amount': amount
        }

        if output_currency == None:
            data['output'] = {key: self.calc(amount, input_currency, key) \
                                    for key, val in self.rates.items() \
                                    if input_currency != key}
        else:
            output_currency = self.check_currency(output_currency)
            data['output'] = {
                output_currency: self.calc(amount, input_currency, output_currency)
            }

        return json.dumps(data);


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Kiwi currency converter')
    parser.add_argument('--input_currency', dest='input_currency',
                        action='store', type=str, required=True,
                        help='3 letters name (ISO 4217) or currency symbol')
    parser.add_argument('--amount', dest='amount',
                        action='store', type=float, required=True,
                        help='amount which we want to convert')
    parser.add_argument('--output_currency', dest='output_currency',
                        action='store', type=str,
                        help='3 letters name (ISO 4217) or currency symbol')

    args = parser.parse_args()

    response = {}
    try:
        converter = CurrencyConverter()
        response = converter.convert(args.input_currency, args.amount, args.output_currency)
    except (ValueError, TypeError, requests.exceptions.RequestException) as e:
        response = e

    print(response)
