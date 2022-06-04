import discord
from discord.ext import commands
from datetime import datetime

links = [
    "partpicker.shop",
    "websafe.online",
    "sportshub.bar",
    "herald.sbs",
    "locations.quest",
    "lovebird.guru",
    "trulove.guru",
    "dateing.club",
    "shrekis.life",
    "headshot.monster",
    "gaming-at-my.best",
    "progaming.monster",
    "yourmy.monster",
    "imageshare.best",
    "screenshot.best",
    "gamingfun.me",
    "catsnthing.com",
    "catsnthings.fun",
    "curiouscat.club",
    "joinmy.site",
    "fortnitechat.site",
    "fortnight.space",
    "freegiftcards.co",
    "stopify.co",
    "leancoding.co",
    "grabify.link",
]
class ipgrabdetector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore DMs.
        if isinstance(message.channel, discord.channel.DMChannel):
            return
        for link in links:
            if link in message.content:
                await message.delete()
                await message.channel.send(f"{message.author.mention} Your message has been deleted for containing an IP grabber link.", delete_after=3)
                grabber = discord.Embed(color=self.bot.main_color, description="**IP grabber link detected at** " + message.channel.mention + "\n" + link)
                grabber.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                grabber.timestamp = datetime.utcnow()
                await self.bot.get_channel(611613073039687701).send(embed=grabber)
                break

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        # Ignore DMs.
        if isinstance(message.channel, discord.channel.DMChannel):
            return
        for link in links:
            if link in after.content:
                await after.delete()
                await after.channel.send(f"{after.author.mention} Your message has been deleted for containing an IP grabber link.", delete_after=3)
                grabber = discord.Embed(color=self.bot.main_color, description="**IP grabber link detected at** " + after.channel.mention + "\n" + link)
                grabber.set_author(name=after.author.name, icon_url=after.author.avatar_url)
                grabber.timestamp = datetime.utcnow()
                await self.bot.get_channel(611613073039687701).send(embed=grabber)
                break

def setup(bot):
    bot.add_cog(ipgrabdetector(bot))
