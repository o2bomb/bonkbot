import discord
import os
import weather
import texttospeech
import textdetect
from discord.ext import commands

# @Complete = Function is complete. No further improvements necessarily needed
# @Improve = Function's performance and code can be improved on and refactored
# @Update = Function's code or features requires updating
# @Feature = Function is missing core feature(s)

token = open("tokens/token.txt", "r").read()

bot = commands.Bot(command_prefix='bonk.')


@bot.command()
async def kill(ctx):
    # @Complete
    # Shuts down the bot. Only the owner of the bot can shut it down
    if await bot.is_owner(ctx.author):
        await ctx.send('Goodbye. Shutting down.')
        await bot.close()


@bot.command(usage="bonk.texts url [language]")
async def texts(ctx, url, language="eng"):
    # Extracts the text from the specified image's URL and posts it in
    # the caller's text channel
    await ctx.send(textdetect.get_parsed_text(url, language))


@bot.command(usage="bonk.tts source [language] [speed]")
async def tts(ctx, source, language="en-us", speed="0"):
    # @Improve - Responsiveness, memory usage, documentation
    # Plays the source string as text-to-speech in the caller's voice channel
    try:
        v_state = ctx.author.voice
        guild = ctx.message.guild
        if len(source) > 60:
            await ctx.send("Source cannot be longer than 60 characters. This is to reduce memory usage and bandwidth.")
        elif v_state is not None:
            if bot.user not in v_state.channel.members:
                v_client = await v_state.channel.connect()
            else:
                v_client = guild.voice_client
            texttospeech.get_tts(source, language, speed)
            audio_src = discord.FFmpegPCMAudio('temp.mp3')
            v_client.play(audio_src)
        else:
            ctx.send("Please join a voice channel before using this command.")
    except (discord.ClientException) as e:
        if e == discord.ClientException:
            ctx.send("Please slow down. I cannot play more than one track at a time.")
        else:
            raise e


@bot.command(usage="bonk.forecast city [country]")
async def forecast(ctx, city, country=""):
    # @Update - Embedded contents, information
    # Gets the current forecast for the specified city and bulids
    # an embed object to display in the caller's text channel
    result = weather.get_current_weather(city, country)
    forecast_embed = discord.Embed(title="Forecast", description=f"Today's forecast for {city}, {result['sys']['country']}", color=0x4d5ef7)
    forecast_embed.set_image(url=f"https://openweathermap.org/img/w/{result['weather'][0]['icon']}.png")
    forecast_embed.add_field(name=f"Average: {result['main']['temp']}°C", value=f"Min: {result['main']['temp_min']}°C, Max: {result['main']['temp_max']}°C", inline=True)
    forecast_embed.add_field(name=f"{result['weather'][0]['main']}", value=f"{result['weather'][0]['description']}", inline=True)
    forecast_embed.set_footer(text="Weather data provided by OpenWeatherMaps")
    await ctx.send(embed=forecast_embed)


@bot.event
async def on_command_error(ctx, error):
    # @Update - To catch more types of errors
    # Handles all command related errors (errors that are raised when a command fails)
    ignored_err = ()

    if isinstance(error, ignored_err):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(("I cannot execute that because there are missing parameters. The correct usage for the command is:\n"
                        f"`{ctx.command.usage}`"))
    elif isinstance(error, commands.CommandNotFound):
        prediction = None
        invoked = ctx.message.content.split()
        for command in bot.commands:
            if invoked[0][5:] in command.name:
                prediction = command.name

        if prediction is not None:
            await ctx.send(f"That command does not exist. Did you mean `bonk.{prediction}`")
        else:
            await ctx.send(f"That command does not exist.")
    elif isinstance(error, commands.DisabledCommand):
        await ctx.send("That command has been disabled.")
    else:
        raise error


@bot.event
async def on_ready():
    print(f'We are logged in as {bot.user}')


@bot.event
async def on_message(message):
    print(f"{message.author} in {message.channel}: \"{message.content}\"")
    await bot.process_commands(message)


@bot.event
async def on_member_update(before, after):
    # @Improve - Code (or remove altogether)
    if str(after) == "felix#2578" and str(after.status) == "offline":
        guild = after.guild
        channels = {}
        for channel in guild.text_channels:
            channels[channel.name] = channel
        await channels['bot-test'].send(content="Felix has logged off! REEEE!!", tts=True)


bot.run(token)
