import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button

activity = discord.Activity(type=discord.ActivityType.listening, name="f!help")

bot = commands.Bot(
    command_prefix=["f!", "Reika ", "Rei "],
    activity=activity,
    status=discord.Status.idle
)
