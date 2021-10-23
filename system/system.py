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
            outfile = open("output.txt","w")
            outfile.write(output)
            outfile.close()
            await ctx.send("The output was greater than 2000 characters, so I have attached it as a text document.")
            await ctx.send(file=discord.File(f"output.txt"))
        else:
            await ctx.send("```\n" + output + "\n```")
def setup(bot):
    bot.add_cog(Say(bot))
