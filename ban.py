import discord
from discord.ext import commands

client = discord.Client()

deny = "stop doing that"
words = ['deffo', 'cap', 'fr', 'atm', 'lowk', 'highk', 'istg', 'cappin', 'yk', 'mv', 'wld', 'ihy', 'gfy']

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
