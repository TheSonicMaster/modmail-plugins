import discord
import pytz
import datetime

from discord.ext import commands

class stafftime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if discord.utils.get(message.guild.roles, id=581366844796043274) not in message.author.roles:
            if "<@&581196949383020584>" in message.content.lower():
                thesonicmaster = datetime.datetime.now(pytz.timezone('Europe/London')).strftime("%H:%M (%I:%M %p)")
                captain = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%H:%M (%I:%M %p)")
                minecat = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M (%I:%M %p)")
                staff=discord.Embed(color=self.bot.main_color, title="Staff timings", url="https://github.com/clerickx/modmail-plugins/tree/master/stafftime")
                staff.add_field(name="TheSonicMaster", value=thesonicmaster, inline=True)
                staff.add_field(name="Captain riggs:tm:", value=captain, inline=True)
                staff.add_field(name="MinecatMeow", value=minecat, inline=True)
                await message.channel.send(embed=staff)
            elif "<@494884004068327425>" in message.content.lower():
                thesonicmaster = datetime.datetime.now(pytz.timezone('Europe/London')).strftime("%H:%M (%I:%M %p)")
                await message.channel.send(f"Please do not ping The Sonic Master. It is considered rude and will not make The Sonic Master respond any faster, especially if The Sonic Master is offline. Be patient for a response and do not expect one immediately.\n\nThe current time of The Sonic Master is {thesonicmaster} (Timezones Exist).")
            elif "<@!494884004068327425>" in message.content.lower():
                thesonicmaster = datetime.datetime.now(pytz.timezone('Europe/London')).strftime("%H:%M (%I:%M %p)")
                await message.channel.send(f"Please do not ping The Sonic Master. It is considered rude and will not make The Sonic Master respond any faster, especially if The Sonic Master is offline. Be patient for a response and do not expect one immediately.\n\nThe current time of The Sonic Master is {thesonicmaster}. (Timezones Exist).")
            elif "<@735550905721684098>" in message.content.lower():
                captain = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%H:%M (%I:%M %p)")
                await message.channel.send(f"The current time of Captain riggs:tm: is {captain}. Depending on this time you may need to be patient for a response.")
            elif "<@!735550905721684098>" in message.content.lower():
                captain = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%H:%M (%I:%M %p)")
                await message.channel.send(f"The current time of Captain riggs:tm: is {captain}. Depending on this time you may need to be patient for a response.")
            elif "<@845406066505285642>" in message.content.lower():
                minecat = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M (%I:%M %p)")
                await message.channel.send(f"The current time of MinecatMeow is {minecat}. Depending on this time you may need to be patient for a response.")
            elif "<@!845406066505285642>" in message.content.lower():
                minecat = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M (%I:%M %p)")
                await message.channel.send(f"The current time of MinecatMeow is {minecat}. Depending on this time you may need to be patient for a response.")
    
    @commands.command()
    async def stafftime(self, ctx):
        thesonicmaster = datetime.datetime.now(pytz.timezone('Europe/London')).strftime("%H:%M (%I:%M %p)")
        captain = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%H:%M (%I:%M %p)")
        minecat = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M (%I:%M %p)")
        staff=discord.Embed(color=self.bot.main_color, title="Staff timings", url="https://github.com/clerickx/modmail-plugins/tree/master/stafftime")
        staff.add_field(name="TheSonicMaster", value=thesonicmaster, inline=True)
        staff.add_field(name="Captain riggs:tm:", value=captain, inline=True)
        staff.add_field(name="MinecatMeow", value=minecat, inline=True)
        await ctx.send(embed=staff)

def setup(bot):
    bot.add_cog(stafftime(bot))
