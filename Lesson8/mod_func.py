import sqlite3 as s
def show_table():
    
    with s.connect('base.db') as bd:
        cur = bd.cursor()
        r = cur.execute('SELECT * FROM заказы').fetchall()
    print ('{0:3} {1:12} {2:17} {3:17} {4:14} {5:8} '.format ('ID','дата заказа','менеджер','клиент','товар','сумма'))
    for a,j,d,f,g,h in r:
        print ('{0:3} {1:12} {2:17} {3:17} {4:14} {5:8} '.format (a,j,d,f,g,h))
def show_table1():
    
    with s.connect('base.db') as bd:
        cur = bd.cursor()
        r = cur.execute('SELECT * FROM сотрудники').fetchall()
    print ('{0:3} {1:12} {2:10} {3:14} {4:15}'.format ('ID','фамилия','имя','дата рождения','должность'))
    for a,j,d,f,g in r:
        print ('{0:3} {1:12} {2:10} {3:14} {4:15}'.format (a,j,d,f,g))
def show_table2():
    
    with s.connect('base.db') as bd:
        cur = bd.cursor()
        r = cur.execute('SELECT * FROM клиенты').fetchall()
    print ('{0:3} {1:12} {2:10} {3:16} {4:10}'.format ('ID','фамилия','имя','номер телефона','e_maile'))
    for a,j,d,f,g in r:
        print ('{0:3} {1:12} {2:10} {3:16} {4:10}'.format (a,j,d,f,g))       
def add_data():
    n = input('ID ')
    n1 = input('Дата заказа ')
    n2 = input('Менеджер ')
    n3 = input('Клиент ')
    n4 = input('Товар ')
    n5 = input('Сумма ')
    with s.connect('base.db') as bd:
        cur = bd.cursor()
        cur.execute('INSERT INTO заказы VALUES(?,?,?,?,?,?)',(n,n1,n2,n3,n4,n5))
def add_data1():
    n = input('ID ')
    n1 = input('Фамилия ')
    n2 = input('Имя ')
    n3 = input('Дата рождения ')
    n4 = input('Должность ')
    with s.connect('base.db') as bd:
        cur = bd.cursor()
        cur.execute('INSERT INTO сотрудники VALUES(?,?,?,?,?)',(n,n1,n2,n3,n4))
def add_data2():
    n = input('ID ')
    n1 = input('Фамилия ')
    n2 = input('Имя ')
    n3 = input('Номер телефона ')
    n4 = input('e_mail ')
    with s.connect('base.db') as bd:
        cur = bd.cursor()
        cur.execute('INSERT INTO клиенты VALUES(?,?,?,?,?)',(n,n1,n2,n3,n4))
def del_data():
    n1 = int(input('Введите ID для удаления '))
    with s.connect('base.db') as bd:
        cur = bd.cursor()
        cur.execute('DELETE FROM заказы WHERE ID == ?',(n1,))
def del_data1():
    n1 = int(input('Введите ID для удаления '))
    with s.connect('base.db') as bd:
        cur = bd.cursor()
        cur.execute('DELETE FROM сотрудники WHERE ID == ?',(n1,))
def del_data2():
    n1 = int(input('Введите ID для удаления '))
    with s.connect('base.db') as bd:
        cur = bd.cursor()
        cur.execute('DELETE FROM клиенты WHERE ID == ?',(n1,))
def upd_data():
     while True:
        bd = s.connect('base.db')
        cur = bd.cursor()
        n2 = input('Введите для изменения данных \n'
                        'в столбце "дата"  1\n'
                        'в столбце "менеджер" 2\n'
                        'в столбце "клиент" 3\n'
                        'в столбце "товар" 4\n'
                        'в столбце "сумма" 5\n'
                        'для отмены 0\n')
        
        match n2:
                case '1':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE заказы SET дата ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '2':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE заказы SET менеджер ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '3':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE заказы SET клиент ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '4':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE заказы SET товар ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '5':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE заказы SET сумма ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '0':
                    break
                case _:
                    print('Ошибка ввода')
                    break
def upd_data1():
    while True:
        bd = s.connect('base.db')
        cur = bd.cursor()
        n2 = input('Введите для изменения данных \n'
                        'в столбце "фамилия" 1\n'
                        'в столбце "имя" 2\n'
                        'в столбце "дата рождения" 3\n'
                        'в столбце "должность" 4\n'
                        'для отмены 0\n')
        match n2:
                case '1':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE сотрудники SET фамилия ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '2':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE сотрудники SET имя ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '3':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE сотрудники SET дата_рождения ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '4':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE сотрудники SET должность ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '0':
                    break
                case _:
                    print('Ошибка ввода')
                    break
def upd_data2():
    while True:
        bd = s.connect('base.db')
        cur = bd.cursor()
        n2 = input('ВВедите для изменения данных \n'
                        'в столбце "фамилия"  1\n'
                        'в столбце "имя" 2\n'
                        'в столбце "телефон" 3\n'
                        'в столбце "e_mail" 4\n'
                        'для отмены 0\n')
        match n2:
                case '1':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE клиенты SET фамилия ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '2':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE клиенты SET имя ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '3':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE клиенты SET телефон ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '4':
                    n1 = input('Введите ID строки для изменения ')
                    nn = input('Новое значение  ')
                    cur.execute('UPDATE клиенты SET e_mail ==? WHERE ID == ?',(nn,n1))
                    bd.commit()
                    bd.close()
                case '0':
                    break
                case _:
                    print('Ошибка ввода')
                    break

