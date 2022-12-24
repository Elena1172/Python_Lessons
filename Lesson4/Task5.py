# 5. Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
# in
# "poly.txt"
# "poly_2.txt"
# out
# The contents of the files do not match!
from random import randint


def write_file(st):
    with open('Task05_1.txt', 'a') as r:
        r.write(st)


def write_file2(st):
    with open('Task05_2.txt', 'a') as r:
        r.write(st)


def creat_list(k):
    l = []
    for i in range(k + 1):
        l.append(randint(0, 11))
    return l


def creat_text(lst):
    wr = ''
    n = len(lst)
    if n < 2:
        wr = 'x = 0'
    else:
        for i in range(n):
            if i != n - 1 and i != n - 2 and lst[i] != 0:
                wr += f'{lst[i]}x^{n-i-1}'
                wr += ' + '
            elif i == n - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == n - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == n - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = randint(1, 9)
n = randint(2, 3)
for i in range(n):
    s = creat_list(k)
    t = creat_text(s)
    write_file(t + '\n')
for i in range(n):
    s = creat_list(k)
    t = creat_text(s)
    write_file2(t + '\n')
with open('Task05_1.txt') as rt:
    r1 = rt.readlines()
with open('Task05_2.txt') as rt:
    r2 = rt.readlines()
if len(r1) == len(r2):
    with open('Task05_3.txt', 'a') as wrtt:
        for i in range(len(r1)):
            s = r1[i].replace('= 0', ' + ') 
            s = s.replace('\n','') + r2[i]
            wrtt.write(s)
else:
    print('Файл заполнить невозможно')
