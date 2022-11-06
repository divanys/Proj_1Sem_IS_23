# Дан список размера N (N — четное число). Поменять местами его первый элемент со
# вторым, третий — с четвертым и т. д.


from random import randint


def inp():  # Функция обработки исключения
    a = input('Введите целое чётное число: ')
    while type(a) != int:
        try:
            a = int(a)
            if a <= 0 or a % 2 != 0:
                a = input('Введите целое чётное число: ')
        except ValueError:
            a = input('Введите целое чётное число: ')

    return a


def lst():
    lst1 = []
    for _ in range(inp()):
        lst1.append(randint(-10, 10))
    print(f'Список был: {lst1} \n---------------------------------')

    for _ in range(0, len(lst1), 2):
        lst1[_], lst1[_ + 1] = lst1[_ + 1], lst1[_]

    return lst1


print(f'Список стал: {lst()}')
