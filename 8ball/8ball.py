import discord
from discord.ext import commands
import random

anslist = ["I am certain of it.","Without a doubt.","You can count on it!","It is decidedly so.","Signs are pointing to yes.","Better not tell you now","Reply hazy, please try again.","Concentrate and ask again.","Don't count on it.","Outlook not so good.","My sources say no."]

class 8ball(commands.Cog):
    """
    Ask me a yes/no question and get an instant answer!
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['8bl', 'eightball'])
    async def 8ball(self, ctx, *, question):
        """
        Ask me a yes/no question and get an instant answer!
        Usage: [prefix]8ball <question>
        """
        embed=discord.Embed(title=f"Question by {ctx.author}:", description=question, color=0x51eaff)
        embed.set_author(name="8-Ball", url="https://github.com/SupDroidStudio/modmail-plugins/", icon_url="https://media.istockphoto.com/photos/pool-ball-picture-id491993923?k=6&m=491993923&s=612x612&w=0&h=u6SNe9jYA1ZidZ_vfU1LHpaDVNnrbUFivOKxazcrNCI=")
        embed.add_field(name="Answer:", value=random.choice(anslist), inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(8ball(bot))
