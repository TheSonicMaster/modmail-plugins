import discord
import subprocess
from discord.ext import commands

class system(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def system(self, ctx, *, message):
        """Run system (shell) commands directly from Discord! By The Sonic Master."""
        async with ctx.typing():
            command = message + " 2>&1"
            command = ''.join(command).split()
            try:
                output = subprocess.run(command, capture_output=True, text=True, check=True, timeout=20)
            except subprocess.TimeoutExpired:
                error = True
        if error:
            await ctx.send("Error timeout of 20 seconds has expired")
        elif output == "":
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
    bot.add_cog(system(bot))
