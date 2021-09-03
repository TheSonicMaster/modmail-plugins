import discord
import os
from discord.ext import commands
from datetime import datetime

class filetype(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def filetype(self, ctx):
        """Detect file type of attached files."""
        attachment = ctx.message.attachments[0]
        url = attachment.url
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "/tmp/" + timestamp
        os.popen("curl -Ls " + url + " -o " + file)
        stream = os.popen("file " + file)
        output = stream.read()
        print(output)
def setup(bot):
    bot.add_cog(filetype(bot))
