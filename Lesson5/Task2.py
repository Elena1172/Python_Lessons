# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные 
# хранятся в отдельных текстовых файлах.
t = 'WWWQQQQhhhFFFGGGGGG<<<<<'
t1 = 'DDDDJJJJttttEEEELLLLnnnnnndddlllll'
t2 = 'BBBBBBNNNNCccccccJJJJJKKKKnnnnn'
def write_file(*text):
    for i in text:
        with open('t.txt','a') as w:
            w.write(i + '\n')
def read_file(path):
   with open(path,'r') as r:
        rr = r.readlines()
        new_sp = [i[:-1] for i in rr]
        return new_sp
def encode_rle(text):
    count = 1
    code = ''
    prev_char = ''
    if not text: return ''
    for char in text:
        if char != prev_char:
            if prev_char:
                code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1

    else:
        code += str(count) + prev_char
        return code
def decode_rle(d):
    decode = ''
    count = ''
    for char in d:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode
write_file(t,t1,t2)
n = input('Enter the name of the file with the text(t.txt): ')
if n == 't.txt':
    r = read_file(n)
    for i in r:
        with open('t1.txt','a') as w:
                w.write(encode_rle(i) + '\n')
    rr = read_file('t1.txt')
    print(rr)
    for i in rr:
        with open('t2.txt','a') as w:
            w.write(decode_rle(i) + '\n')
else:
    print('Name not found')