import discord
import os
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def system(self, ctx, *, message):
        """Run system (shell) commands directly from Discord! By The Sonic Master."""
        command = message + " 2>&1"
        stream = os.popen(command)
        output = stream.read()
        if output == "":
            await ctx.send("Command produced no output.")
        elif len(output) > 2000:
            output = output[0:2000]
        else:
            await ctx.send("Warning: output trucated to 2000 characters because it exceeded the Discord character count limit\n```\n" + output + "\n```")

def setup(bot):
    bot.add_cog(Say(bot))
