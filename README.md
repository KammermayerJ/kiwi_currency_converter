# Currency converter - KIWI task

## Junior Python Developer (Data&Automation Team)

## Requires
- python 3.7
- pipenv
- requests
- flask

## Instalation packages via pipenv
```
pipenv install
```

## Parameters
- `amount` - amount to convert - float
- `input_currency` - 3 letters name or currency symbol
- `output_currency` - 3 letters name or currency symbol

### Available currency symbols
```
$ => USD
€ => EUR
£ => GBP
₽ => RUB
¥ => CNY
₣ => CHF
```

## Examples

### CLI 
```
./currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK
{   
    "input": {
    	"currency": "EUR",
        "amount": 100.0,        
    },
    "output": {
        "CZK": 2572.62, 
    }
}
```
```
./currency_converter.py --amount 0.9 --input_currency ¥ --output_currency AUD
{   
    "input": {
    	"currency": "CNY",
        "amount": 0.9        
    },
    "output": {
        "AUD": 0.19, 
    }
}
```
```
./currency_converter.py --amount 10.92 --input_currency £ 
{
    "input": {
    	"currency": "GBP",
        "amount": 10.92       
    },
    "output": {
    	"DZD": 1689.99, 
    	"NAD": 197.26, 
    	"GHS": 69.97,
        .
        .
        .
    }
}
```
### API
Run server by `./api.py`
Server is runnig on http://127.0.0.1:5000/

```
GET /currency_converter?amount=0.9&input_currency=¥&output_currency=AUD
{   
    "input": {
    	"currency": "CNY",
        "amount": 0.9        
    },
    "output": {
        "AUD": 0.19, 
    }
}
```

```
GET /currency_converter?amount=10.92&input_currency=£
{
    "input": {
    	"currency": "GBP",
        "amount": 10.92 
    },
    "output": {
    	"DZD": 1689.99, 
    	"NAD": 197.26, 
    	"GHS": 69.97,
        .
        .
        .
    }
}
```
### API wrong currency code/symbol
```
GET currency_converter?amount=5&input_currency=CZK&output_currency=USX
{
	"status":"error",
	{"message":"Wrong code: USX. Available codes: DZD, NAD, GHS, EGP, ..."}
}
```

### Test
File `test_converter.py` for basic tests