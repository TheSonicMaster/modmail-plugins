import discord
import pytz
import datetime

from discord.ext import commands

def getStaffEmbed(self):
    staffeb=discord.Embed(color=self.bot.main_color, title="Staff timings", url="https://github.com/clerickx/modmail-plugins/tree/master/stafftime")
    staffeb.add_field(name="TheSonicMaster", value=getTime('Europe/London'), inline=True)
    staffeb.add_field(name="Captain riggs\:tm:", value=getTime('Asia/Kolkata'), inline=True)
    staffeb.add_field(name="Xinc", value=getTime('Europe/London'), inline=True)
    return staffeb
        
def getTime(timezone):
    return datetime.datetime.now(pytz.timezone(timezone)).strftime("%H:%M (%I:%M %p)")

class stafftime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        if "<@&581196949383020584>" in message.content.lower():
            await message.channel.send(embed=getStaffEmbed())
        elif "<@494884004068327425>" in message.content.lower():
            thesonicmaster = getTime('Europe/London')
            await message.channel.send(f"Please do not ping The Sonic Master. It is considered rude and will not make The Sonic Master respond any faster, especially if The Sonic Master is offline. Be patient for a response and do not expect one immediately.\n\nThe current time of The Sonic Master is {thesonicmaster} (Timezones Exist).")
        elif "<@735550905721684098>" in message.content.lower():
            captain = getTime('Asia/Kolkata')
            await message.channel.send(f"The current time of Captain riggs\:tm: is {captain}. Depending on this time you may need to be patient for a response.")
        elif "<@775023869261381643>" in message.content.lower():
            xinc = getTime('Europe/London')
            await message.channel.send(f"The current time of Xinc is {xinc}. Depending on this time you may need to be patient for a response.")
    
    @commands.command()
    async def stafftime(self, ctx):
        await ctx.send(embed=getStaffEmbed(self))

def setup(bot):
    bot.add_cog(stafftime(bot))
