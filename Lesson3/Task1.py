# 1. Задайте список, состоящий из произвольных чисел, количество задаёт
# пользователь.Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8
from random import randint


def Creat_List(n):
    l = []
    for i in range(n):
        m = randint(1, 31)
        l.append(m)
    return l
def sum_el(lst):
    n = len(lst)
    s = 0
    for i in range(0,n,2):
        s += lst[i]
    return s
n = int(input('Введите количество элементво списка: '))
if  n > 0:
    l = Creat_List(n)
    print (f'{l} -> {sum_el(l)}')
else:
    print('Неправильный ввод данных')
