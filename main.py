from db import Database
from server import Server
from tbot import TelegramBot

bot = TelegramBot()
bot.run_tbot(Database(session=True))
Server(bot).run()
