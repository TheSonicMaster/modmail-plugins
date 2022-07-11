import discord
import requests
from datetime import datetime
from discord.ext import commands

class phishingdetector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        r = requests.get("https://raw.githubusercontent.com/nikolaischunk/discord-phishing-links/main/txt/domain-list.txt")
        self.links = r.text.split("\n")
        self.links.pop()

    @commands.Cog.listener()
    async def on_message(self, message):
        for link in self.links:
            if f"http://{link}" in message.content.lower() or f"https://{link}" in message.content.lower():
                await message.delete()
                await message.channel.send(f"{message.author.mention} No phishing links allowed.", delete_after=3)
                log = discord.Embed(color=self.bot.main_color, description="**Phishing link (" + link + ") detected and deleted at** " + message.channel.mention + "\n" + message.content)
                log.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                log.timestamp = datetime.utcnow()
                await self.bot.get_channel(611613073039687701).send(embed=log)
                return

def setup(bot):
    bot.add_cog(phishingdetector(bot))
