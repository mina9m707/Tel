from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater('5357617447:AAGN4uwbAnu9dZOkq9gE-nw4xkGbZjERmQc')

def start(bot, update):
   chat_id = update.message.chat_id
   bot.sendMessage(chat_id, 'تبریک میگم')

start_Command = CommandHandler('start', start)

Updater.dispatcher.add_handler(start_Command)

Updater.start_polling()