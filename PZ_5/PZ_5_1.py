def inp(num):  # Функция обработки исключения
    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            num = input('Введите число: ')
    return num


def sumList():  # Главная функция с интеграцией обработки исключений и проведением расчётов
    stopWord = '0'
    summa = 0
    while stopWord != '1':
        num = input('Введите число: ')
        num = inp(num)
        summa += num
        stopWord = input("Если не хотите вводить больше, пропишите 1, иначе нажмите Enter:   ")
    return summa  # Возврат суммы


print(f"Сумма числового ряда равна {sumList()}")
