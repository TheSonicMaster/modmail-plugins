from discord.ext import commands

class umfix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 735550905721684098:
            words = message.content.lower().split(" ")
            for word in words:
                if i.startswith("uh"):
                    await message.delete()
                    await message.author.send("Hey you used uh again stop it")
                elif i.startswith("um"):
                    await message.delete()
                    await message.author.send("Hey you used um again stop it")
                elif i.startswith("cuz"):
                    await message.delete()
                    await message.author.send("Hey you used cuz again stop it")
                    
 
def setup(bot):
    bot.add_cog(umfix(bot))
