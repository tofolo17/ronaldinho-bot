import asyncio

import discord as disc
from discord.ext import commands

from Images import *

client = commands.Bot(command_prefix="ronaldo ")

status_list = {
    'FutCadeia': disc.ActivityType.playing,
    'o campeonato da cadeia no Paraguai': disc.ActivityType.watching,
    'em mais um rolê aleatório': disc.ActivityType.playing,
    'Champions League': disc.ActivityType.competing,
    'a Tropa do Bruxo': disc.ActivityType.listening,
    'Harry Potter': disc.ActivityType.watching,
    'R10 Skills Highlights': disc.ActivityType.watching,
    'a abertura da Copa do Mundo': disc.ActivityType.watching,
    'embaixadinha': disc.ActivityType.playing
}


@client.event
async def on_ready():
    print("Opa!")
    while True:
        for k, v in status_list.items():
            await client.change_presence(activity=disc.Activity(name=k, type=v))
            await asyncio.sleep(5)


@client.command()
async def gol(ctx):
    responses = [
        "É caixa.",
        "Tá lá.",
        "Vou te dibrei!",
        "Dorme no peito do pai.",
        "Broquei 3 hoje.",
        "Hat-trick do Bruxo.",
        "Joga a luva, goleirão!",
        "Desculpa te acordar, coruja."
    ]
    await ctx.send(choice(responses))


@client.command()
async def lindo(ctx):
    await ctx.send(pega_imagem())


client.run("ODQ5MzA5MzQ2MTgwODkwNzA1.YLZS9w.M855FYRAnux7_CLlq-X77SVro9g")
