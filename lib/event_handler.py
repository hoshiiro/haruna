from . import bot
from discord_components import *

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print(f"Logged as {bot.user}")
