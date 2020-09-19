import discord
from discord.ext import commands

class Help_Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
        colour = ctx.author.colour
        )
        embed.set_thumbnail(
                url="https://images6.alphacoders.com/537/537683.png"
        )
        embed.set_author(name="Help Menu", icon_url='https://cdn.discordapp.com/avatars/665542847684018189/cae34b00b8bc18ff1772bdee18eeecab.webp?size=128')
        embed.add_field(name='> `inv`', value='***for Bot invite Link***', inline=False)
        embed.add_field(name='> `weather`', value='***Checks weather for citys***', inline=False)
        embed.add_field(name='> `avatar`', value='***Show memebers avatar***', inline=False)
        embed.add_field(name='> `whois`', value='***show info about member***', inline=False)
        embed.add_field(name='> `load`', value='***Load Cogs***', inline=False)
        embed.add_field(name='> `Unload`', value='***Unload Cogs***', inline=False)
        embed.add_field(name='> `ping`', value='***pings the bot***', inline=False)
        embed.set_footer(text=f"Requested by: {ctx.author}")
            
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help_Command(bot))
