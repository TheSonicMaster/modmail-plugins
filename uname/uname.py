import discord
from os import system
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def uname(self, ctx, *, message):
        """A buggy implimentation of uname from GNU Coreutils."""
        await ctx.send("test")

def setup(bot):
    bot.add_cog(Say(bot))
