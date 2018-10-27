from telegram import Bot
from telegram.ext import Updater, CommandHandler

from secret import annxious_tbot_token
from .views import registry


class TelegramBot:
    def __init__(self):
        self.bot = Bot(token=annxious_tbot_token)

    def run_tbot(self, db):
        updater = Updater(bot=self.bot)

        for name, callback in registry.items():
            updater.dispatcher.add_handler(
                CommandHandler(name, lambda bot, update: callback(bot, update, db))
            )

        updater.start_polling()

    def send_message(self, id, message):
        self.bot.send_message(chat_id=id, text=message)