import discord
from discord.ext import commands
from random import choice as select
class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def steal(self, ctx, *, message):
        """Steal something! Be careful not to get caught..."""
        possibleactions = ["steal","steal","getcaught"]
        action = select(possibleactions)
        if action == "steal":
            message = "You successfully stole " + message + "!"
        elif action == "getcaught":
            punishments = ["fine","comserv","prison"]
            punishment = select(punishments)
            if punishment == "fine":
                fines = ["10","50","100","250","500","1000","2500","5000"]
                amount = select(fines)
                message = "You got caught! Your punishment is a fine of $" + amount + "!"
            elif punishment == "comserv":
                possiblehours = ["10","50","100","250","500","1000","2500","5000"]
                hours = select(possiblehours)
                message = "You got caught! Your punishment is " + hours + " hours of community service!"
            elif punishment == "prison":
                possibleyears = ["1","2","3","4","5","6","7","8","9","10"]
                years = select(possibleyears)
                message = "You got caught! Your punishment is " + years + " years in prison!"
        await ctx.send(message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")

def setup(bot):
    bot.add_cog(Say(bot))
