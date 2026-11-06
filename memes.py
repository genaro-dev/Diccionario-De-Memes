import os
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')  

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

CARPETA_IMAGENES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

@bot.command()
async def meme(ctx):
    imagenes = [archivo for archivo in os.listdir(CARPETA_IMAGENES) if archivo.endswith('.png')]
    imagen = random.choice(imagenes)
    with open(os.path.join(CARPETA_IMAGENES, imagen), 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)

bot.run("")
