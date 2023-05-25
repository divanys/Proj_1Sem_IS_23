# Создайте класс "Автомобиль", который содержит информацию о марке, модели и
# годе выпуска. Создайте класс "Грузовик", который наследуется от класса
# "Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
# "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
# информацию о количестве пассажиров.

class Automobile:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Truck(Automobile):
    def __init__(self, brand, model, year, payload_capacity):
        super().__init__(brand, model, year)
        self.payload_capacity = payload_capacity

class Car(Automobile):
    def __init__(self, brand, model, year, passenger_capacity):
        super().__init__(brand, model, year)
        self.passenger_capacity = passenger_capacity

# Пример использования классов
car1 = Car("Toyota", "Corolla", 2020, 5)
print(car1.brand)  # Вывод: Toyota
print(car1.model)  # Вывод: Corolla
print(car1.year)  # Вывод: 2020
print(car1.passenger_capacity)  # Вывод: 5

truck1 = Truck("Volvo", "FH16", 2019, 20000)
print(truck1.brand)  # Вывод: Volvo
print(truck1.model)  # Вывод: FH16
print(truck1.year)  # Вывод: 2019
print(truck1.payload_capacity)  # Вывод: 20000
