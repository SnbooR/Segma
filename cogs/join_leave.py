import discord
from discord.ext import commands
import asyncio

class Join_Leave(commands.Cog):
    """Welcomes members on join, and leaving"""

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

#joining

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel("channel_id")
        await channel.send(f'Welcome to the server {member.mention}')
# leaving

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel("channel_id")
        await channel.send(f'Member has just left {member.mention}')

def setup(bot):
    bot.add_cog(Join_Leave(bot))
