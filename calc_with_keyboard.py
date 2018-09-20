''' Бонусное задание: клавиатура
Добавьте к предыдущей задаче клавиатуру калькулятора с цифрами и основными математическими действиями. '''

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

expression =''

def calc_keyboard(bot, update):
    global expression
    
    custom_keyboard = [['1', '2', '3', '4', '5'], 
                       ['5', '6', '7', '8', '9'],
                       ['0', '+', '-', '*', ':', '=']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)    
    expression = expression + update.message.text
    if expression.endswith('='):
        bot.send_message(chat_id= ID_CHAT,
                     text = bot_calc(expression),
                     reply_markup=reply_markup)                
        expression = ''

def keyboard_off(bot, update):
    reply_markup = telegram.ReplyKeyboardRemove()
    bot.send_message(chat_id=ID_CHAT, text="I'm back.", reply_markup=reply_markup) 

def bot_calc(text):
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
    return answer
    
def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('keyboard_off', keyboard_off))
    dp.add_handler(MessageHandler(Filters.text, calc_keyboard))
    #Начало цикла
    mybot.start_polling()
    mybot.idle()
 

if __name__ == "__main__":
    main()
