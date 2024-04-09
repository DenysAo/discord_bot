import discord
import json
from discord.ext import commands

file = open('config.json', 'r')
config = json.load(file)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(config['prefix'], intents=intents)

@bot.event
async def on_ready():
    print('bot online')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'{ctx.author.mention}pong')

@bot.command(name='foo')
async def ping(ctx: commands.context, *, args):
    await ctx.send(embed=discord.Embed(title=f'{result}', description='Hi, this is a test command', color='#64ff0a'))

bot.run(config['token'])
