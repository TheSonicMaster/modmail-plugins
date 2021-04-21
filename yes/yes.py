import discord
from random import randint as select
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def echo(self, ctx, *, message):
        """Similar to echo, but repeats the output several times."""
        loopcount = select(1,10)
        for i in range(1,loopcount):
            await ctx.send(message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere"))

def setup(bot):
    bot.add_cog(Say(bot))
