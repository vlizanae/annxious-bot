from telegram.ext import Updater, CommandHandler

from secret import annxious_tbot_token
from .views import registry


def run_tbot(db):
    updater = Updater(token=annxious_tbot_token)

    for name, callback in registry.items():
        updater.dispatcher.add_handler(
            CommandHandler(name, lambda bot, update: callback(bot, update, db))
        )

    updater.start_polling()
