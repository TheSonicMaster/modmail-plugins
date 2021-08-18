import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def echo(self, ctx, *, message):
        """Echos your message back to you!"""
        await ctx.send("Message sent by + " str(ctx.author) + "using `+echo` command:\n" + message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere"))

def setup(bot):
    bot.add_cog(Say(bot))
