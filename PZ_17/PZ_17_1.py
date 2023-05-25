# Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения.

class Counter:
    def __init__(self):
        self.value = 0  # начальное значение счетчика

    def increment(self):
        self.value += 1

    def decrement(self):
        if self.value > 0:
            self.value -= 1

# Пример использования класса "Счетчик"
counter = Counter()
print(counter.value)  # Вывод: 0

counter.increment()
counter.increment()
print(counter.value)  # Вывод: 2

counter.decrement()
print(counter.value)  # Вывод: 1
