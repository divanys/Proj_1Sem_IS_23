#Создайте класс «Список», который имеет методы
# для добавления и удаления элементов,
# поиска элемента и сортировки списка.
# Создать экземпляр класса и выполнить в нем следующие действия:
# 1. Заполнить список 15 случайными числами
# 2. Проверить наличие в списке элемента со значением 2
# и удалить его из списка
# 3. Выполнить сортировку оставшихся элементов
# Результаты работы показывать в консоль.


import random

class MyList:
    def __init__(self):
        self.data = []
    
    def add_element(self, element):
        self.data.append(element)
    
    def remove_element(self, element):
        if element in self.data:
            self.data.remove(element)
    
    def search_element(self, element):
        return element in self.data
    
    def sort_list(self):
        self.data.sort()
    
    def print_list(self):
        print(self.data)

# Создание экземпляра класса "Список"
my_list = MyList()

# Заполнение списка 15 случайными числами
for _ in range(15):
    my_list.add_element(random.randint(1, 10))

# Вывод содержимого списка
print("Исходный список:")
my_list.print_list()

# Проверка наличия элемента со значением 2 и его удаление
if my_list.search_element(2):
    my_list.remove_element(2)

# Вывод содержимого списка после удаления элемента
print("Список после удаления элемента со значением 2:")
my_list.print_list()

# Сортировка списка
my_list.sort_list()

# Вывод содержимого отсортированного списка
print("Отсортированный список:")
my_list.print_list()