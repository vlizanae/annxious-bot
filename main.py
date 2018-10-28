from db import Database
from server import Server
from tbot import TelegramBot

bot = TelegramBot(Database(session=True))
bot.run_tbot()
Server(bot).run()
