# * 4. Задайте список из произвольных вещественных чисел, количество задаёт
# пользователь.Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36
from random import uniform


def Creat_list(n):
    lst = []
    for i in range(n):
        n = round(uniform(1, 21), 2)
        lst.append(n)
    return lst


def List_Value(l):
    n = len(l)
    lst = []
    max_val = l[0] % 1
    min_val = l[0] % 1
    for i in range(1, n):
        num = l[i] % 1
        if num > max_val:

            max_val = num
        if num < max_val and num < min_val:
            min_val = num
    max_val = round(max_val, 2)
    min_val = round(min_val, 2)
    num_def = max_val - min_val
    num_def = round(num_def, 2)
    lst.append(max_val)
    lst.append(min_val)
    lst.append(num_def)
    return lst


y = int(input('Введите количество элементов списка: '))
if y > 0:
    lst = Creat_list(y)
    lst1 = List_Value(lst)
    print(f'{lst} Min: {lst1[1]}, Max; {lst1[0]}, Difference: {lst1[2]} ')
else:
    print('Неправильно задано число')
