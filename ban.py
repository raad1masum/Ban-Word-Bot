import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is read.')

client.run('NjcxNTMzNjgyMzYzODU4OTQ0.Xi-UkQ.t9IOYjgFepSkWq7Itu_F0kDOe-U')
