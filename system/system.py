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
            await ctx.send("Command produced no output, but exited successfully (code 0).")
        elif len(output) > 2000:
            await ctx.send("Character count of the command output (" + str(len(output)) + ") is greater than the Discord limit (2000); cannot display output.")
        else:
            await ctx.send("```\n" + output + "\n```")

def setup(bot):
    bot.add_cog(Say(bot))
