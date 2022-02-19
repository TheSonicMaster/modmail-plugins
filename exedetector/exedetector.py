from discord.ext import commands
from discord import Embed

import datetime

class exedetector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.filename.lower().endswith(".exe"):
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} Please do not send executable files. You may send a link to the website/webpage where they may be obtained from instead.", delete_after=3)
                    exe = Embed(color=self.bot.main_color, description="**Exe detected at **" + message.channel.mention + "\n" + attachment.url)
                    exe.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                    exe.timestamp = datetime.datetime.utcnow()
                    await self.bot.get_channel(611613073039687701).send(embed=exe)

def setup(bot):
    bot.add_cog(exedetector(bot))
