# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
from random import randrange


def creat_list(n):
    return list(range(n))


def shuffle_list(m):
    n = len(m)
    for i in range(n//2):
        j = randrange(n)
        m[i], m[j] = m[j], m[i]
    return m

while True:
    n = int(input('N = '))
    v = creat_list(n)
    print(v)
    print(shuffle_list(v))
