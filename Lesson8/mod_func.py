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

show_table()
show_table1()
show_table2()
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
add_data()
add_data1()
add_data2()
show_table()
show_table1()
show_table2()
    
