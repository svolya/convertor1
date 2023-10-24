from online import get_currencies



 # 1. Приветствие
print('программа конвертер валют!')

# 2. Мануал - как пользоватся программой.
print(("""
Для работы с программой требуется:
- выбрать исходную валюту 
- выбрать в какую валюту следует перевести
- ввести количество исходной валюты
"""))
def convert(amount, from_ticker, to_ticker,currencies):
    from_currency = currencies.get(from_ticker)
    to_currency = currencies.get(to_ticker)

    coefficient = to_currency / from_currency
    return round(amount * coefficient, 2)


def input_currency(input_message, current_currencies):
    ticker = input(f"{input_message}: ").upper()

    currency = current_currencies.get(ticker, None)
    if currency is None:
        print(f'ошибка при вводе валюты: {ticker}')
        exit()

    return ticker
current_currencies = get_currencies()

# 3. Ввести исходную валюту
from_ticker = input_currency("введите исходную валюту ",
                                            current_currencies)

# 4. ввести в какую валюту перевести
to_ticker = input_currency("введите в какую  валюту перевести ",
                                        current_currencies)

# 5. количество валюты для перевода
def input_amount():
    while True:
        try:
            amount = float(input("введите количество валюты: "))
          #  type(amount) != str
            result = convert(amount, from_ticker, to_ticker, current_currencies)
            print(f'Результат: {amount} {from_ticker} = {result} {to_ticker}')
            go_back = int(input('Хотите продолвить? ДА = 1 / НЕТ = 2 :  '))
            if go_back == 1:
                input_amount()
            else:
                exit()

        except ValueError as error:

            print(f'Ошибка ввода!')
            input_amount()

input_amount()

