#!/usr/bin/env python3

# I've had enough. FINALLY a profanity filter done right.

# Required modules.
import discord
from discord.ext import commands
from datetime import datetime

# Profane words.
with open("wordlist.txt") as file:
    words = file.read().splitlines()

# Log channel.
logchannel = discord.utils.get(ctx.guild.text_channels, name = "modlog")

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
                    await self.bot.get_channel(logchannel).send(embed=log)
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
                    await self.bot.get_channel(logchannel).send(embed=log)
                    break

def setup(bot):
    bot.add_cog(profanitydoneright(bot))
