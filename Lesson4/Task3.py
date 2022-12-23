# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.
from random import randint


def Creat_list():
    lst = []
    n = 7
    for i in range(n):
        x = randint(9,15)
        lst.append(x)
    return lst
def unicum_val(l):
    new_list = []
    for i in range(len(l)):
        if not l.count(l[i]) > 1:
            new_list.append(l[i])
    return new_list
lst = Creat_list()
print(lst)
lst1 = unicum_val(lst)
print(lst1)

