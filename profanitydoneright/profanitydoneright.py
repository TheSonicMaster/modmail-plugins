#!/usr/bin/env python3

# I've had enough. FINALLY a profanity filter done right.

# Required modules.
import discord
from discord.ext import commands
from requests import get
from datetime import datetime

# Load list of profane words.
url = "https://raw.githubusercontent.com/TheSonicMaster/modmail-plugins/master/profanitydoneright/wordlist.txt"
words = get(url).text.split("\n")

class profanitydoneright(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        for word in words:
            for uword in message.content.lower().strip("!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~").split(" "):
                if uword == word:
                    await message.delete()
                    await after.channel.send(f"{after.author.mention} No profanity allowed.", delete_after=3)
                    log = discord.Embed(color=self.bot.main_color, description="**Profanity detected and deleted at** " + message.channel.mention + "\n" + word)
                    log.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                    log.timestamp = datetime.utcnow()
                    await self.bot.get_channel(611613073039687701).send(embed=log)
                    break

    @commands.Cog.listener()
    async def on_message_edit(self, orig, message):
        for word in words:
            for uword in message.content.lower().strip("!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~").split(" "):
                if uword == word:
                    await message.delete()
                    await after.channel.send(f"{after.author.mention} No profanity allowed.", delete_after=3)
                    log = discord.Embed(color=self.bot.main_color, description="**Profanity detected and deleted at** " + message.channel.mention + "\n" + word)
                    log.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                    log.timestamp = datetime.utcnow()
                    await self.bot.get_channel(611613073039687701).send(embed=log)
                    break

def setup(bot):
    bot.add_cog(profanitydoneright(bot))
