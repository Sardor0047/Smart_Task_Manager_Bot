from telegram.ext import Updater,CallbackQueryHandler,CommandHandler
from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from tinydb import TinyDB, Query
import os


def start(update,context):
    update.message.reply_text(
        "Vazifalaringizni boshqarish uchun bot!"
    )






token = os.getenv('Token')

updater = Updater(token)

dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(CommandHandler('list',start))
dispatcher.add_handler(CommandHandler('add',start))



updater.start_polling()
updater.idle()