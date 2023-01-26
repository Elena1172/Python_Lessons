import sqlite3 as s
x = [
    [
        2,
        '21/01/23',
        'Иванов Ваня',
        'Савельева Оля',
        'пылесос',
        15000
    ],
    [
        '3',
        '22/01/23',
        'Иванов Ваня',
        'Ткачев  Анатолий',
        'телевизор',
        20000
     ],
     [
        '4',
        '23/01/23',
        'Иванов Ваня',
        'Проклов Юра',
        'комод',
        13000
    ]
    ]
y = [
    [
        1,
        'Воронина',
        'Юля',
        '123456',
        'el_mail1'
    ],
    [
        2,
        'Савельева',
        'Оля',
        '234567',
        'el_mail2'
    ],
    [
        3,
        'Ткачев',
        'Анатолий',
        '34567',
        'el_mail3'
    ],
    [
        4,
        'Проклов',
        'Юра',
        '456789',
        'el_mail4'
    ],
    ]
    
with s.connect('base.db') as bd:
    cur = bd.cursor()
    bd.execute("""CREATE TABLE IF NOT EXISTS {}(
                                               ID INTEGER PRIMARY KEY ,
                                               дата DATE,
                                               менеджер VARCHAR(30),
                                               клиент VARCHAR(30),
                                               товар TEXT,
                                               сумма REAL)""".format ('заказы'))
    bd.execute("""CREATE TABLE IF NOT EXISTS {}(
                                               ID INTEGER PRIMARY KEY,
                                               фамилия VARCHAR(30),
                                               имя VARCHAR(10),
                                               дата_рождения DATE,
                                               должность TEXT)""".format ('сотрудники'))
    bd.execute("""CREATE TABLE IF NOT EXISTS {}(
                                               ID INTEGER PRIMARY KEY,
                                               фамилия VARCHAR(30),
                                               имя VARCHAR(10),
                                               телефон TEXT,
                                               e_mail TEXT)""".format ('клиенты'))
    cur.execute('INSERT INTO заказы VALUES(?,?,?,?,?,?)',(1,"20/01/23","Марков Василий","Воронина Юля","холодильник",100000))
    cur.executemany('INSERT INTO заказы VALUES(?,?,?,?,?,?)',(x))                                                 
    cur.execute('INSERT INTO сотрудники VALUES(?,?,?,?,?)',(1,"Марков","Василий","01/01/00","менеждер"))
    cur.execute('INSERT INTO сотрудники VALUES(?,?,?,?,?)',(2,"Иванов","Ваня","01/02/98","менеждер"))
    cur.executemany('INSERT INTO клиенты VALUES(?,?,?,?,?)',(y))
    
