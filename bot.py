import discord
import jishaku
import os
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='t.')
bot.remove_command('help')

bot.load_extension('jishaku')

@bot.event
async def on_ready():
    print(f'Bot is connect')
    await bot.change_presence(status = discord.Status.online, activity = discord.Game('TEST JSK'))

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! My name is **Tester Bot** and i help testing commands for Python!")

token = os.environ.get("Token")
bot.run(str(token))
