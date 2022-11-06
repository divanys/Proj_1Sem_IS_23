# Дан список размера N. Найти номер его первого локального минимума (локальный
# минимум — это элемент, который меньше любого из своих соседей).

from random import randint


def inp():  # Функция обработки исключения
    a = input('Введите размер списка: ')
    while type(a) != int:
        try:
            a = int(a)
            if a <= 0:
                a = input('Введите целое число: ')
        except ValueError:
            a = input('Введите целое число: ')
    return a


def minObj(predel):  # Функция со сравнением следующего и предыдущего элемента относительно текущего в списке
    lst = []
    for _ in range(predel):
        lst.append(randint(-10, 10))

    for _ in range(len(lst)):
        if lst[_] < lst[_ + 1] and lst[_] < lst[_ - 1]:
            numba = _ + 1
            return lst[_], lst, numba


# Вывод локального минимума и его идентификатора
LocMin, AllList, numb = minObj(inp())
print(f"Первый локальный минимум списка {AllList}: {LocMin} под номером {numb}")
