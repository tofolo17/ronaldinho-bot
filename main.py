import asyncio
import os
from random import choice

import discord as disc
from discord.ext import commands

from Images import pega_imagem

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
    'embaixadinha': disc.ActivityType.playing,
}


# Cycles the bot's status through the list every 5 seconds.
@client.event
async def on_ready():
    print("Opa!")
    while True:
        for k, v in status_list.items():
            await client.change_presence(
                activity=disc.Activity(name=k, type=v)
            )
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
        "Desculpa te acordar, coruja.",
    ]
    await ctx.send(choice(responses))


@client.command()
async def lindo(ctx):
    await ctx.send(pega_imagem())


# Discord bot token, read from the environment (never hardcode it).
client.run(os.environ.get("DISCORD_TOKEN"))
