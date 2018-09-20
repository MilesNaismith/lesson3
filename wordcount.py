'''Подсчёт количества слов
Добавить команду /wordcount котрая считает сова в присланной фразе. Например на запрос /wordcount "Привет как дела" 
бот должен посчитать количество слов в кавычках и ответить: 3 слова.
Не забудьте: добавить проверки на наличие кавычек, пустую строку. Подумайте, какие еще проверки нужны? '''


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
            text = '{} {}'.format(text, 'слово')
        elif text.endswith('2') or text.endswith('3') or text.endswith('4'):
            text = '{} {}'.format(text, 'слова')
        else:
            text = '{} {}'.format(text, 'слов')        
    else:
        text = 'Где кавычки?'        
    print(text)
    update.message.reply_text(text)   



def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('wordcount', word_count))
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()