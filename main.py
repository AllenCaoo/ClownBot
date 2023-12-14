import warnings
import discord

import question_ping
import utils
from facial_recognition_haar import run
from facial_recognition_CNN import draw_nose
import random
from discord.ext import commands

owner_id = str(open(".info/owner_id.txt", "r").read()).replace(" ", "")  # put your id in .info/owner_id.txt
token = open(".info/token.txt", "r").read()  # put your bot token.txt in .info/owner_id.txt
bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())
warnings.filterwarnings("ignore", category=UserWarning)


@bot.event
async def on_ready():
    print("ClownBot is good to go!")
    print("The owner is {owner}".format(owner=owner_id))
    print("Servers this bot is on: ")
    servers = bot.guilds
    for i in range(len(servers)):
        print("{number}. {server_name}".format(number=i + 1, server_name=servers[i]))


@bot.command(brief='Ask me a yes/no question and I will reply',
             description="'.ask Am I beautiful' and I will reply yes - you are c:")
async def ask(ctx):
    print("{author} asks {question}".format
          (author=ctx.message.author, question=ctx.message.content))
    question = ctx.message.content[5:].lower().split()  # ".ask " is 4 characters long
    print(question)
    if question[0] not in utils.yes_no_questions:
        await ctx.send("I don't know ask Pennywise.")
    else:
        num = random.randint(0, 1)
        if num == 0:
            await ctx.send('yes')
        else:
            await ctx.send('no')


@bot.command(brief='ClownBot is happy and will celebrate in chat',
             description='I will put some emojis in the chat in which this command is typed')
async def celebrate(ctx):
    lst = [utils.circus_tent, utils.partying_face]  # Maybe add more emojis
    num_emojis = random.randint(3, 10)  # Choose random number of emojis between 3 and 10
    rev = ""
    for _ in range(num_emojis):
        index = random.randint(0, len(lst) - 1)
        rev += lst[index]
    await ctx.send(rev)


@bot.command(brief='Submit an attachment of a person and I will clown them',
             description="Upload a file --> type .clown in 'add comment'")
async def clown(ctx):
    if len(ctx.message.attachments) < 1:
        await ctx.send("Give me an image you clown...")
    elif len(ctx.message.attachments) > 1:
        await ctx.send("Only send one attachment you clown...")
    else:
        attachment = ctx.message.attachments[0]  # first attachment object
        print('{author} clowned {attachment}'.format(author=ctx.message.author, attachment=attachment))
        url = attachment.url
        if len(url) < 6:
            await ctx.send("Cannot read file")
        # elif not utils.is_image(url):
        #     await ctx.send("Only jpg and png please.")
        else:
            try:
                in_path = 'images/recent_in.jpg'
                out_path = 'images/recent_out.jpg'
                await attachment.save(in_path)
                found_face = draw_nose(in_path)
                if not found_face:
                    await ctx.send("Please submit an image with more distinct facial features.")
                else:
                    await ctx.send(file=discord.File(out_path))
            except:
                await ctx.send("It don't work")


@bot.command(brief='Submit an attachment of an image and I will question ping it',
             description="Upload a file --> type .ping in 'add comment'")
async def ping(ctx):
    if len(ctx.message.attachments) < 1:
        await ctx.send("Give me an image you clown...")
    elif len(ctx.message.attachments) > 1:
        await ctx.send("Only send one attachment you clown...")
    else:
        attachment = ctx.message.attachments[0]  # first attachment object
        print('{author} pinged {attachment}'.
              format(author=ctx.message.author, attachment=attachment))
        url = attachment.url
        if len(url) < 6:
            await ctx.send("Cannot read file")
        elif not utils.is_image(url):
            await ctx.send("Only jpg and png please.")
        else:
            in_path = 'images/recent_in.jpg'
            out_path = 'images/recent_out.jpg'
            await attachment.save(in_path)
            question_ping.draw_pings(in_path)
            await ctx.send(file=discord.File(out_path))


@bot.command(brief="Shows how trash Allen's internet is")
async def latency(ctx):
    await ctx.send('{latency} ms'.format(latency=bot.latency * 1000))


if __name__ == '__main__':
    bot.run(token)
