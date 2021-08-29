import os, discord
from . import bot

@bot.command()
async def load(ctx, ext):
    bot.load_extension(f'cogs.{ext}')

@bot.command()
async def unload(ctx, ext):
    bot.unload_extension(f'cogs.{ext}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
