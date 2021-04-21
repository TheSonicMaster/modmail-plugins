import discord
from os import system
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def uname(self, ctx, *, message):
        """Similar to echo, but repeats the output several times."""
        await ctx.send(system("uname -vrms"))

def setup(bot):
    bot.add_cog(Say(bot))
