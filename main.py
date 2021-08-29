import os
from lib import bot
from dotenv import load_dotenv

from lib import event_handler
from lib import command_handler
from lib import cogs_handler

load_dotenv()
bot.run(os.getenv('token'))
