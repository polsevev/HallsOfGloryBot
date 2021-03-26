
import requests
import os
from discord.ext import commands

GUILD = os.getenv('Rolf\'s bot testing')

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print("Bot ready")


@bot.command(brief = "Random Chuck Norris joke")
async def chuck(ctx):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    value = response.json()["value"]
    await ctx.send(value)


@bot.command(brief = "Random quote from Taylor Swift")
async def taylor(ctx):
    response = requests.get("https://api.taylor.rest/")
    text = response.json()["quote"]
    await ctx.send("Shit Taylor Swift has said: " + text)


@bot.command(brief = "Random quote from Trump")
async def trump(ctx):
    response = requests.get("https://www.tronalddump.io/random/quote")
    text = response.json()["value"]
    name = "Donald Trump"
    date = response.json()["appeared_at"]
    year = date[:4]
    message = name + " said \"" + text + "\" in " + year
    await ctx.send(message)


bot.run("")