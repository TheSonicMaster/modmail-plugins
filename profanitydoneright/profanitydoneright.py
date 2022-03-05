#!/usr/bin/env python3

# I've had enough. FINALLY a profanity filter done right.
# It also has state-of-the-art technology to allow detection of profane images.

# Required modules.
import discord
from discord.ext import commands
from datetime import datetime
from requests import get
from os import remove
from PIL import Image
import pytesseract

# Load list of profane words.
with open("plugins/TheSonicMaster/modmail-plugins/profanitydoneright-master/wordlist.txt", "r") as wordlist:
    words = wordlist.read().splitlines()
wordlist.close()

# Whitelisted channels.
safechannels = [639525202732253204, 804090051285352508, 583379256441045012, 583379256441045012, 611613073039687701]

# Strip these out to prevent bypassing.
stripchars = "!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# Setup tesseract.
pytesseract.pytesseract.tesseract_cmd = r'plugins/TheSonicMaster/modmail-plugins/profanitydoneright-master/tesseract/tesseract'
tessdata = r'--tessdata-dir "plugins/TheSonicMaster/modmail-plugins/profanitydoneright-master/tesseract/tessdata"'

class profanitydoneright(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Skip whitelisted channels.
        for chan in safechannels:
            if message.channel.id == chan:
                return
        # Check for profane words.
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
        # Check for attached images containing profanity.
        if message.attachments:
            for attachment in message.attachments:
                img = attachment.filename.lower()
                if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith(".png") or img.endswith(".gif") or img.endswith(".tif") or img.endswith(".tiff"):
                    getimg = get(attachment.url)
                    with open(img,"wb") as f:
                        f.write(getimg.content)
                    f.close()
                    imgwords = pytesseract.image_to_string(Image.open(img),config=tessdata).lower().split()
                    for word in words:
                        for uword in imgwords:
                            uword = uword.strip(stripchars)
                            if uword == word:
                                await message.delete()
                                await message.channel.send(f"{message.author.mention} No profane images allowed.", delete_after=3)
                                log = discord.Embed(color=self.bot.main_color, description="**Image profanity (" + word + ") detected and deleted at** " + message.channel.mention + "\n" + attachment.url)
                                log.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                                log.timestamp = datetime.utcnow()
                                await self.bot.get_channel(611613073039687701).send(embed=log)
                                remove(img)
                                return
                    remove(img)

    @commands.Cog.listener()
    async def on_message_edit(self, orig, message):
        # Skip whitelisted channels.
        for chan in safechannels:
            if message.channel.id == chan:
                return
        # Check for profane words.
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
        # Check for attached images containing profanity.
        if message.attachments:
            for attachment in message.attachments:
                img = attachment.filename.lower()
                if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith(".png") or img.endswith(".gif") or img.endswith(".tif") or img.endswith(".tiff"):
                    getimg = get(attachment.url)
                    with open(img,"wb") as f:
                        f.write(getimg.content)
                    f.close()
                    imgwords = pytesseract.image_to_string(Image.open(img),config=tessdata).lower().split()
                    for word in words:
                        for uword in imgwords:
                            uword = uword.strip(stripchars)
                            if uword == word:
                                await message.delete()
                                await message.channel.send(f"{message.author.mention} No profane images allowed.", delete_after=3)
                                log = discord.Embed(color=self.bot.main_color, description="**Image profanity (" + word + ") detected and deleted at** " + message.channel.mention + "\n" + attachment.url)
                                log.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                                log.timestamp = datetime.utcnow()
                                await self.bot.get_channel(611613073039687701).send(embed=log)
                                remove(img)
                                return
                    remove(img)

def setup(bot):
    bot.add_cog(profanitydoneright(bot))
