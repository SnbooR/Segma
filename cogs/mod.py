import discord
from discord.ext import commands


class Moderation(commands.Cog):
    """Mod Commands"""
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-------")

    @commands.command(name="ban", description="Bans member")
    @commands.has_guild_permissions(ban_members=True)
    @commands.guild_only()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """
        Ban members from the guild
        """
        await ctx.send("*man just got shit on*")
        await ctx.guild.ban(user=member, reason=reason)

    # Logs the members who has been banned
        channel = self.bot.get_channel(757742628308779078)

        embed = discord.Embed(title=f"{ctx.author.name} Just banned: {member.name}", description=reason)
        await channel.send(embed=embed)


 
    @commands.command(name="kick", description="kicks member")
    @commands.has_guild_permissions(kick_members=True)
    @commands.guild_only()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """
        Kick members from the guild
        """
        await ctx.send("*yup, just got KICKED*")
        await ctx.guild.kick(user=member, reason=reason)

    # Logs the members who has been banned or kicked or muted
        channel = self.bot.get_channel(757742628308779078)
        embed = discord.Embed(title=f"{ctx.author.name} Just kicked: {member.name}", description=reason)
        await channel.send(embed=embed)


    # unban members
    
    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, member, *, reason=None):
        """
        Unban members
        """
        member = await self.bot.fetch_user(int(member))
        await ctx.send("*Inhaled*")
        await ctx.guild.unban(member, reason=reason)

        channel = self.bot.get_channel(757742628308779078)
        embed = discord.Embed(title=f"{ctx.author.name} Just unbanned: {member.name}", description=reason)
        await channel.send(embed=embed)

    #purge command
    @commands.command(aliases=["clean"])
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, amount=15):
        """
        Clean the chat
        """
        await ctx.channel.purge(limit=amount+1)

        channel = self.bot.get_channel(757742628308779078)
        embed = discord.Embed(title=f"{ctx.author.name} purgeed: {ctx.channel.name}", description=f"{amount} messages", inline=False)
        await channel.send(embed=embed)

    #mute command - note! not working currently
    @commands.command(name="mute")
    @commands.has_guild_permissions(mute_members=True)
    @commands.guild_only()
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """
        Mute members
        """
        await member.mute(reason=reason)
        await ctx.send(f'User {member.name} is muted ')

def setup(bot):
    bot.add_cog(Moderation(bot))
