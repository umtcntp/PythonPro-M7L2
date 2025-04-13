import discord
from discord.ext import commands
from config import token
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./images/{file_name}')
            #await ctx.send(f"Saved the image to ./images/{file_name}")
            result = get_class(model_path='./keras_model.h5', labels_path='./labels.txt', image_path=f'./images/{file_name}')[0]
            if result == "Güvercin\n":
                await ctx.send("This is a pigeon, for more info check the link: https://en.wikipedia.org/wiki/Pigeon")
            elif result == "Serçe\n":
                await ctx.send("This is a sparrow, for more info check the link: https://en.wikipedia.org/wiki/Sparrow")
            else:
                await ctx.send("I couldn't recognize the bird, please try again with a different image")
    else:
        await ctx.send("You forgot the upload the image")

bot.run(token)