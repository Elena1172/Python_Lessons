# Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.
def Number_Factorize(n):
    div = 2
    n_list = []
    while n > 1:
        if n % div == 0:
            n_list.append(div)
            n //= div
        else:
            div += 1
    return n_list
num = int(input('Задайте натуральное число: '))
if num > 0:
    lst = Number_Factorize(num)
    print(lst)
else:
    print("Неправильный ввод данных")