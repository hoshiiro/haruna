import requests, json, discord, datetime
from . import bot

prev_msg = None

@bot.command('aquote')
async def test(ctx, *, character_name):
    """
    Shows a quote by anime character. 
    Example: .aquote first_char_name last_char_name
    """

    response = requests.get("https://animechan.vercel.app/api/quotes/character?name={}".format(character_name))
    if response.status_code == 404:
        
        message = await ctx.send("> Character not found, maybe a typo(?) or not in the database(?)")
        prev_msg = True
    else:

        data = json.loads(response.text)
        data = data[0]

        embed = discord.Embed(title=data['character'],description=data['quote'],color=discord.Color.blue())

        embed.set_footer(text=f"From {data['anime']} | Animechan Quotes API")
        
        if prev_msg == True:
            await message.edit("> Showing quote for **\"{character_name}\"**", embed=embed)
            prev_msg = False
        else:
            await ctx.send(f"> Showing first quote for **\"{character_name}\"** ", embed=embed)

@bot.command('num')
async def addnum(ctx, operator, number1, number2):

    """Basic add, sub, div, mul, a literal calculator like program."""

    num1 = int(number1)
    num2 = int(number2)

    op = operator

    async def send_msg(ctx, op, num):
        await ctx.send(f"{num1} {op} {num2} = {num}")

    if op == "add":
        num = num1 + num2
        await send_msg(ctx, "+", num)
    elif op == "sub":
        num = num1 - num2
        await send_msg(ctx, "-", num)
    elif op == "mul":
        num = num1 * num2
        await send_msg(ctx, "*", num)
    elif op == "div":
        num = num1 / num2
        await send_msg(ctx, "÷", num)
    else:
        await ctx.send("Invalid operation.")

@bot.command('clear')
async def clear(ctx, amount):
    """Delete amount of message in amount arguments"""
    await ctx.channel.purge(limit=int(amount))


@bot.command('about')
async def about(ctx):
    """Print about this bot."""

    file = open("about.txt", "r").read()
    embed = discord.Embed(
            title="About Me",
            description=file,
            timestamp=datetime.datetime.utcnow())
    embed.set_image(url="http://imgur.com/a/yvkvZcX")
    embed.set_footer(text=f"Requested by {ctx.author.name}.", icon_url=ctx.author.avatar_url)
    await ctx.send(f"> Information About Flaura Bot • [ for {ctx.author} ]", embed=embed)

