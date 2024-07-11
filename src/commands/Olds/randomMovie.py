# '''
# File: randomMovie.py
# Project: commands
# File Created: Thursday, 11th July 2024 10:31:55 pm
# Author: Diveer (yosefbesher34@gmail.com)
# -----
# Last Modified: Thursday, 11th July 2024 11:55:13 pm
# -----
# Copyright 2024
# Thanks For Using My Projects
# '''


# import random
# import discord
# import discord.bot
# from discord.ext import commands

# import aiohttp
# import json

# from src.utils import utilities


# class random_movie(commands.Cog):
#   def __init__(self, bot: discord.Bot):
#     self.bot: discord.Bot = bot

#   @commands.slash_command(name="random", description="Get Info About A Random Movie")
#   async def info_random_movie(self, ctx: discord.ApplicationContext) -> None:
#     n1 = random.randint(0, 9)
#     n2 = random.randint(0, 9)
#     n3 = random.randint(0, 9)
#     n4 = random.randint(0, 9)
#     n5 = random.randint(0, 9)
#     n6 = random.randint(0, 9)
#     n7 = random.randint(0, 9)

#     url = f"http://www.omdbapi.com/?t=tt{n1}{n2}{n3}{n4}{n5}{n6}{n7}&apikey=11634dc"
#     async with aiohttp.ClientSession() as session:
#       async with session.get(url) as resp:
#         info = json.loads(await resp.text())
#         if info['Response'] != 'False':
#           embed = utilities.embed_maker(info)
#           await ctx.send_response(embed=embed)
#         else:
#           error = f'Try Again ! Code: tt{n1}{n2}{n3}{n4}{n5}{n6}{n7}'
#           await ctx.send_response(error)



# def setup(bot: discord.Bot):
#   bot.add_cog(random_movie(bot))
