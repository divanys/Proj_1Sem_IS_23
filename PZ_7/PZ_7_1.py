# Дан символ C. Вывести два символа, первый из которых предшествует символу C в
# кодовой таблице, а второй следует за символом C.

def inp():  # Обработки исключений нет, так как вводится любой символ. Обработка количества введённых символов
    b = input('Введите любой 1 символ: ')
    while len(b) != 1:
        b = input('Введите любой 1 символ: ')
    return b


a = inp()  # для удобства присваиваем значение функции в переменную


def symbols():  # функция, вычисляющая, какие символы стоят до и после введённого символа
    lst = [chr(ord(a) - 1), chr(ord(a) + 1)]  # Функция ord(c) возвращает числовое значение для заданного символа.
    return lst


# вывод символов с пояснением

print(f"Символ, предшествующий введённому символу, {symbols()[0]} "
      f"\nСимвол, следующий за введённым символом, {symbols()[1]}")
