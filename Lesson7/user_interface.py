from logg import logging
import mod_calc as c
import exep as e
def menu_rat():
    n1 = e.get_numder()
    while True:
        m = input('Select an operation\n'
                    '1 -  "sum+"\n'
                    '2 - "sub-"\n'
                    '3 - "mul*"\n'
                    '4 - "div/"\n'
                    '5 - "div//"\n'
                    '6 - "div%"\n'
                    '7 - "pow**"\n'
                    '8 - "scrt**0.5"\n'
                    '0 -  previos menu\n'
                    )
        match m:
            case '1':
                n2 = e.get_numder()
                logging.info(f'summa {n1} and {n2} =  {c.sum(n1,n2)}')
                return print(f'{n1} + {n2} = {c.sum(n1,n2)}')
            case '2':
                n2 = e.get_numder()
                logging.info(f' sub {n1} and {n2} = {c.sub(n1,n2)}')
                return print(f'{n1} - {n2} = {c.sub(n1,n2)}')
            case '3':
                n2 = e.get_numder()
                logging.info(f' muit {n1} and {n2} = {c.mul(n1,n2)}')
                return print(f'{n1} * {n2} = {c.mul(n1,n2)}')
            case '4':
                n2 = e.get_numder1()
                logging.info(f' {n1} div/ {n2} = {c.div01(n1,n2)}')
                return print(f'{n1} разделить на {n2} = {c.div01(n1,n2)}')
            case '5':
                n2 = e.get_numder()
                logging.info(f' {n1} div// {n2} = {c.div02(n1,n2)}')
                return print(f'{n1} деление целочисленное на {n2} = {c.div02(n1,n2)}')
            case '6':
                n2 = e.get_numder()
                logging.info(f' {n1} div% {n2} = {c.div03(n1,n2)}')
                return print(f'{n1} деление без остатка на {n2} = {c.div03(n1,n2)}')
            case '7':
                n2 = e.get_numder()
                logging.info(f' {n1}^ {n2} = {c.pow(n1,n2)}')
                return print(f'{n1} в степени {n2} = {c.pow(n1,n2)}')
            case '8':
                logging.info(f' {n1}^0.5  = {c.sqrt(n1)}')
                return print(f'квадратный корень  числа {n1} = {c.sqrt(n1)}')
            case '0':
                logging.info('exit')
                break
            case _:
                logging.warning('Error Value')
                print('Error')
                break
def menu_com():
    n = e.get_numder()
    n1 = e.get_numder()
    nn = complex(n,n1)
    while True:
        m = input('Select an operation\n'
                    '1 -  "sum+"\n'
                    '2 -  "sub-"\n'
                    '3 -  "mul*"\n'
                    '4 - "div/"\n'
                    '5 - "pow**"\n'
                    '0 -  previos menu\n')
        match m:
            case '1':
                n2 = e.get_numder()
                n3 = e.get_numder()
                mm = complex(n2,n3)
                logging.info(f'sum {nn} and {mm} = {c.sum(nn,mm)}')
                return print(f'{nn} + {mm} = {c.sum(nn,mm)}')
                
            case '2':
                n2 = e.get_numder()
                n3 = e.get_numder()
                mm = complex(n2,n3)
                logging.info(f'sub {nn} and {mm} = {c.sub(nn,mm)}')
                return print(f'{nn} - {mm} = {c.sub(nn,mm)}')
            case '3':
                n2 = e.get_numder()
                n3 = e.get_numder()
                mm = complex(n2,n3)
                logging.info(f'mult  {nn} and {mm} = {c.mul(nn,mm)}')
                return print(f'{nn} * {mm} = {c.mul(nn,mm)}')
            case '4':
                mm = e.get_numder2()
                logging.info(f'{nn} div {mm} = {c.div01(nn,mm)}')
                return print(f'{nn} / {mm} = {c.div01(nn,mm)}')
            case '5':
                n4 = e.get_numder()
                logging.info(f'{nn}^{n4} = {c.pow(nn,n4)}')
                return print(f'{nn} * {n4} = {c.pow(nn,n4)}')
            case '0':
                logging.info('exit')
                break
            case _:
                print ('Error')
                logging.warning('Error Value')
                break
def menu():
    print('Calculator welcomes you!')
    while True:
        st = input('Working with\n'
        '1 - rational\n'
        '2 - complex\n'
        '0 - exit\n')
        match st:
            case '1':
                 menu_rat()
            case '2':
                 menu_com()
            case '0':
                 break
            case _:
                 print('Error')
                 break



            
        
        
        
