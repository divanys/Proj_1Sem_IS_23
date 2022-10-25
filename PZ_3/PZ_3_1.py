# print("Чётное" if int(input()) % 2 == 0 else "Нечётное") ======> решение в одну строку
try:
    a = input('Введите a: ')
    while type(a) != int:  # Обработка исключений try:
        a = int(a)
except ValueError:
    print('Вами введено не ЦЕЛОЕ число, попробуйте снова.')
    a = input('Введите a: ')
if a % 2 == 0:  # Проверка на чётность числа и вывод
    print('Чётное.')
else:
    print('Нечётное.')
