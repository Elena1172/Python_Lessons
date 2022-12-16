# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и
# выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071
def creat_list(n):
    y = []
    for i in range(1,n+1):
        f = (1 + 1/i)**i
        y.append(round(f,3))
    return y
def sum(m):
    n = len(m)
    s = 0
    for i in range(n):
        s += m[i]
    return s
number = int(input("Введите число: "))
l = creat_list(number)
print(l)
print(f'{sum(l):.3f}')

