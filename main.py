import discord
import cv2
from face_recognition import run
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print("ClownBot is good to go!")

@bot.command()
async def latency(ctx):
    await ctx.send(f'{int(bot.latency * 1000)} ' + 'ms')
    
@bot.command()
async def ask(ctx):
    num = random.randint(0, 1)
    if num == 0:
        await ctx.send('yes')
    else:
        await ctx.send('no')

@bot.event
async def on_message(ctx):
    print("DEBUG:", ctx.attachments)

@bot.command()
async def clown(ctx):
    info = ctx.attachments
    url = info['url']
    if len(info) < 0:
        await ctx.send("Give me an image you clown...")
    elif not url[-3:] == 'jpg' and not url[-3:] == 'png':
        await ctx.send("Only jpg and png please.")
    else:
        file = await info[0].to_file()
        file.filename = 'recent.png'
        embed = discord.Embed()
        embed.set_image(url='attachment://recent.png')
        await ctx.send(file=file, embed=embed)

token = input("What is your bot token? ")
bot.run(token)