import os
import discord
import itertools
import threading
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

#----------------------------Commands---------------------------------

class Main_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
#pings the bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Ping is: `{round(self.bot.latency * 1000)}ms`')
    
# invite the bot.

    @commands.command(description="Get a link to invite me.", usage="invite")
    async def invite(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="Invite Link",
                description=f"https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}"
                    "&permissions=268823640&scope=bot",
                colour=ctx.author.colour,
                )
            )

# show member's avatar.

    @commands.command(name='avatar', aliases=['Avatar'])
    async def av_cmd(self, ctx, user: discord.Member):
        embed = discord.Embed(
        colour = ctx.author.colour,
        title=f"{user}"
        )
        embed.set_image(url=f"{user.avatar_url}")
        await ctx.send(embed=embed)

# if the member don't mention a member then send his own avatar.

    @av_cmd.error
    async def av_error(self, ctx, error):
        if isinstance (error, commands.MissingRequiredArgument):

            embed = discord.Embed(
                colour = ctx.author.colour,
                title=f"{ctx.author}"
                )
            embed.set_image(url=f"{ctx.author.avatar_url}")
            await ctx.send(embed=embed)
    
#simple whois command that shows when did the user join the server and his avatar and the user ID
    
    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        embed = discord.Embed(colour=ctx.author.colour, timestamp=ctx.message.created_at,
                                    title=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="ID:", value=member.id, inline=False)
        embed.add_field(name="Display Name:", value=member.display_name, inline=True)

        await ctx.send(embed=embed)

# register the class
def setup(bot):
    bot.add_cog(Main_Commands(bot))
