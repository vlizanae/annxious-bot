from db import Database
from server import Server
from tbot import TelegramBot
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

bot = TelegramBot(Database(session=True))
bot.run_tbot()
Server(bot).run()
