#  4. Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
from random import randint


def write_file(st):
    with open('Task_04.txt', 'a') as r:
        r.write(st)


def creat_sps(k):
    ls = []
    for i in range(k + 1):
        ls.append(randint(0, 11))
    return ls


def creat_str(lst):
    wrt = ''
    n = len(lst)
    for i in range(n):
        if i != n - 1 and i != n-2 and lst[i] != 0:
            wrt += f'{lst[i]}x^{n-i-1}'
            wrt += ' + '
        elif i == n - 2 and lst[i] != 0:
            wrt += f'{lst[i]}x'
            if lst[i+1] != 0:
                wrt += ' + '
        elif i == n - 1 and lst[i] != 0:
            wrt += f'{lst[i]} = 0'
        elif i == n - 1 and lst[i] == 0:
            wrt += ' = 0'
    return wrt
k = randint(2,10)
for i in range(3):
    s = creat_sps(k)
    st = creat_str(s)
    write_file(st+'\n')

