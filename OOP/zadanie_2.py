# Николаю требуется проверить, возможно ли из представленных
# отрезков условной длины сформировать треугольник. Для этого
# он решил создать класс TriangleChecker, принимающий только 
# положительные числа. С помощью метода is_triangle()
# возвращаются следующие значения (в зависимости от ситуаций)
# -Ура, можно построить треугольник!
# -С отрицательными числами ничего не выйдет!
# -Нужно вводить только числа!
# -Жаль, но из этого треугольник не сделать

class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = (a, b, c)

    def is_num(n):
        return isinstance(n, float) or isinstance(n, int)

    def is_triangle(self):
        if not all(map(TriangleChecker.is_num, self.sides)):
            return 'Нужно вводить только числа!'
        elif not all(map(lambda x: x > 0, self.sides)):
            return 'С отрицательными числами ничего не выйдет!'
        if max(self.sides) < sum(self.sides) / 2:
            return 'Ура, можно построить треугольник!'
        else:
            return 'Жаль, но из этого треугольник не сделать.'

g = TriangleChecker(7, 7, 7)
print(g.is_triangle())
 
e = TriangleChecker(-3, 2, 3)
print(e.is_triangle())
 
r = TriangleChecker(10, 5, 4)
print(r.is_triangle())
 
k = TriangleChecker('v', 'j', 'a')
print(k.is_triangle())