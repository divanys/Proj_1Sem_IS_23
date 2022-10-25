n = input('Введите целое число: ')  # ввод значения суммы

while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
        if n <= 0:
            n = input('Введите целое число: ')
            continue
    except ValueError:
        n = input('Введите целое число: ')

k = 0  # Обозначение счётчика и необходимых параметров для вычислений
long = len(str(n))
mod = 10
div = 1

for _ in range(long):  # Поочерёдное нахождение разрядов числа
    num = n % mod
    num = num // div
    if int(num) == 2:
        k += 1
        num = 0
    mod *= 10
    div *= 10

print(True if k >= 1 else False)
