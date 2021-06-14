import discord
import cv2
from face_recognition import run
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print("ClownBot is good to go!")


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
    print(attachment)
    url = attachment.url
    if not url[-3:] == 'jpg' and not url[-3:] == 'png':
        await ctx.send("Only jpg and png please.")
    else:
        file_path = 'images/recent_in.jpg'
        await attachment.save(file_path)
        run(file_path)
        await ctx.send(file=discord.File('images/recent_out.jpg'))


token = input("What is your bot token? ")
bot.run(token)
