import discord
from discord.ext import commands
from api.azurlane import ship
import datetime

class al(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Azurlane Cogs loaded successfully")

    @commands.command()
    async def info(self, ctx, *, shipname):
        """Print general info of the ship"""
        api = ship(shipname)
        gen = api.geninfo()

        embed = discord.Embed(
                    title="{} - {}".format(api.ship_name(), api.ship_type()),
                    description=f"{api.ship_description()}",
                    timestamp=datetime.datetime.utcnow(),
                    color=discord.Color.orange()
                )
        try:
            embed.add_field(name="Construction Time", value=gen['Construction'], inline=True)
        except KeyError:
            embed.add_field(name="Obtainment", value=gen['Obtainment'], inline=True)
        embed.add_field(name="Rarity", value=gen['Rarity'], inline=True)
        embed.add_field(name="Classification", value=gen['Classification'], inline=True)
        embed.add_field(name="Faction", value=gen['Faction'], inline=True)
        embed.add_field(name="Illustrator", value=gen['Illustrator'], inline=True)
        embed.add_field(name="Voice Actor", value=gen['Voice actor'], inline=True)
        embed.set_footer(text="https://azurlane.koumakan.jp", icon_url="http://gravatar.com/avatar/ae7c270bebbeb8c26ba11c27b5296a2f?s=150")
        embed.set_image(url=api.ship_banner())
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(al(bot))
