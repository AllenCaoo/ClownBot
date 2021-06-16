import warnings

import cv2
import discord
from facial_recognition_haar import run
from facial_recognition_CNN import draw_nose
import random
from discord.ext import commands

owner_id = open(".info/owner_id.txt", "r").read()  # put your id in .info/owner_id.txt
bot = commands.Bot(command_prefix='.')
warnings.filterwarnings("ignore", category=UserWarning)

@bot.event
async def on_ready():
    print("ClownBot is good to go!")
    print(f"The owner is {owner_id}")


@bot.command()
async def stop(ctx):
    if str(ctx.message.author.id) == str(owner_id):
        await ctx.message.delete()
        while True:
            words = input("What would you like to say? ")
            if words == 'q':
                break
            await ctx.message.channel.send(words)
    else:
        await ctx.message.channel.send("Only Allen tells me to stop")


@bot.command(brief="Shows how trash Allen's internet is")
async def latency(ctx):
    await ctx.send(f'{int(bot.latency * 1000)} ' + 'ms')


@bot.command(brief='Ask me a yes/no question and I will reply',
             description="'.ask Am I beautiful' and I will reply yes - you are c:")
async def ask(ctx):
    num = random.randint(0, 1)
    if num == 0:
        await ctx.send('yes')
    else:
        await ctx.send('no')


@bot.command(brief='Submit an attachment of a person and I will clown them',
             description="Upload a file --> type .clown in 'add comment'")
async def clown(ctx):
    if len(ctx.message.attachments) < 0:
        await ctx.send("Give me an image you clown...")
    elif len(ctx.message.attachments) > 1:
        await ctx.send("Only send one attachment you clown...")
    attachment = ctx.message.attachments[0]  # first attachment object
    print(f'{ctx.message.author} clowned {attachment}')
    url = attachment.url
    if not url[-3:] == 'jpg' and not url[-3:] == 'png' and not url[-3:] == 'JPG':
        await ctx.send("Only jpg and png please.")
    else:
        in_path = 'images/recent_in.jpg'
        out_path = 'images/recent_out.jpg'
        await attachment.save(in_path)
        found_face = draw_nose(in_path)
        if not found_face:
            await ctx.send("Please submit an image with more distinct facial features.")
        else:
            await ctx.send(file=discord.File(out_path))


token = input("What is your bot token? ")
bot.run(token)
