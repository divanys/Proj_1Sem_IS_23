try:  # обработка исключений
    v = int(input('Enter the speed in standing water as v (km/h): '))  # значение скорости в стоячей воде
    u = int(input('Enter the speed of the river flow as u (km/h): '))  # значение скорости течения реки
    t1 = int(input(
        'Enter the first time as t1 (in standing water, hours): '))  # значение времени движения по стоячей воде(озеру)
    t2 = int(input('Enter the second time as t2 (in river flow, hours): '))  # значение времени движения против реки
    s = v * t1 + (v - u) * t2
    print('The path is equal to', s, 'km.')  # выводим результат переменной
except:
    print('Incorrect data!')  # если введены неверный тип данных, выводим ошибку
