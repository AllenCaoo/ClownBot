import warnings
import discord
from facial_recognition_haar import run
from facial_recognition_CNN import draw_nose
import random
from discord.ext import commands

owner_id = open(".info/owner_id.txt", "r").read()  # put your id in .info/owner_id.txt
token = open(".info/token.txt", "r").read()  # put your bot token.txt in .info/owner_id.txt
bot = commands.Bot(command_prefix='.')
warnings.filterwarnings("ignore", category=UserWarning)


@bot.event
async def on_ready():
    print("ClownBot is good to go!")
    print("The owner is {owner}".format(owner=str(owner_id)))
    print("Servers this bot is on: ")
    servers = bot.guilds
    for i in range(len(servers)):
        print("{number}. {server_name}".format(number=i + 1, server_name=servers[i]))


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
    await ctx.send('{latency} ms'.format(latency=bot.latency*1000))


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
    if len(ctx.message.attachments) < 1:
        await ctx.send("Give me an image you clown...")
    elif len(ctx.message.attachments) > 1:
        await ctx.send("Only send one attachment you clown...")
    attachment = ctx.message.attachments[0]  # first attachment object
    print('{author} clowned {attachment}'.format(author=ctx.message.author, attachment=attachment))
    url = attachment.url
    if len(url) < 6:
        await ctx.send("Cannot read file")
    elif not url[-3:] == 'jpg' and not url[-3:] == 'png' \
            and not url[-3:] == 'JPG' and not url[-4] == 'jpeg':
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


bot.run(token)
