#!/usr/bin/env python3

# I've had enough. FINALLY a profanity filter done right.

# Required modules.
import discord
from discord.ext import commands
from datetime import datetime

# Load list of profane words.
with open("plugins/TheSonicMaster/modmail-plugins/profanitydoneright-master/wordlist.txt", "r") as wordlist:
    words = wordlist.read().splitlines()

# Whitelisted channels.
safechannels = [639525202732253204, 804090051285352508, 583379256441045012, 583379256441045012, 611613073039687701]

# Strip these out to prevent bypassing.
stripchars = "!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~"

class profanitydoneright(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        for chan in safechannels:
            if message.channel.id == chan:
                return
        for word in words:
            for uword in message.content.lower().split(" "):
                uword = uword.strip(stripchars)
                if uword == word:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} No profanity allowed.", delete_after=3)
                    log = discord.Embed(color=self.bot.main_color, description="**Profanity (" + word + ") detected and deleted at** " + message.channel.mention + "\n" + message.content)
                    log.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                    log.timestamp = datetime.utcnow()
                    await self.bot.get_channel(611613073039687701).send(embed=log)
                    return

    @commands.Cog.listener()
    async def on_message_edit(self, orig, message):
        for chan in safechannels:
            if message.channel.id == chan:
                return
        for word in words:
            for uword in message.content.lower().split(" "):
                uword = uword.strip(stripchars)
                if uword == word:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} No profanity allowed.", delete_after=3)
                    log = discord.Embed(color=self.bot.main_color, description="**Profanity (" + word + ") detected and deleted at** " + message.channel.mention + "\n" + message.content)
                    log.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                    log.timestamp = datetime.utcnow()
                    await self.bot.get_channel(611613073039687701).send(embed=log)
                    return

def setup(bot):
    bot.add_cog(profanitydoneright(bot))
