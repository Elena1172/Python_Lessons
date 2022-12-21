# ** 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов. Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
def List_Fib(n):
    fib1 = 1
    fib2 = 1
    result = 0
    new_list = [-1,1, 0, fib1,fib2]
    for i in range(2,n):
            result = fib1 + fib2
            new_list.append(result)
            fib1 = fib2
            fib2 = result
            if i % 2 == 0:
                  new_list.insert(0, result)
            if not i % 2 == 0:
                  result *= -1
                  new_list.insert(0, result)
        
    return new_list

n = int(input('Введите число >1 для вывода списка Фибоначи '))
if n > 1:
      print (f' {n} -> {List_Fib(n)}')
else:
      print('Число задано неверно.')

