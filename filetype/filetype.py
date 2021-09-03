import discord
import os
from discord.ext import commands
from datetime import datetime

class filetype(commands.Cog):
    """Detect file type of attached files."""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(invoke_without_command=True)
    @commands.Cog.listener()
    async def on_message(self, ctx, *, message):
        attachment = message.attachments[0]
        url = attachment.url
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "/tmp/" + timestamp
        os.popen("curl -Ls " + url + " -o " + file)
        stream = os.popen("file " + file)
        output = stream.read()
        await ctx.send(output)
def setup(bot):
    bot.add_cog(filetype(bot))
