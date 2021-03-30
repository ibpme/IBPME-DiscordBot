import discord
import asyncio
from secret import TOKEN
import nim_api
import gpa_api
import jokes_api
from keep_alive import keep_alive

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

    if message.content.startswith('$dev'):
        await message.channel.send('**IBPME-Bot** is developed by **Iman-Budi Pranakasih**\nTo help contribute view this repo on github: https://github.com/ibpme/IBPME-DiscordBot')

    if message.content.startswith('$help') or message.content.startswith('$?'):
        with open('commands.png', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send('More info on : https://github.com/ibpme/IBPME-DiscordBot/blob/main/README.md', file=picture)

    # NIM FINDER
    if message.content.startswith("$find-name"):
        nim = message.content.split("$find-name", 1)[1].strip()
        name = nim_api.find_name(nim)
        await message.channel.send(name)

    if message.content.startswith("$find-nim"):
        name = message.content.split("$find-nim", 1)[1].strip()
        nim = nim_api.find_nim(name)
        await message.channel.send(nim)

    # GPA CALC
    if message.content.startswith("$gpa-calc"):
        command = message.content.split("$gpa-calc", 1)[
            1]
        if "initial" in command:
            initial_gpa, total_credit = gpa_api.parse_command(command)
            gpa = gpa_api.calc_gpa_string(
                command, inital_gpa=initial_gpa, total_credit=total_credit)
        else:
            gpa = gpa_api.calc_gpa_string(command)

        await message.channel.send(gpa)

    # JOKES GENERATOR
    if message.content.startswith("$jokes") or message.content.startswith("$receh"):
        question, answer = jokes_api.get_random_joke()
        await message.channel.send(question)
        await asyncio.sleep(2)
        await message.channel.send(answer)


keep_alive()
client.run(TOKEN)
