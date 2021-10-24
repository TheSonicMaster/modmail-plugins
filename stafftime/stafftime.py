import discord
import pytz
import datetime

from discord.ext import commands

class stafftime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if "<@&581196949383020584>" in message.content.lower():
            thesonicmasterpy = pytz.timezone('Europe/London')
            thesonicmaster = datetime.datetime.now(thesonicmasterpy).strftime("%H:%M (%I:%M %p)")
            amdreepy = pytz.timezone('America/Chicago')
            amdree = datetime.datetime.now(amdreepy).strftime("%H:%M (%I:%M %p)")
            captainpy = pytz.timezone('Asia/Kolkata')
            captain = datetime.datetime.now(captainpy).strftime("%H:%M (%I:%M %p)")
            lifeiscombopy = pytz.timezone('Africa/Cairo')
            lifeiscombo = datetime.datetime.now(lifeiscombopy).strftime("%H:%M (%I:%M %p)")
            minecatpy = pytz.timezone('US/Eastern')
            minecat = datetime.datetime.now(minecatpy).strftime("%H:%M (%I:%M %p)")
            RaptaGpy = pytz.timezone('Europe/Athens')
            RaptaG = datetime.datetime.now(RaptaGpy).strftime("%H:%M (%I:%M %p)")
            staff=discord.Embed(color=self.bot.main_color, title="Staff timings", url="https://github.com/clerickx/modmail-plugins/stafftime")
            staff.add_field(name="TheSonicMaster", value=thesonicmaster, inline=True)
            staff.add_field(name="Amdree", value=amdree, inline=True)
            staff.add_field(name="Captain riggs:tm:", value=captain, inline=True)
            staff.add_field(name="LifeIsCombo", value=lifeiscombo, inline=True)
            staff.add_field(name="MinecatMeow", value=minecat, inline=True)
            staff.add_field(name="RaptaG_", value=RaptaG, inline=True)
            await message.channel.send(embed=staff)
        elif "<@494884004068327425>" in message.content.lower():
            thesonicmasterpy = pytz.timezone('Europe/London')
            thesonicmaster = datetime.datetime.now(thesonicmasterpy).strftime("%H:%M (%I:%M %p)")
            await message.channel.send(f"The current time of TheSonicMaster is {thesonicmaster}. Depending on this time you may need to be patient for a response.")
        elif "<@!494884004068327425>" in message.content.lower():
            thesonicmasterpy = pytz.timezone('Europe/London')
            thesonicmaster = datetime.datetime.now(thesonicmasterpy).strftime("%H:%M (%I:%M %p)")
            await message.channel.send(f"The current time of TheSonicMaster is {thesonicmaster}. Depending on this time you may need to be patient for a response.")
        elif "<@622588567188668416>" in message.content.lower():
            amdreepy = pytz.timezone('America/Chicago')
            amdree = datetime.datetime.now(amdreepy).strftime("%H:%M (%I:%M %p)")
            await message.channel.send(f"The current time of Amdree is {amdree}. Depending on this time you may need to be patient for a response.")
        elif "<@!622588567188668416>" in message.content.lower():
            amdreepy = pytz.timezone('America/Chicago')
            amdree = datetime.datetime.now(amdreepy).strftime("%H:%M (%I:%M %p)")
            await message.channel.send(f"The current time of Amdree is {amdree}. Depending on this time you may need to be patient for a response.")
        elif "<@735550905721684098>" in message.content.lower():
            captainpy = pytz.timezone('Asia/Kolkata')
            captain = datetime.datetime.now(captainpy).strftime("%H:%M (%I:%M %p)")
            await message.channel.send(f"The current time of Captain riggs:tm: is {captain}. Depending on this time you may need to be patient for a response.")
        elif "<@!735550905721684098>" in message.content.lower():
            captainpy = pytz.timezone('Asia/Kolkata')
            captain = datetime.datetime.now(captainpy).strftime("%H:%M (%I:%M %p)")
            await message.channel.send(f"The current time of Captain riggs:tm: is {captain}. Depending on this time you may need to be patient for a response.")
        elif "<@536654456968839215>" in message.content.lower():
            lifeiscombopy = pytz.timezone('Africa/Cairo')
            lifeiscombo = datetime.datetime.now(lifeiscombopy).strftime("%H:%M (%I:%M %p)")
            await message.channel.send(f"The current time of LifeIsCombo is {lifeiscombo}. Depending on this time you may need to be patient for a response.")
        elif "<@!536654456968839215>" in message.content.lower():
            lifeiscombopy = pytz.timezone('Africa/Cairo')
            lifeiscombo = datetime.datetime.now(lifeiscombopy).strftime("%H:%M (%I:%M %p)")
            await message.channel.send(f"The current time of LifeIsCombo is {lifeiscombo}. Depending on this time you may need to be patient for a response.")
        elif "<@845406066505285642>" in message.content.lower():
            minecatpy = pytz.timezone('US/Eastern')
            minecat = datetime.datetime.now(minecatpy).strftime("%H:%M (%I:%M %p)")
            await message.channel.send(f"The current time of MinecatMeow is {minecat}. Depending on this time you may need to be patient for a response.")
        elif "<@!845406066505285642>" in message.content.lower():
            minecatpy = pytz.timezone('US/Eastern')
            minecat = datetime.datetime.now(minecatpy).strftime("%H:%M (%I:%M %p)")
            await message.channel.send(f"The current time of MinecatMeow is {minecat}. Depending on this time you may need to be patient for a response.")
        elif "<@723936869397823489>" in message.content.lower():
            RaptaGpy = pytz.timezone('Europe/Athens')
            RaptaG = datetime.datetime.now(RaptaGpy).strftime("%H:%M (%I:%M %p)")
            await message.channel.send(f"The current time of RaptaG_ is {RaptaG}. Depending on this time you may need to be patient for a response.") 
        elif "<@!723936869397823489>" in message.content.lower():
            RaptaGpy = pytz.timezone('Europe/Athens')
            RaptaG = datetime.datetime.now(RaptaGpy).strftime("%H:%M (%I:%M %p)")
            await message.channel.send(f"The current time of RaptaG_ is {RaptaG}. Depending on this time you may need to be patient for a response.")
    
    @commands.command()
    async def stafftime(self, ctx):
        thesonicmasterpy = pytz.timezone('Europe/London')
        thesonicmaster = datetime.datetime.now(thesonicmasterpy).strftime("%H:%M (%I:%M %p)")
        amdreepy = pytz.timezone('America/Chicago')
        amdree = datetime.datetime.now(amdreepy).strftime("%H:%M (%I:%M %p)")
        captainpy = pytz.timezone('Asia/Kolkata')
        captain = datetime.datetime.now(captainpy).strftime("%H:%M (%I:%M %p)")
        lifeiscombopy = pytz.timezone('Africa/Cairo')
        lifeiscombo = datetime.datetime.now(lifeiscombopy).strftime("%H:%M (%I:%M %p)")
        minecatpy = pytz.timezone('US/Eastern')
        minecat = datetime.datetime.now(minecatpy).strftime("%H:%M (%I:%M %p)")
        RaptaGpy = pytz.timezone('Europe/Athens')
        RaptaG = datetime.datetime.now(RaptaGpy).strftime("%H:%M (%I:%M %p)")
        staff=discord.Embed(color=self.bot.main_color, title="Staff timings", url="https://github.com/clerickx/modmail-plugins/stafftime")
        staff.add_field(name="TheSonicMaster", value=thesonicmaster, inline=True)
        staff.add_field(name="Amdree", value=amdree, inline=True)
        staff.add_field(name="Captain riggs:tm:", value=captain, inline=True)
        staff.add_field(name="LifeIsCombo", value=lifeiscombo, inline=True)
        staff.add_field(name="MinecatMeow", value=minecat, inline=True)
        staff.add_field(name="RaptaG_", value=RaptaG, inline=True)
        await ctx.send(embed=staff)

def setup(bot):
    bot.add_cog(stafftime(bot))
