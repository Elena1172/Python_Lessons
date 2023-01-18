##1. Представлен список чисел. Необходимо вывести элементы исходного
##списка, значения которых больше предыдущего элемента. Use comprehension.
##in
##9
##out
##[15, 16, 2, 3, 1, 7, 5, 4, 10]
##16, 3, 7, 10]
from random import randint
def creat_list(n:int):
    ls = []
    for i in range(n):
        ls.append(randint(-5,25))
    return ls
def filtr_List(lst):
    lst1 = [lst[i] for i in range(1,len(lst)) if lst[i] > lst[i-1]]
    return lst1
if __name__ == '__main__':
    nb = int(input('Введите натуральное число: '))
    if nb > 1:
        l = creat_list(nb)
        print(l)
        print(filtr_List(l))
    else:
        print ('Некорректный ввод данных')
