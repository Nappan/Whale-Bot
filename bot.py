#Imports
import discord
from discord.ext import commands

TOKEN = 'ODE0MzA2MDU4OTkwMTI1MTQ2.YDb7nQ._yhoio-E5Xrfgqv1mgCBGCim5e4'

#Initiating bot
bot = commands.Bot(command_prefix='!')

#commands
@bot.command()
async def test(ctx,arg):
    await ctx.send(arg)

bot.run(TOKEN)