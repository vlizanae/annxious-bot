from telegram import Bot
from telegram.ext import Updater, CommandHandler
from telegram.utils.request import Request
import logging

from config import annxious_tbot_token
from .views import start, help, userid


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class TelegramBot:
    def __init__(self):
        self.bot = Bot(
            token=annxious_tbot_token,
            request=Request(con_pool_size=10)
        )

    def run_tbot(self, db):
        updater = Updater(bot=self.bot)

        # Views
        updater.dispatcher.add_handler(
            CommandHandler('start', lambda bot, update: start(bot, update, db))
        )
        updater.dispatcher.add_handler(
            CommandHandler('help', help)
        )
        updater.dispatcher.add_handler(
            CommandHandler('userid', lambda bot, update: userid(bot, update, db))
        )

        updater.start_polling()

    def send_message(self, id, message):
        self.bot.send_message(chat_id=id, text=message)
