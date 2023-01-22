from logg import logging
def get_numder():
    while True:
        try:
            n = float(input('Enter number: '))
            return n
        except ValueError:
            print('Error ')
            logging.warning('ValueError')
def get_numder1():
    while True:
        try:
            n = float(input('Enter number: '))
            100/n
            return n
        except Exception:
            print('ValueError')
            logging.warning('ValueError')
        except ZeroDivisionError:
            print('ZeroDivisionError')
            logging.warning('ZeroDivisionError')
def get_numder2():
    while True:
        try:
            n = get_numder()
            m = get_numder()
            nm = complex(n,m)
            1/nm
            return nm
        except ZeroDivisionError:
            print('ZeroDivisionError')
            logging.warning('ZeroDivisionError')
