# 3. Напишите программу, которая принимает на вход координаты точки
# (X и Y),причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
while True:
    print('Введите поочередно координаты x и y (кроме 0)')
    x = int(input('x = '))
    y = int(input('y = '))
    if x > 0:
        if y > 0:
            print(f'x={x}; y={y} -> 1')
        else:
            print(f'x={x}; y={y} -> 4')
    elif x < 0:
        if y > 0:
            print(f'x={x}; y={y} -> 2')
        else:
            print(f'x={x}; y={y} -> 3')
    else:
        print('Некорректный ввод данных')