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
def convert(amount, from_ticker, to_ticker,currencies): # обслуживание расчета
    from_currency = currencies.get(from_ticker)
    to_currency = currencies.get(to_ticker)

    coefficient = to_currency / from_currency
    return round(amount * coefficient, 2)


def input_currency(input_message, current_currencies):  # обслуживание ввода тикера валют
    ticker = input(f"{input_message}: ").upper()

    currency = current_currencies.get(ticker, None)
    if currency is None:
        print(f'ошибка при вводе валюты: {ticker}')
        exit()
    return ticker


def input_amount():  # обслуживание ввода количества денег на конвертацию
    while True:
        try:
            amount = float(input("введите количество валюты: "))
            result = convert(amount, from_ticker, to_ticker, current_currencies)
            print(f'Результат: {amount} {from_ticker} = {result} {to_ticker}')
            go_back = int(input('Хотите продолжить? ДА = 1 / НЕТ = 2 :  '))
            if go_back == 1:
                input_amount()
            else:
                exit()

        except ValueError:

            print(f'Ошибка ввода!')
            input_amount()
        return
# 3 Получение данных с интернета
current_currencies = get_currencies()

# 4. Ввести исходную валюту
from_ticker = input_currency("введите исходную валюту ",
                                            current_currencies)

# 5. Ввести в какую валюту перевести
to_ticker = input_currency("введите в какую  валюту перевести ",
                                        current_currencies)

# 6. Ввести количество денег
input_amount()

