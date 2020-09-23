import discord
from discord.ext import commands


class OwnerCommands(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.has_guild_permissions(manage_guild=True)
    async def servers(self, ctx):
        """
        Show the guilds your bot in
        """
        activeservers = self.bot.guilds
        for guild in activeservers:
            await ctx.send(guild.name)
            await ctx.send(guild.id)

def setup(bot):
    bot.add_cog(OwnerCommands(bot))