''' Полнолуние
Научить бота отвечать на вопрос “Когда ближайшее полнолуние после 2016-10-01?”. 
Чтобы узнать, когда ближайшее полнолуние, используй модуль ephem. Чтобы им пользоваться, 
его нужно установить ($ pip install ephem) и импортировать. '''

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from settings import API_TOKEN, ID_CHAT
import ephem
from datetime import datetime, date, time
import telegram

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def full_moon(bot,update):
    user_text = update.message.text.split()
    user_date = user_text[-1].split('.')
    try:
        for value in range(len(user_date)):
            user_date[value] = int(user_date[value])
    except (TypeError, ValueError):
        text = 'неверные данные'
        print(text)    
        update.message.reply_text(text)        
    user_date = tuple(user_date[::-1])        
    text = ephem.next_full_moon(user_date)
    print(ephem.next_full_moon(user_date))
    update.message.reply_text(text)



def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('fullmoon', full_moon))
    mybot.start_polling()
    mybot.idle()
 

main()