# * 4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь, ключи — первые буквы фамилий, значения — словари, реализованные по схеме 
# предыдущего задания.
d = "Иван Сергеев, Инна Серова, Петр Алексеев,Илья Иванов, Анна Савельева, Юнона Ветрякова,Борис Аркадьев,Антон Серов,Павел Анисимов"
k = lambda e,a: [i for i in a if i[1][0] == e]
k2 = lambda x,y: [i for i in y if i[0][0] == x]
def creat_dict(txt):
    lst = txt.split(',')
    lst1 = [i.split() for i in lst]
    lst2 = list(set([i[1][0] for i in lst1]))
    d3 = {}
    for el in lst2:
        sp = k(el,lst1)
        sp1 = list(set([i[0][0] for i in sp]))
        d = {}
        for el1 in sp1:
            sp2 = k2(el1,sp)
            d[el1] = sp2
        d3[el] = d
    return d3
print(creat_dict(d))