# Вариант 3. Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти максимальные продажи по
# каждому виду продукции, результаты вывести на экран.


string1 = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
lst1 = list(string1.split(' '))  # Разбиваем данную нам по условию строку на отдельные слова и значения
lst2 = []
futKeys = []
dictionary = {}  # Создаём 2 списка - значения для названий товаров - и пустой словарь

for i in lst1:
    if i.isalpha():
        lst2.append(lst1.index(i))
        futKeys.append(i)  # если в строке есть ключ (название продукта), то берем его id и само название

for i in range(len(lst2)):  # добавление в словарь ключа-названия товара и список проданных товаров
    if lst2[i] == lst2[-1]:
        dictionary[futKeys[i]] = [int(lst1[j]) for j in range(lst2[i] + 1, len(lst1))]
    else:
        dictionary[futKeys[i]] = [int(lst1[p]) for p in range(lst2[i] + 1, lst2[i + 1])]

lst3 = []
for key, value in dictionary.items():  # Вывод каждого словаря
    lst3.append(key)
    print(f'{len(lst3)}-й словарь: \n{key}: {value}\n')

for key, value in dictionary.items():  # Вывод максимального значения каждого списка и его id в списке в день продажи
    print(f"{key} продались лучше всего в {value.index(max(value)) + 1}-й день - {max(value)} кг.")
