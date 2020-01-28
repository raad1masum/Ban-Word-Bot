import discord
from discord.ext import commands

client = command .Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is read.')

client.run('key')
