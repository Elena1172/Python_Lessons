# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20
def pr_pos(a, n1, n2):
    n = len(a)
    if 0 < n1 < n + 1 and 0 < n2 < n + 1:
        pr = a[n1-1]*a[n2 - 1]
        return pr
    else:
        return print("На указанных позициях элементов списка нет ")


def creat_list(n):
    l = list(range(-n, n+1))
    return l


number = int(input("N = : "))
l = creat_list(number)
pos1 = int(input("Position one: "))
pos2 = int(input("Position two: "))
print(l)
m = pr_pos(l, pos1, pos2)
if type(m) == type(5) or type(m) == type(5.5):
    print(m)
