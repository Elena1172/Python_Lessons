# 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. 
# Игрок - игрок, без бота.
board = list(range(1,10))
def draw_board(board):
    print('-------------')
    for i in range(3):
        print('|',board[0+i*3],'|',board[1+i*3],'|',board[2+i*3],'|')
        print('-------------')
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = int(input(('Куда поставим ' + player_token + '? ')))
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in 'XO':
                board[player_answer - 1] = player_token
                valid = True
            else:
                print('Эта клетка занята')
        else:
            print('Некорректный ввод.Введите число от 1 до 9.')
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_coord:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False
def main(board,encoding = 'utf-8'):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "Bыиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)
main(board)
