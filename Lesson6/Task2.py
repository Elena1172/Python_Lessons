##2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21.
##Use comprehension.
##in
##100
##out
##[20, 21, 40, 42, 60, 63, 80, 84, 100]
def creat_list(n:int):
    ls = [i for i in range(20,n+1) if not i%20 or  not i%21]
    return ls
if __name__ == '__main__':
    number = int(input('Введите натуральное число больше 20 '))
    if number > 19:
        print(creat_list(number))
    else:
        print('Некорректный ввод данных')