# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
# корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
# 86532547891), а во второй с некорректными номерами телефонов. Посчитать
# полученные строки в каждом файле.

import re

nums = []
mask_nums = []
right_num = []
folse_num = []

with open("hotline.txt", "r+", encoding="utf-8") as file:  # Чтение файла
    string = file.read()

p = re.compile(r"8.*[0-9]")  # Создание шаблона для сортировки

num = p.findall(string)  # Нахождение элементов по шаблону
for i in range(len(num)):  # Обходом списка вычитаем все лишние элементы номеров
    for j in num[i]:
        if not j.isdigit():
            new_i = num[i].replace(j, '')
            num[i] = new_i

for i in num:  # С помощью проверки сортируем номера
    if len(i) == 11:
        right_num.append(i)
    elif len(i) != 11:
        folse_num.append(i)

with open("hotline.txt", "r+", encoding="utf-8") as file:  # Запись в файлы правильных и неправильных номеров
    with open("ПравильныеНомера.txt", 'w+', encoding="utf-8") as f1:
        for _ in right_num:
            f1.write(_)
            f1.write('\n')

    with open("НеправильныеНомера.txt", 'w+', encoding="utf-8") as f2:
        for _ in folse_num:
            f2.write(_)
            f2.write('\n')

print(f"\nСписок правильных номеров: \n{right_num} \nИх количество: {len(right_num)} \n\nСписок неправильных номеров: \n{folse_num} \nИх количество: {len(folse_num)}")  # Вывод
