'''
File: infoMovie.py
Project: commands
File Created: Thursday, 11th July 2024 9:37:49 pm
Author: Diveer (yosefbesher34@gmail.com)
-----
Last Modified: Thursday, 11th July 2024 11:55:08 pm
-----
Copyright 2024
Thanks For Using My Projects
'''


import discord
import discord.bot
from discord.ext import commands

import aiohttp
import json
from src.utils import utilities

class info_movie(commands.Cog):
  moviesCommands = discord.SlashCommandGroup("movie", "Everything the bots Offer About Movies")
  
  def __init__(self, bot: discord.Bot):
    self.bot: discord.Bot = bot

  @moviesCommands.command(name="info", description="Get Info About Any Movie")
  async def info_about_movie(self, ctx: discord.ApplicationContext, name) -> None:
    url = f"http://www.omdbapi.com/?t={name}&apikey=11634dc&type=movie"

    async with aiohttp.ClientSession() as session:
      async with session.get(url) as resp:
        info = json.loads(await resp.text())
        
        embed = utilities.embed_maker(info)
        await ctx.send_response(embed=embed)
  
  @moviesCommands.command(name="search", description="Search About Any Movie")
  async def search_about_movie(self, ctx: discord.ApplicationContext, name) -> None:
    url = f"http://www.omdbapi.com/?s={name}&apikey=11634dc&type=movie"

    async with aiohttp.ClientSession() as session:
      async with session.get(url) as resp:
        info = json.loads(await resp.text())
        options = []
        
        if info["Search"]:
          for i in info["Search"]:
            options.append(discord.SelectOption(label=f"{i['Title']}-{i["Year"]}",description="T"))
        
        class MyView(discord.ui.View):
          @discord.ui.select( 
            placeholder = "Choose A Movie", # the placeholder text that will be displayed if nothing is selected
            min_values = 1, # the minimum number of values that must be selected by the users
            max_values = 1, # the maximum number of values that can be selected by the users
            options = options
          )
          
          async def select_callback(self, select, interaction): # the function called when the user is done selecting options
            urls = f"http://www.omdbapi.com/?t={select.values[0][:-5]}&apikey=11634dc&type=movie"
            async with aiohttp.ClientSession() as session:
              async with session.get(urls) as resp:
                info = json.loads(await resp.text())
                
                embed = utilities.embed_maker(info)
                await interaction.response.send_message(embed=embed)
        await ctx.send_response(view=MyView())


def setup(bot: discord.Bot):
  bot.add_cog(info_movie(bot))
