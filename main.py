import discord
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

token = input("What is your bot token? ")
bot.run(token)