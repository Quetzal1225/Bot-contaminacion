import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot que te puede ayudar en salvar el planeta!')

@bot.command()
async def contaminacion(ctx, item: str):
    """¿De que tienes curiosidad? (reciclar, reutilizar o reducir)"""
    erres_3 = {
        "reciclar": "Para reciclar puedes hacer desde casa la separacion de basura",
        "reutilizar": "Podemos utilizar cualquier material que no este del todo inservible para volverlo una manualidad o algo util, como por ejemplo hacer macetas con el fondo de las botellas de plastico",
        "reducir": "Puedes usar cosas biodegradables, asi como dejar de usar tanto cosas desechablesy ser más conscientes con lo que compras, como por ejemplo en vez de comprar botellas de agua de plastico, mejor cargar una botella de agua que puedes volver a usar cuando salgas, a menos que tengas demasada sed"
    }
    informacion = erres_3.get(item.lower(), "Disculpa pero no sé exactamente a qué te refieres.")

    img_random = random.choice(os.listdir("images"))
    with open(f"images/{img_random}", "rb") as f:
        picture = discord.File(f)
        print(img_random)
        await ctx.send(content=informacion, file=picture)

