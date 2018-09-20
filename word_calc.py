''' Словарный калькулятор
Научите бота вычислять математические выражения с целыми числами от одного до десяти, заданные словами. 
Например, “сколько будет три минус два” или “сколько будет четыре умножить на шесть”.
Дополнительно: научите бота обрабатывать вещественные числа (“четыре и пять умножить на шесть и два” – это “4.5 * 6.2”) '''


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from settings import API_TOKEN, ID_CHAT
import telegram

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

### ПРИВЕДЕНИЕ К ВИДУ ДЛЯ КАЛЬКУЛЯТОРА ###
def change(some_list):
    sinonim = {'один':'1',
               'два':'2',
               'три':'3',
               'четыре':'4',
               'пять':'5',
               'шесть':'6',
               'семь':'7',
               'восемь':'8',
               'девять':'9',
               'ноль':'0',
               'плюс':'+',
               'минус':'-',
               'умножить':'*',
               'разделить':':',
               'и':'.'}
    for value in range(len(some_list)):
        if some_list[value] in sinonim:
            some_list[value] = sinonim[some_list[value]]
    for value in some_list:                        
        if value == 'на':
            some_list.remove('на')    
    return some_list                 
 
 
def word_calc(bot, update):
    user_text = update.message.text
    if user_text.startswith('/wordcalc сколько будет '):
        parts = user_text[23:].split()
    else:
        text = 'Неверный формат записи'
    user_text = change(parts)
    user_text = ''.join(user_text) + '='
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


def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('wordcalc', word_calc))
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()