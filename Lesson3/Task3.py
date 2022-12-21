# 3. Напишите программу, которая будет преобразовывать десятичное число в
# двоичное.Без использования встроенной функции преобразования, без строк.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
def Numbe_Conversion(x):
    base = 2
    st = ''
    y = x
    if y < 0:
        y *= -1
    while y:
        dig = y % base
        st = str(dig) + st
        y //= base
    st = int(st)
    if x < 0:
        st *= -1
        return st
    return st


n = int(input('Введите целое число: '))
print(f'{n} -> {Numbe_Conversion(n) }')
