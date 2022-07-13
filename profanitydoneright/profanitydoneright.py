#!/usr/bin/env python3

# I've had enough. FINALLY a profanity filter done right.
# It also has state-of-the-art technology to allow detection of profane images.

# Required modules.
import discord
from discord.ext import commands
from datetime import datetime
from requests import get
import os
from pathlib import Path as path
from stat import S_IEXEC
from PIL import Image
import pytesseract

# Download required stuff.
TESSVER = "5.2.0"
tessbin = get("https://github.com/DanielMYT/tesseract-static/releases/download/tesseract-" + TESSVER + "/tesseract")
with open("tesseract","wb") as f:
    f.write(tessbin.content)
f.close()
path("tessdata").mkdir(parents=True,exist_ok=True)
tessdat = get("https://raw.githubusercontent.com/tesseract-ocr/tessdata/4.1.0/eng.traineddata")
with open("tessdata/eng.traineddata","wb") as f:
    f.write(tessdat.content)
f.close()

# Load list of profane words.
with open("plugins/TheSonicMaster/modmail-plugins/profanitydoneright-master/wordlist.txt", "r") as wordlist:
    words = wordlist.read().splitlines()
wordlist.close()

# Whitelisted channels.
safechannels = [639525202732253204, 804090051285352508, 583379256441045012, 583379256441045012, 611613073039687701]

# Strip these out to prevent bypassing.
stripchars = "!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# Setup tesseract.
os.chmod("tesseract",os.stat("tesseract").st_mode | S_IEXEC)
pytesseract.pytesseract.tesseract_cmd = r'./tesseract'
tessdata = r'--tessdata-dir "tessdata"'

class profanitydoneright(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore DMs.
        if isinstance(message.channel, discord.channel.DMChannel):
            return
        # Skip whitelisted channels and owner.
        for chan in safechannels:
            if message.channel.id == chan:
                return
        if message.author.id == 494884004068327425:
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
                                os.remove(img)
                                return
                    os.remove(img)

    @commands.Cog.listener()
    async def on_message_edit(self, orig, message):
        # Ignore DMs.
        if isinstance(message.channel, discord.channel.DMChannel):
            return
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
                                os.remove(img)
                                return
                    os.remove(img)

def setup(bot):
    bot.add_cog(profanitydoneright(bot))
