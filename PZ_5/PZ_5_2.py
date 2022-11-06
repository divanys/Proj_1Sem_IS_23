def inp():  # Функция обработки исключения
    a = input('Введите сторону треугольника (число): ')
    while type(a) != int:
        try:
            a = int(a)
            if a <= 0:
                a = input('Введите сторону треугольника (число): ')
        except ValueError:
            a = input('Введите сторону треугольника (число): ')
    return a


def TrianglePS(a):
    P = 3 * a
    S = a ** 2 * ((3 ** (1 / 2)) / 4)

    return P, S  # Возврат периметра и площади


print('1')
P1, S1 = TrianglePS(inp())  # Трёхкратный вызов функции
print('2')
P2, S2 = TrianglePS(inp())
print('3')
P3, S3 = TrianglePS(inp())

print('n', '       P', '                                    ', 'S')
print('1', '     =', P1, ' ' if P1 < 10 else '', '                                ', '=', round(S1, 3))
print('2', '     =', P2, ' ' if P2 < 10 else '', '                                ', '=', round(S2, 3))
print('3', '     =', P3, ' ' if P3 < 10 else '', '                                ', '=', round(S3, 3))
