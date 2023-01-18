## 5. Реализовать функцию, возвращающую n шуток, сформированных из трех
##случайных слов, взятых из трёх списков (по одному из каждого)
##in
##10 True
##out
##['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий',
##'автомобиль сегодня веселый', 'город позавчера утопичный']
from random import choice
def cr_lst (q,w,e,n,bl=False):
    rez = []
    if bl:
        for i in q:
            st = i + ' ' + choice(w) + ' '+ choice(e)
            rez.append(st)
    
        return rez
    for i in range(n):
        st = choice(q) + ' ' + choice(w) + ' '+ choice(e)
        rez.append(st)
    return rez
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
if __name__ == '__main__':
    n = int(input('Введите количество шуток '))
    b = int(input('Введите 1, если True,или 0, если False:   '))
    if n > 0 and (b == 1 or b == 0):
        print(cr_lst(nouns,adverbs,adjectives,n,bl=b))
    else:
        print('Некорректный ввод данных')
