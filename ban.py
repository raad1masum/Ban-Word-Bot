import discord
from discord.ext import commands

client = discord.Client()

deny = "deny message"
words = []

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    ms = message.content.lower()

    if message.author == client.user:
        return

    for x in words:
        if x == ms:
            await message.channel.send(deny)

client.run('key')
