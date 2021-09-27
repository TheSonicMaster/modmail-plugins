import discord
from random import randint as select
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def yes(self, ctx, *, message):
        """Similar to echo, but repeats the output several times."""
        loopcount = select(1,10)
        name = str(ctx.author)
        final = message
        for i in range(1,loopcount):
            final = final + "\n" + message
        final = final + "\nCommand `yes` run by " + name
        await ctx.send(final.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere").replace("@everyone", "@.everyone").replace("@here", "@.here").replace("<@&581197130983800852>", "@.TheSonicMaster").replace("<@&581196949383020584>", "@.Staff").replace("<@&768749656388796436>", "@.Bot Developer").replace("<@&869259187719393320>", "@.Graphic Designer").replace("<@&852675563038179368>", "@.Server Booster").replace("<@&637739972174151689>", "@.VIP").replace("<@&631154626993061902>", "@.MC Map Contributor").replace("<@&819284703987236906>", "@.Super Secret").replace("<@&757188660742455296>", "@.Mew").replace("<@&837010087830618162>", "@.Chad").replace("<@&639473367316955171>", "@.Secret").replace("<@&639546711387144195>", "@.oof").replace("<@&592036135774060551>", "@.Canary").replace("<@&627463051712659494>", "@.Nostalgic").replace("<@&690902448478617631>", "@.Artist").replace("<@&618879701326233600>", "@.Gamer").replace("<@&589110560344375297>", "@.Hacker").replace("<@&639415893113307138>", "@.Musician").replace("<@&798870960308486156>", "@.Photographer").replace("<@&591521552453861386>", "@.human").replace("<@&581196486533054504>", "@.Member"))

def setup(bot):
    bot.add_cog(Say(bot))
