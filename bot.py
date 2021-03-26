import random

import requests
import os
from discord.ext import commands

GUILD = os.getenv('Rolf\'s bot testing')

bot = commands.Bot(command_prefix='$')

translateAPI = "https://api.funtranslations.com/translate/"

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

@bot.command(brief = "Get some good advice")
async def advice(ctx):
    response = requests.get("https://api.adviceslip.com/advice")
    text = response.json()
    await ctx.send(text["slip"]["advice"])

@bot.command(brief = "Get a random cat fact")
async def catfact(ctx):
    response = requests.get("https://cat-fact.herokuapp.com/facts")
    size = len(response.json())
    index = random.randint(0, size-1)
    await ctx.send(response.json()[index]["text"])

@bot.command(brief = "POGCHAMP!")
async def pogchamp(ctx):
    await ctx.send("POGCHAMP!")

@bot.command(brief = "I want to die")
async def pogchamp(ctx):
    await ctx.send("Kille me please")





bot.run("")