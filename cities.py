''' Бонусное задание
Научите бота играть в города. 
Правила такие - внутри бота есть список городов, пользователь пишет /goroda Москва и если в списке такой город есть, 
бот отвечает городом на букву "а" - "Альметьевск, ваш ход". Оба города должны удаляться из списка. '''

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

town_list = ['Москва', 'Архангельск', 'Красноярск', 'Курск', 'Клин', 'Нальчик', 'Краснодар']

game_list = town_list[:]

def cities(bot,update):
    global game_list
    user_text = update.message.text.split()
    user_town = user_text[1]
    print(user_town)
    if user_town in game_list:
        game_list.remove(user_town)
        end_letter = user_town[-1].upper()
        if len(game_list) == 0:
            text = 'Ты выиграл!'
            print(text)
            update.message.reply_text(text)    
        for town in game_list:
            if town.startswith(end_letter):
                bot_town = town
                print(town)
                update.message.reply_text(bot_town)
                game_list.remove(bot_town)
                break
            elif game_list.index(town) == len(game_list) - 1:
                text = 'Ты выиграл!'
                print(text)
                update.message.reply_text(text)     

    else:
        text = 'нет такого города'            
        print(text)
        update.message.reply_text(text)
def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('goroda', cities))
    mybot.start_polling()
    mybot.idle()
 

main()