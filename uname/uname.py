import discord
import os
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def uname(self, ctx, *, message):
        """A buggy implimentation of uname from GNU Coreutils."""
        command = "uname " + message + " 2>&1"
        stream = os.popen(command)
        output = stream.read()
        await ctx.send(output)

def setup(bot):
    bot.add_cog(Say(bot))
