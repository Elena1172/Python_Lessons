import mod_func as m
def menu():
    while True:
        n = input('Введите для добавления данных  в базу 1\n'
                'удаления 2\n'
                'изменения 3\n'
                'просмотра таблиц 4\n'
                'для отмены 0\n')
        match n:
            case '1':
                menu1()
            case '2':
                menu2()
            case '3':
                menu3()
            case '4':
                menu4()
            case '0':
                break
            case _:
                print('Ошибка ввода дданных')
                break
def menu1():
    while True:
        n = input('Для добавления данных в таблицу заказы введите 1\n'
                    'в таблицу сотрудники 2\n'
                    'в таблицу клиенты 3\n'
                    'для отмены 0\n')
        match n:
            case '1':
                m.add_data()
            case '2':
                m.add_data1()
            case '3':
                m.add_data2()
            case '0':
                break
            case _:
                print('Ошибка ввода')
                break
def menu2():
    while True:
        n = input('Для удаления данных из таблицы заказы введите 1\n'
                    'из таблицы сотрудники 2\n'
                    'из таблицы клиенты 3\n'
                    'для отмены 0\n')
        match n:
            case '1':
                m.del_data()
            case '2':
                m.del_data1()
            case '3':
                m.del_data2()
            case '0':
                break
            case _:
                print('Ошибка ввода')
                break
def menu3():
    while True:
        n = input('Для изменения данных в таблице заказы введите 1\n'
                    'в таблице сотрудники 2\n'
                    'в таблице клиенты 3\n'
                    'для отмены 0\n')
        match n:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '0':
                break
            case _:
                print('Ошибка ввода')
                break
def menu4():
    while True:
        n = input('Для просмотра данных из таблицы заказы введите 1\n'
                    'из таблицы сотрудники 2\n'
                    'из таблицы клиенты 3\n'
                    'для отмены 0\n')
        match n:
            case '1':
                m.show_table()
            case '2':
                m.show_table1()
            case '3':
                m.show_table2()
            case '0':
                break
            case _:
                print('Ошибка ввода')
                break 
menu()         