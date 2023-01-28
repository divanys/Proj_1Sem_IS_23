# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.

from random import randint

row = randint(2, 6)  # создаём количество строк рандомным числом
column = row  # матрица квадратная, значит количество строк и колонок равные

matrix = [[(randint(-10, 10)) for _ in range(row)] for i in range(column)]

print("Вывод 1 матрицы:")

for i in matrix:
    print(*i, sep='\t')  # Вывод 1 матрицы


print('*********************************')


for i in range(row):
    for j in range(column):
        if i == j:
            matrix[i][j] = matrix[i][j] ** 2  # на главной диагонали увеличить в 2 раза

print("Вывод 2 матрицы:")

for i in matrix:
    print(*i, sep='\t')  # Вывод 2 матрицы
