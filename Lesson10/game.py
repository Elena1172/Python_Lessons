import telebot

import config
import random

from telebot import types
bot = telebot.TeleBot(config.TOKEN)
item = {}


gameIsStart = True


gameGround = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]


CrossesOrToe = ["0", "X"]


playerSymbol = CrossesOrToe[random.randint(0, 1)]


botSymbol = ""
if (playerSymbol == "0"):
    botSymbol = "X"
else:
    botSymbol = "0"

print("Bot is start")
winbool = False

losebool = False


def clear():
    global gameGround
    gameGround = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " ", ]


def win(cell_1, cell_2, cell_3):
    if cell_1 == playerSymbol and cell_2 == playerSymbol and cell_3 == playerSymbol:
        global winbool
        winbool = True


def lose(cell_1, cell_2, cell_3):
    if cell_1 == botSymbol and cell_2 == botSymbol and cell_3 == botSymbol:
        global losebool
        losebool = True


def defend(cell_1, cell_2, posDef):
    if cell_1 == playerSymbol and cell_2 == playerSymbol:
        posDef = botSymbol


@bot.message_handler(commands=['start'])
def welcome(message):
    kb = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    kb.add(types.KeyboardButton('/play'),types.KeyboardButton('/exit'))
    bot.send_message(message.chat.id,"Привет,я  телеграм бот, выбирай )",reply_markup=kb)
                    

@bot.message_handler(commands=['play'])
def mess(message):
    if gameIsStart == True:

        item = {}
        bot.send_message(message.chat.id, "Игра началась")

    global markup
    markup = types.InlineKeyboardMarkup(row_width=3)

    i = 0

    for i in range(9):
        item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

    markup.row(item[0], item[1], item[2])
    markup.row(item[3], item[4], item[5])
    markup.row(item[6], item[7], item[8])
    bot.send_message(message.chat.id, "Выбери клетку", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    if (call.message):

        # bot manager
        randomCell = random.randint(0, 8)
        if gameGround[randomCell] == playerSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == botSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == " ":
            gameGround[randomCell] = botSymbol
        # player manager
        for i in range(9):
            if call.data == str(i):
                if (gameGround[i] == " "):
                    gameGround[i] = playerSymbol

            # lose or win
            win(gameGround[0], gameGround[1], gameGround[2])
            win(gameGround[0], gameGround[4], gameGround[8])
            win(gameGround[6], gameGround[4], gameGround[2])
            win(gameGround[6], gameGround[7], gameGround[8])
            win(gameGround[0], gameGround[3], gameGround[6])
            lose(gameGround[0], gameGround[1], gameGround[2])
            lose(gameGround[0], gameGround[4], gameGround[8])
            lose(gameGround[6], gameGround[4], gameGround[2])
            lose(gameGround[6], gameGround[7], gameGround[8])
            lose(gameGround[0], gameGround[3], gameGround[6])

            item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Крестики нолики",
                              reply_markup=None)
        # update cells
        global  markup
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])

        bot.send_message(call.message.chat.id, "Выбери клетку", reply_markup=markup)
        global winbool
        if winbool:
            clear()
            bot.send_message(call.message.chat.id, "Я проиграл :(")

            winbool = False
            gameIsStart = False
        global losebool
        if losebool:
            clear()
            bot.send_message(call.message.chat.id, "Я выиграл!!")


            losebool = False
            gameIsStart = False
@bot.message_handler(commands=['exit'])
def ans(message):
    bot.send_message(message.chat.id,"До свидания! ",reply_markup=types.ReplyKeyboardRemove())
    bot.close()
@bot.message_handler()
def ans(message):
    bot.send_message(message.chat.id,"Таких команд я не знаю.")
bot.polling(none_stop=True)
