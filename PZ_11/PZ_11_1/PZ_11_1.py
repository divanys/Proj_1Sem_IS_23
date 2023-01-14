# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Квадраты четных элементов:
# Сумма квадратов четных элементов:
# Среднее арифметическое суммы квадратов четных элементов:

from random import randint

my_list = []   # Заполняем список рандомным количеством рандомных чисел.
for i in range(randint(5, 20)):
    my_list.append(str(randint(-10, 10)))

print(my_list)

new_file = open("filext.txt", "w+")   # Создаём файл, в который поместим список
new_file.writelines(' '.join(my_list))
new_file.close()

new_file = open("filext.txt", "r+")   # Считываем сам список из этого файла
list_1 = new_file.read().split(' ')
print(list_1)
new_file.close()

# создаём новый файл, в который заносим "Входные данные", "Количество элементов", "Минимальный элемент",
# "Квадраты чётных элементов", "Сумма квадратов чётных элементов", "Среднее арифметическое суммы квадратов чётных элементов".

new_file = open("filext.txt", "r+")
main_file = open("main.txt", "w+")

lenLst = []
for _ in range(len(list_1)):
    if int(list_1[_]) % 2 == 0:
        lenLst.append(int(list_1[_]) ** 2)

main_file.writelines(f"Исходные данные:  \n"
                     f"{' '.join(list_1)}\n\n"
                     f"Количество: \n"
                     f"{str(len(new_file.read()))}\n\n"
                     f"Минимальный элемент:  \n"
                     f"{str(min(int(i) for i in list_1))}\n\n"
                     f"Квадраты чётных элементов:  \n"
                     f"{' '.join(str(int(i)**2) for i in list_1 if int(i) % 2 == 0)}\n\n"
                     f"Сумма квадратов чётных элементов: \n"
                     f"{str(sum(lenLst))}\n\n"
                     f"Среднее арифметическое суммы квадратов чётных элементов: \n"
                     f"{str(sum(lenLst) / len(lenLst))}")

new_file.close()
main_file.close()