'''Бот-калькулятор
Научите бота выполнять основные арифметические действия с числами: сложение, вычитание, умножение и деление. 
Если боту сказать “2-3=”, он должен ответить “-1”. Все выражения для калькулятора должны заканчиваться знаком равно.
Дополнительно: не забудьте обработать возможные ошибки во вводе: пробелы, отсутствие чисел, деление на ноль. '''


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


def bot_calc(bot, update):
    user_text = update.message.text.split()
    if len(user_text) == 1:
        answer = 'Что будем считать? Отсутствует выражение!'
        print(answer)
        update.message.reply_text(answer)
    else:
        text = user_text[1]
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


def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('calc', bot_calc))
    mybot.start_polling()
    mybot.idle()

main()

