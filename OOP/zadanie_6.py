# Создайте класс «Прямоугольник» с атрибутами длины и ширины.
# Добавьте методы для вычисления площади и периметра.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
# Создание объекта "Прямоугольник" с длиной 5 и шириной 3
rectangle = Rectangle(5, 3)

# Вычисление площади
area = rectangle.calculate_area()
print("Площадь: ", area)  # Выводит: Площадь: 15

# Вычисление периметра
perimeter = rectangle.calculate_perimeter()
print("Периметр: ", perimeter)  # Выводит: Периметр: 16