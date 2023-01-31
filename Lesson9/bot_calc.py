import telebot
TOKEN = ''
bot = telebot.TeleBot(TOKEN)
val = ''
old_val = ''
kb = telebot.types.InlineKeyboardMarkup()
kb.row( telebot.types.InlineKeyboardButton('',callback_data='no'),
        telebot.types.InlineKeyboardButton('c',callback_data='c'),
        telebot.types.InlineKeyboardButton('<=',callback_data='<='),
        telebot.types.InlineKeyboardButton('/',callback_data='/'))

kb.row( telebot.types.InlineKeyboardButton('7',callback_data='7'),
        telebot.types.InlineKeyboardButton('8',callback_data='8'),
        telebot.types.InlineKeyboardButton('9',callback_data='9' ),
        telebot.types.InlineKeyboardButton('*',callback_data='*'))

kb.row( telebot.types.InlineKeyboardButton('4',callback_data='4'),
        telebot.types.InlineKeyboardButton('5',callback_data='5'),
        telebot.types.InlineKeyboardButton('6',callback_data='6'),
        telebot.types.InlineKeyboardButton('-',callback_data='-'))

kb.row( telebot.types.InlineKeyboardButton('1',callback_data='1'),
        telebot.types.InlineKeyboardButton('2',callback_data='2'),
        telebot.types.InlineKeyboardButton('3',callback_data='3'),
        telebot.types.InlineKeyboardButton('+',callback_data='+'))

kb.row( telebot.types.InlineKeyboardButton(' ',callback_data='no'),
        telebot.types.InlineKeyboardButton('0',callback_data='0'),
        telebot.types.InlineKeyboardButton(',',callback_data='.'),
        telebot.types.InlineKeyboardButton('=',callback_data='='))
@bot.message_handler(commands=['start'])
def get_message(message):
    global val
    if val == '':
        bot.send_message(message.from_user.id, '0',reply_markup=kb)
    else:
        bot.send_message(message.from_user.id,val,reply_markup=kb)
@bot.callback_query_handler(func=lambda call:True) 
def callback_fun(query):
    global val, old_val
    data = query.data
    if data == 'no':
        pass
    elif data == 'c':
        val = ''
    elif data == '<=':
        if val != '':
            val = val[:len(val) - 1]
    elif data == '=':
        try:
            val = str(eval(val))
        except:
            val = 'Ошибка!'
    else:
        val += data
    if (val != old_val and val != '') or ('0' != old_val and val == ''):
        if val == '':
            bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id,text='0',reply_markup=kb)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id,text=val,reply_markup=kb)
    old_val = val
    if val == 'Ошибка!': val = ''
bot.polling(non_stop=False) 