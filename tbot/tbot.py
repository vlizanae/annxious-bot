from telegram import Bot
from telegram.ext import Updater, CommandHandler
from telegram.utils.request import Request

from config import annxious_tbot_token
from .views import start, help, userid, status


class TelegramBot:
    def __init__(self, db):
        self.bot = Bot(
            token=annxious_tbot_token,
            request=Request(con_pool_size=10)
        )
        self.db = db

    def run_tbot(self):
        updater = Updater(bot=self.bot)

        # Views
        updater.dispatcher.add_handler(
            CommandHandler('start', lambda bot, update: start(bot, update, self.db))
        )
        updater.dispatcher.add_handler(
            CommandHandler('help', help)
        )
        updater.dispatcher.add_handler(
            CommandHandler('userid', lambda bot, update: userid(bot, update, self.db))
        )
        updater.dispatcher.add_handler(
            CommandHandler('status', lambda bot, update: status(bot, update, self.db))
        )

        updater.start_polling()

    def send_message(self, id, message):
        self.bot.send_message(chat_id=id, text=message)
