import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "deffo":
        await message.channel.send("STOP SAYING THAT!!!")

client.run('key')
