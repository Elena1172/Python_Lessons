# 4. Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*
# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти
while True:
    n = input('Задайте номер четверти: ')
    if n == '1':
        print(f'{n} -> x > 0, y > 0')
    elif n == '2':
        print(f'{n} -> x < 0, y > 0')
    elif n == '3':
        print(f'{n}1 -> x < 0, y < 0')
    elif n == '4':
        print(f'{n} -> x > 0, y < 0')
    else:
        print('нет такой четверти')