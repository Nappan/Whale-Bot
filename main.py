#Imports
import discord
from discord.ext import commands
import os

#Initiating bot
bot = commands.Bot(command_prefix='!')
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

#commands
@bot.command()
async def test(ctx,arg):
    await ctx.send(arg)

bot.run(TOKEN)