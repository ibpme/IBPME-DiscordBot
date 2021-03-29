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

    # GENERAL COMMANDS
    if message.content.startswith('$hello'):
        await message.channel.send('Hello {}!'.format(message.author.name))

    if message.content.startswith('$invite-me'):
        await message.channel.send('Add this bot to your discord server by clicking this link: https://discord.com/api/oauth2/authorize?client_id=825996658554568725&permissions=2148002880&scope=bot')

    # NIM FINDER
    if message.content.startswith("$find-name"):
        nim = message.content.split("$find-name", 1)[1].strip()
        name = nim_api.find_name(nim)
        await message.channel.send(name)

    if message.content.startswith("$find-nim"):
        name = message.content.split("$find-nim", 1)[1].strip()
        nim = nim_api.find_nim(name)
        await message.channel.send(nim)

client.run(TOKEN)
