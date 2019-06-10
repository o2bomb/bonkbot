import discord
import weather
import texttospeech
from discord.ext import commands

token = open("tokens/token.txt", "r").read()

bot = commands.Bot(command_prefix='bonk.')


def get_channel_info():
    # @Improve
    # Returns all the channels as a dictionary,
    # where key = channel_name and value = channel_object
    server = bot.get_guild(403553600384794624)
    print(server.name)
    channels = {}
    for channel in server.text_channels:
        channels[channel.name] = channel

    return channels


@bot.command()
async def kill(ctx):
    if str(ctx.author) == "felix#2578":
        await ctx.send('Goodbye. Shutting down.')
        await bot.close()


@bot.command()
async def tts(ctx, source, language="en-us", speed="0"):
    # @Improve
    vc = ctx.author.voice
    if vc is not None:    # If the author of the command is in a voice channel
        texttospeech.get_tts(source, language, speed)
        stream = await vc.channel.connect()
    else:
        print("Error: TTS failed. Author is not in a voice channel.")


@bot.command()
async def forecast(ctx, city, country=""):
    # @Improve
    # Gets the current forecast for the specified city and bulids
    # an embed object to display in the author's channel
    result = weather.get_current_weather(city, country)
    forecast_embed = discord.Embed(title="Forecast", description=f"Today's forecast for {city}, {result['sys']['country']}", color=0x4d5ef7)
    forecast_embed.set_image(url=f"https://openweathermap.org/img/w/{result['weather'][0]['icon']}.png")
    forecast_embed.add_field(name=f"Average: {result['main']['temp']}°C", value=f"Min: {result['main']['temp_min']}°C, Max: {result['main']['temp_max']}°C", inline=True)
    forecast_embed.add_field(name=f"{result['weather'][0]['main']}", value=f"{result['weather'][0]['description']}", inline=True)
    forecast_embed.set_footer(text="Weather data provided by OpenWeatherMaps")
    await ctx.send(embed=forecast_embed)


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
