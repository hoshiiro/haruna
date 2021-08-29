import requests, json, discord
from . import bot

@bot.command('aquote')
async def test(ctx, *, msg):
    """
    Shows a quote by anime character. 
    Example: .aquote first_char_name last_char_name
    """

    response = requests.get("https://animechan.vercel.app/api/quotes/character?name={}".format(msg))
    data = json.loads(response.text)
    data = data[0]

    embed = discord.Embed(title=data['character'],description=data['quote'],color=discord.Color.blue())

    embed.set_footer(text=f"From {data['anime']} | Animechan Quotes API")

    await ctx.send(embed=embed)

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


@bot.command('testchan')
async def testchan(ctx, ch_id):
    channel = ctx.get_channel(ch_id)
    channel.send_message("bruh")

