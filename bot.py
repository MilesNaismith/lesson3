from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from tokentoken import API_TOKEN, ID_CHAT
import ephem
from datetime import datetime, date, time
import telegram


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

expression =''
def greet_user(bot, update):
    text = 'Привет! Бот работает!'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet_user(bot,update):
    user_text = update.message.text.split()
    planet = user_text[1]
    today = datetime.strftime(datetime.now(), '%Y/%m/%d')
    planet = getattr(ephem,planet)(today)
    text = ephem.constellation(planet)
    print(text)
    update.message.reply_text(text)

def word_count(bot, update):
    user_text = update.message.text.split()
    if len(user_text) == 1:
        text = 'Требуется ввести фразу'
    elif len(user_text) == 2 and user_text[1] =='""':
        text = 'Вы просто написали кавычки'
    elif len(user_text) == 2 and user_text[1] =='"':
        text = 'Вы просто написали кавычку'            
    elif user_text[1].startswith('"') and user_text[-1].endswith('"'):
        text = str(len(user_text) - 1)
        if text.endswith('1'):
            text = text + ' слово'
        elif text.endswith('2') or text.endswith('3') or text.endswith('4'):
            text = text + ' слова'
        else:
            text = text + ' слов'        
    else:
        text = 'Где кавычки?'        
    print(text)
    update.message.reply_text(text)   
### КАЛЬКУЛЯТОР ###
def bot_calc(bot, update):
    global expression
    user_text = expression
    
    if len(user_text) <= 1:
        answer = 'Что будем считать? Отсутствует выражение!'
        print(answer)
        update.message.reply_text(answer)
    
    else:
        text = user_text
    
    if '+' in text:
        x = int(text[:text.index('+')])
        y = int(text[text.index('+') + 1:text.index('=')])
        answer = x + y
    elif '-'in text:
        x = int(text[:text.index('-')])
        y = int(text[text.index('-') + 1:text.index('=')])
        answer = x - y
    elif '*' in text:
        x = int(text[:text.index('*')])
        y = int(text[text.index('*') + 1:text.index('=')])
        answer = x * y
    elif ':' in text:
        x = int(text[:text.index(':')])
        y = int(text[text.index(':') + 1:text.index('=')])
        if y == 0:
            answer = 'на ноль делить нельзя'
        else:
            answer = x / y       
    print(answer)
    update.message.reply_text(answer)    
### ПРИВЕДЕНИЕ К ВИДУ ДЛЯ КАЛЬКУЛЯТОРА ###
def change(some_list):
    print(some_list)
    for value in range(len(some_list)):
        if some_list[value] == 'один':
            some_list[value] = '1'
        elif some_list[value] == 'два':
            some_list[value] = '2'
        elif some_list[value] == 'три':
            some_list[value] = '3'
        elif some_list[value] == 'четыре':
            some_list[value] = '4'
        elif some_list[value] == 'пять':
            some_list[value] = '5'
        elif some_list[value] == 'шесть':
            some_list[value] = '6'
        elif some_list[value] == 'семь':
            some_list[value] = '7'
        elif some_list[value] == 'восемь':
            some_list[value] = '8'
        elif some_list[value] == 'девять':
            some_list[value] = '9'
        elif some_list[value] == 'ноль':
            some_list[value] = '0'
        elif some_list[value] == 'плюс':
            some_list[value] = '+'                                    
        elif some_list[value] == 'минус':
            some_list[value] = '-'
        elif some_list[value] == 'умножить':
            some_list[value] = '*'
        elif some_list[value] == 'разделить':
            some_list[value] = ':'
        elif some_list[value] == 'и':
            some_list[value] = '.' 
    for value in some_list:                        
        if value == 'на':
            some_list.remove('на')    
    return some_list        
            
def word_calc(bot, update):
    user_text = update.message.text
    print(user_text)
    if user_text.startswith('/wordcalc сколько будет '):
        parts = user_text[23:].split()
    else:
        text = 'Неверный формат записи'
    user_text = change(parts)
    print(user_text)
    user_text = ''.join(user_text) + '='
    print(user_text)
    if len(user_text) <= 1:
        answer = 'Что будем считать? Отсутствует выражение!'
        print(answer)
        update.message.reply_text(answer)
    else:
        text = user_text
    if '+' in text:
        x = float(text[:text.index('+')])
        y = float(text[text.index('+') + 1:text.index('=')])
        answer = x + y
    elif '-'in text:
        x = float(text[:text.index('-')])
        y = float(text[text.index('-') + 1:text.index('=')])
        answer = x - y
    elif '*' in text:
        x = float(text[:text.index('*')])
        y = float(text[text.index('*') + 1:text.index('=')])
        answer = x * y
    elif ':' in text:
        x = float(text[:text.index(':')])
        y = float(text[text.index(':') + 1:text.index('=')])
        if y == 0:
            answer = 'на ноль делить нельзя'
        else:
            answer = x / y       
    print(answer)
    update.message.reply_text(answer)         
    

def calc_keyboard(bot, update):
    global expression
    custom_keyboard = [['1', '2', '3', '4', '5'], 
                       ['5', '6', '7', '8', '9'],
                       ['0', '+', '-', '*', ':', '=']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    
    expression = expression + update.message.text
    if expression.endswith('='):
        bot_calc(bot, update)
        expression = ''    
    bot.send_message(chat_id= ID_CHAT,
                     text = expression,
                     reply_markup=reply_markup)                
def keyboard_off(bot, update):
    reply_markup = telegram.ReplyKeyboardRemove()
    bot.send_message(chat_id=ID_CHAT, text="I'm back.", reply_markup=reply_markup)               
    

def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_user))
    dp.add_handler(CommandHandler('wordcount', word_count))
    dp.add_handler(CommandHandler('calc', bot_calc))
    dp.add_handler(CommandHandler('wordcalc', word_calc))
    dp.add_handler(MessageHandler(Filters.text, calc_keyboard))
    dp.add_handler(CommandHandler('keyboard_off', keyboard_off))
    #Начало цикла
    mybot.start_polling()
    mybot.idle()
 

main()