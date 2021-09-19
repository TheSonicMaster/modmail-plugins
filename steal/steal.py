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
            super = message.lower()
            if "sonic" in super:
                print("You got caught. Everything you stole in the past has been confiscated!")
            elif "owner" in super:
                print("You got caught. Everything you stole in the past has been confiscated!")
            elif "admin" in super:
                print("You got caught. Everything you stole in the past has been confiscated!")
            else:
                message = "You successfully stole " + message + "!"
        elif action == "getcaught":
            punishments = ["fine","comserv","prison","serverban"]
            punishment = select(punishments)
            if punishment == "fine":
                fines = ["10","50","100","250","500","1000","2500","5000","10000","25000","50000","100000","250000","500000"]
                amount = select(fines)
                message = "You got caught! Your punishment is a fine of $" + amount + "!"
            elif punishment == "comserv":
                possiblehours = ["50","100","250","500","1000","2500","5000"]
                hours = select(possiblehours)
                message = "You got caught! Your punishment is " + hours + " hours of community service!"
            elif punishment == "prison":
                possibleyears = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
                years = select(possibleyears)
                message = "You got caught! Your punishment is " + years + " years in prison!"
            elif punishment == "serverban":
                units = ["d","w","m","i"]
                unit = select(units)
                if unit == "d":
                    possibledays = ["1","2","3","4","5","6","7"]
                    days = select(possibledays)
                    message = "You got caught! Your punishment is a ban from this server for " + days + " days!\n*Note: This is only a joke, you won't actually get banned.*"
                elif unit == "w":
                    possibleweeks = ["1","2","3","4"]
                    weeks = select(possibleweeks)
                    message = "You got caught! Your punishment is a ban from this server for " + weeks + " weeks!\n*Note: This is only a joke, you won't actually get banned.*"
                elif unit == "m":
                    possiblemonths = ["1","2","3","4","5","6","7","8","9","10","11","12"]
                    months = select(possiblemonths)
                    message = "You got caught! Your punishment is a ban from this server for " + months + " months!\n*Note: This is only a joke, you won't actually get banned.*"
                elif unit == "i":
                    message = "You got caught! Your punishment is a permanent ban from this server!\n*Note: This is only a joke, you won't actually get banned.*"
        await ctx.send(message.replace("@everyone", "@.everyone").replace("@here", "@.here"))

def setup(bot):
    bot.add_cog(Say(bot))
