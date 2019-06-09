import discord
import weather
from discord.ext import commands

token = open("token.txt", "r").read()

bot = commands.Bot(command_prefix='bonk.')


def get_channel_info():
    server = bot.get_guild(403553600384794624)
    print(server.name)
    channels = {}
    for channel in server.channels:
        channels[channel.name] = channel

    return channels


@bot.command()
async def kill(ctx):
    if str(ctx.author) == "felix#2578":
        await ctx.send('Goodbye. Shutting down.')
        await bot.close()


@bot.command()
async def forecast(ctx, city, country=""):
    result = weather.get_current_weather(city, country)
    await ctx.send(result)


@bot.event
async def on_ready():
    print(f'We are logged in as {bot.user}')


@bot.event
async def on_message(message):
    print(f"{message.author} in {message.channel}: \"{message.content}\"")
    await bot.process_commands(message)


@bot.event
async def on_member_update(before, after):
    if str(after) == "felix#2578" and str(after.status) == "offline":
        channels = get_channel_info()
        await channels['bot-test'].send(content="Felix has logged off! REEEE!!", tts=True)


bot.run(token)
