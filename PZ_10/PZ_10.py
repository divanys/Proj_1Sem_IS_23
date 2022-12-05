# Вариант 3.
# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин. Определить:
# 1. Полный список всех книг магазинов.
# 2. Какие книги есть во всех магазинах.
# 3. Хотя бы одну книгу, которая есть не во всех магазинах.


lst2BookAndMarket = []
# Разбиваем строку на отдельные элементы типа (название: содержание)
lstBookAndMarket = list(
    "Магистр – Лермонтов, Достоевский, Пушкин, Тютчев. ДомКниги – Толстой, Грибоедов, Чехов, Пушкин."
    " БукМаркет – Пушкин, Достоевский, Маяковский. Галерея – Чехов, Тютчев, Пушкин".split('. '))

for _ in lstBookAndMarket:  # Вывод данного списка.
    lst2BookAndMarket.append(_.split(" – "))

# Каждому магазину присваиваем свой список книг, но в виде множества
Magistr = set(lst2BookAndMarket[0][1].split(', '))
DomKnigi = set(lst2BookAndMarket[1][1].split(', '))
BookMarket = set(lst2BookAndMarket[2][1].split(', '))
Galereya = set(lst2BookAndMarket[3][1].split(', '))
print('-----------------------------------------------------------',
      "Полный список книг во всех магазинах (ассортимент): ",
      f"Магистр: {Magistr}",
      f"ДомКниги: {DomKnigi}",
      f"БукМаркет: {BookMarket}",
      f"Галерея: {Galereya}",
      '-----------------------------------------------------------', sep='\n')

# Список книг, имеющихся во всех магазинах
print("Список книг, имеющихся во всех магазинах:\n",
      f"{Magistr & DomKnigi & BookMarket & Galereya}\n",
      "-----------------------------------------------------------")

# Список книг, встречающихся только 1 раз
print("Список книг, встречающихся только 1 раз в магазинах:\n",
      f"{Magistr ^ DomKnigi ^ BookMarket ^ Galereya}\n",
      '-----------------------------------------------------------')
