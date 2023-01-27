# Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать первую последовательность, содержащую
# числа кратные трем, и вторую – для всех остальных. Найти количество элементов в
# полученных последовательностях.

from random import randint

lstRandom = [randint(1, 100) for i in range(int(input("Введите количество чисел: ")))]  # создаём список с рандомными значениями
lstFor3 = list(filter(lambda x: x % 3 == 0, lstRandom))  # список со значениями, кратными 3
lstOther = list(filter(lambda x: x not in lstFor3, lstRandom))  # список с другими значениями
print("Случайная последовательность чисел:", lstRandom, "\n", "Кратные трём:", lstFor3, "их количество:", len(lstFor3), "\n", "Не кратны трём:", lstOther, "их количество:", len(lstOther))


# решение в 2 строки:
# lstRandom = [randint(1, 100) for i in range(int(input("Введите количество чисел: ")))]
# print("Случайная последовательность чисел:", lstRandom, "\n", "Кратные трём:", list(filter(lambda x: x % 3 == 0, lstRandom)), "их количество:", len(list(filter(lambda x: x % 3 == 0, lstRandom))), "\n", "Не кратны трём:", list(filter(lambda x: x % 3 != 0, lstRandom)), "их количество:", len(list(filter(lambda x: x % 3 != 0, lstRandom))))