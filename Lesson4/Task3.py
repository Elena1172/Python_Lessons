# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.
from random import randint


def Creat_list(n):
    lst = []
    for i in range(n):
        x = randint(9,9+n-1)
        lst.append(x)
    return lst
def unicum_val(l):
    new_list = []
    for i in range(len(l)):
        if not l.count(l[i]) > 1:
            new_list.append(l[i])
    return new_list
n = int(input('Введите количество чисел в последовательности: '))
if n > 0:
    lst = Creat_list(n)
    print(lst)
    lst1 = unicum_val(lst)
    print(lst1)
else:
    print('Неправильный ввод данных')
