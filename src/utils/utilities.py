'''
File: utilities.py
Project: utils
File Created: Thursday, 11th July 2024 9:37:49 pm
Author: Diveer (yosefbesher34@gmail.com)
-----
Last Modified: Friday, 12th July 2024 12:59:06 am
-----
Copyright 2024
Thanks For Using My Projects
'''


from discord import Role, Member, User, Embed
from discord.ext import commands
from .. import config

import datetime

rates = {
  "G": "https://help.imdb.com/article/contribution/titles/certificates/GU757M8ZJ9ZPXB39?ref_=helpart_nav_27#:~:text=G%20%2D-,For%20all%20audiences,-PG%20%2D%20Parental%20Guidance",
  "PG": "https://help.imdb.com/article/contribution/titles/certificates/GU757M8ZJ9ZPXB39?ref_=helpart_nav_27#:~:text=Parental%20Guidance%20Suggested%20(mainly%20for%20under%2010%27s)",
  "PG-13": "https://help.imdb.com/article/contribution/titles/certificates/GU757M8ZJ9ZPXB39?ref_=helpart_nav_27#:~:text=PG%2D13%20%2D-,Parental%20Guidance%20Suggested%20for%20children%20under%2013,-R%20%2D%20Under%2017",
  "R": "https://help.imdb.com/article/contribution/titles/certificates/GU757M8ZJ9ZPXB39?ref_=helpart_nav_27#:~:text=Under%2017%20not%20admitted%20without%20parent%20or%20guardian",
  "NC-17": "https://help.imdb.com/article/contribution/titles/certificates/GU757M8ZJ9ZPXB39?ref_=helpart_nav_27#:~:text=NC%2D17%20%2D-,Under%2017%20not%20admitted,-Approved%20%2D%20Pre%2D1968",
  "N/A": "N/A"
}

def check_staff(ctx: commands.Context, user: Member | User) -> bool:
  """
  Checks if a user Have the `Staff` role.

  :return: Returns True if the user has the `Staff` role or False if not.
  """

  role: Role = ctx.guild.get_role(config.STAFF_ROLE_ID)

  if role in user.roles:
    return True
  else:
    return False

def embed_maker(info):
  """_summary_

  Args:
    info (_type_): _description_

  Returns:
    Embed: _description_
  """  
  
  embed = Embed(
    title=f"**{info["Title"]}**",
    description=f"{info["Plot"]}",
    colour=0xFFFFFF,
    timestamp=datetime.datetime.now(),
  )

  embed.set_author(name=f"{info["Director"]}")

  embed.add_field(
    name=":hash: Genre", value=f"{info["Genre"]}", inline=True
  )
  
  global ratted
  
  if info["Rated"] in rates:
    ratted = rates[info["Rated"]]
  else:
    ratted = 'N/A'
  
  embed.add_field(
    name=":identification_card: Rating",
    value=f"[{info["Rated"]}]({ratted})",
    inline=True,
  )

  min = [int(i) for i in f"{info["Runtime"]}".split() if i.isdigit()][0]
  h = min // 60
  m = min % 60

  embed.add_field(
    name=":hourglass_flowing_sand: Duration",
    value=f"{info["Runtime"]} ({h}h {m}m)",
    inline=True,
  )
  embed.add_field(
    name=":inbox_tray: Imdb Rating",
    value=f":arrow_up_small: {info["imdbRating"]} ({info["imdbVotes"]} Votes)",
    inline=True,
  )
  embed.add_field(name=":map: Language", value=f"{info["Language"]}", inline=True)
  embed.add_field(name=":asterisk: Type", value=f":movie_camera: {info["Type"]}", inline=True
  )
  embed.add_field(
    name=":trophy: Awards",
    value=f"{info["Awards"]}",
    inline=False,
  )

  embed.set_image(
    url=f"{info["Poster"]}"
  )

  embed.set_footer(
    text=f"Released: {info["Released"]}", icon_url="https://slate.dan.onl/slate.png"
  )

  return embed