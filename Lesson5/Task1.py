# 1. Напишите программу, удаляющую из текста все слова, содержащие "qwe". 
# В тексте используется разделитель пробел
from random import sample
def Creat_str(n:int):
    el = ['qwe','qew','wqe','weq','eqw','ewq']
    lst = sample(el,k = n,counts = [3,2,2,2,2,2])
    str = ' '.join(lst)
    return  str
def Remove_el(text,el):
    lst = text.split(' ')
    lst1 = [i for i in lst if i != el]
    text2 = ' '.join(lst1)
    return text2
n = int(input('Number of words: '))
if  14 > n > 0:
    s = Creat_str(n)   
    print (s)
    print(Remove_el(s,'qwe'))
else:
    print('The data is incorrect')



