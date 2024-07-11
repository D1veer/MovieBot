'''
File: main.py
Project: Movies
File Created: Thursday, 11th July 2024 9:37:49 pm
Author: Diveer (yosefbesher34@gmail.com)
-----
Last Modified: Thursday, 11th July 2024 11:48:19 pm
-----
Copyright 2024
Thanks For Using My Projects
'''

import os
from discord.ext import commands
import discord.bot
from src import config

bot = commands.Bot(
  command_prefix="!",
  help_command=None,
  activity=discord.Activity(type=discord.ActivityType.streaming, name='Made By @Diveer.'),
  status=discord.Status.idle,
  case_insensitive=True,
  intents=discord.Intents.all()
)


for filename in os.listdir("./src/commands"):
  if filename.endswith(".py"):
    bot.load_extension(f"src.commands.{filename[:-3]}")
    print(f'\n✅ | Loaded src.commands.{filename[:-3]} Successfully.')
print(f'-' * 50, '\n✅ | Loaded Extensions Successfully.\n\n')


@bot.event
async def on_ready() -> None:
  print('Try To Connoting To Discord..')
  print(f'Connected To Discord Discord as {bot.user.display_name}')


bot.run(config.TOKEN)
