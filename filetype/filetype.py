import discord
import os
from discord.ext import commands
from datetime import datetime
from requests import get

class filetype(commands.Cog):
    """Detect file type of attached files."""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(invoke_without_command=True)
    @commands.Cog.listener()
    async def on_message(self, ctx, *, message):
        if message.attachments:
            await ctx.send("Checking file type of attached file...")
        attachment = message.attachments[0]
        url = attachment.url
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "/tmp/" + str(timestamp)
        downloaded = get(url)
        with open(file,"wb") as download:
            download.write(downloaded.content)
        stream = os.popen("file " + file)
        output = stream.read()
        await ctx.send(output)
def setup(bot):
    bot.add_cog(filetype(bot))
