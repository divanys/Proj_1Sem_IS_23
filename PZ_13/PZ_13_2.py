# Из матрицы сформировать массив из положительных чётных элементов, найти их сумму и среднее арифметическое.


from random import randint

row = randint(2, 6)  # создаём количество строк и столбиков рандомным числом
column = randint(2, 6)

matrix = [[(randint(-10, 10)) for _ in range(row)] for i in range(column)]

print("Вывод 1 матрицы:")

for i in matrix:
    print(*i, sep='\t')  # Вывод 1 матрицы

positiveChetList = []

print('*****************************')
for i in matrix:
    for j in i:
        if j > 0 and j % 2 == 0:  # положительные чётные элементы
            positiveChetList.append(j)

print("массив из положительных чётных элементов: ", positiveChetList)

try:
    print('сумма: ', sum(positiveChetList), 'среднее арифметическое: ', sum(positiveChetList) / len(positiveChetList))
except:
    print("В матрице не имеются положительные чётные элементы")
