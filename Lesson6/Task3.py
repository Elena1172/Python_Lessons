##3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
##ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с
##соответствующей буквы.
##in
##"Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
##out
##{'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'],
## 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}
t = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
def creat_dict(lst):
    lst1 = list(set([i[0] for i in lst]))
    d = {}
    k = lambda x,y:[i for i in y if i[0] == x]
    for el in lst1:
        d[el] = k(el,lst)
    d = sorted(d.items(), key=lambda x: x[0])
    return d
if __name__ == '__main__':  
    print(creat_dict(t))
