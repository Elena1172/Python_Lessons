# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
from random import randint


def Creat_list(n):
    lst = []
    for i in range(n):
        m = randint(1, 41)
        lst.append(m)
    return lst


def val_list(l):
    n = len(l)
    l1 = []
    for i in range(n//2):
        l1.append(l[0+i] * l[(n-1) - i])
    if not n % 2 == 0:
        l1.append(l[n//2])
    return l1

a = int(input('Введит5е количество элементов списка: '))
if a > 0:
    b = Creat_list(a)
    x = val_list(b)
    print(f'{b} -> {x}')
else:
    print('Неправильный ввод данных ')
