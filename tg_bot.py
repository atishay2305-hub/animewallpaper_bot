# telegram bot
# 

from asyncore import dispatcher
from distutils.cmd import Command
from email.message import Message
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5659302124:AAH9B_nev1w1PUGDuTdysd0zAGMY_ysrPxI")


def start(update: Update, context: CallbackContext):
    update.message.reply_text()
    "AE86 riderz, tell me what you want: ?"

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Engine got thrashed?")

def wallpaper_url(update: Update, context: CallbackContext):
    update.message.reply_text("Wallpaper URL => https://www.wallpaperflare.com/search?wallpaper=Initial+D")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry bro" % update.message.text
    )

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('wallpapers', wallpaper_url))
updater.dispatcher.add_handler(CommandHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()