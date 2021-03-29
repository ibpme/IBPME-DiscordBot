import discord
from secret import TOKEN
import nim_api

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello {}!'.format(message.author.name))

    if message.content.startswith('$invite-me'):
        await message.channel.send('Add this bot to yout discord server by clicking this link:')

    if message.content.startswith("$find-name"):
        nim = message.content.split("$find-name", 1)[1].strip()
        name = nim_api.find_name(nim)
        await message.channel.send(name)

    if message.content.startswith("$find-nim"):
        name = message.content.split("$find-nim", 1)[1].strip()
        nim = nim_api.find_nim(name)
        await message.channel.send(nim)

client.run(TOKEN)
