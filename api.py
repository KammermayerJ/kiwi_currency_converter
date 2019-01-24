from flask import Flask, request, jsonify
from currency_converter import CurrencyConverter
import requests

app = Flask(__name__)

@app.route('/currency_converter', methods=['GET'])
def index():

    input_currency = request.args.get('input_currency')
    amount = request.args.get('amount')
    output_currency = request.args.get('output_currency')

    try:
        converter = CurrencyConverter()
        return converter.convert(input_currency, amount, output_currency)
    except (ValueError, TypeError, requests.exceptions.RequestException) as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run()
