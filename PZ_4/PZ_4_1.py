price = input('Введите стоимость 1 кг конфет(руб): ')  # ввод значения суммы

while type(price) != float:  # Обработка исключений
    try:
        price = float(price)
        if price > 0:
            continue
        price = input('Введите стоимость 1 кг конфет(руб): ')
    except ValueError:
        price = input('Введите стоимость 1 кг конфет(руб): ')

price2 = 0

for _ in range(1, 11):
    price2 += price
    print(f'Стоимость {_} кг конфет равна {price2} рублей')
